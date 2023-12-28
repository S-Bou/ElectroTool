/*WiFi manager to check DDBB state of some devices*/

#include <stdio.h>
#include <sys/param.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/timers.h"
#include "freertos/event_groups.h"
#include "esp_wifi.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "esp_netif.h"
#include "esp_http_client.h"
#include "esp_http_server.h"
#include "esp_tls.h"
#include "driver/gpio.h"
#include "datacon.h"

static const char* TAG = "MyModule";
int phplen = 0;
char phpinfo[200];
char status[3]; 

// ------------------------ GPIOs CONFIG ---------------------------------------------------------------------

#define GREEN_LED_GPIO GPIO_NUM_16
#define RED_LED_GPIO GPIO_NUM_4
#define ONBOARD_LED_GPIO GPIO_NUM_2

static uint8_t green_led_state = 0;
static uint8_t red_led_state = 0;
static uint8_t onboard_led_state = 0;

static void configure_gpios(void)
{
    ESP_LOGI(TAG, "Configuration of GPIOs");
    gpio_reset_pin(GREEN_LED_GPIO);
    gpio_reset_pin(RED_LED_GPIO);
    gpio_reset_pin(ONBOARD_LED_GPIO);
    /* Set the GPIO as a push/pull output */
    gpio_set_direction(GREEN_LED_GPIO, GPIO_MODE_OUTPUT);
    gpio_set_direction(RED_LED_GPIO, GPIO_MODE_OUTPUT);
    gpio_set_direction(ONBOARD_LED_GPIO, GPIO_MODE_OUTPUT);
}

// ------------------------ WiFi CONNECTION -------------------------------------------------------------------

static void wifi_event_handler(void *event_handler_arg, esp_event_base_t event_base, int32_t event_id, void *event_data)
{
    switch (event_id)
    {
    case WIFI_EVENT_STA_START:
        printf("WiFi connecting ... \n");
        break;
    case WIFI_EVENT_STA_CONNECTED:
        printf("WiFi connected ... \n");
        break;
    case WIFI_EVENT_STA_DISCONNECTED:
        printf("WiFi lost connection ... \n");
        onboard_led_state = 1; 
        gpio_set_level(ONBOARD_LED_GPIO, onboard_led_state); 
        break;
    case IP_EVENT_STA_GOT_IP:
        printf("WiFi got IP ... \n\n");
        break;
    default:
        break;
    }
}

void wifi_connection()
{
    // 1 - Wi-Fi/LwIP Init Phase
    esp_netif_init();                    // TCP/IP initiation 					s1.1
    esp_event_loop_create_default();     // event loop 			                s1.2
    esp_netif_create_default_wifi_sta(); // WiFi station 	                    s1.3
    wifi_init_config_t wifi_initiation = WIFI_INIT_CONFIG_DEFAULT();
    esp_wifi_init(&wifi_initiation); // 					                    s1.4
    // 2 - Wi-Fi Configuration Phase
    esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, wifi_event_handler, NULL);
    esp_event_handler_register(IP_EVENT, IP_EVENT_STA_GOT_IP, wifi_event_handler, NULL);
    wifi_config_t wifi_configuration = {
        .sta = {
        .ssid = SSID,
        .password = PASS}};
    esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_configuration);
    // 3 - Wi-Fi Start Phase
    esp_wifi_start();
    // 4- Wi-Fi Connect Phase
    esp_wifi_connect();
}

// ------------------------ GET EVENT -------------------------------------------------------------------------

esp_err_t client_event_get_handler(esp_http_client_event_handle_t evt)
{
    static char *output_buffer;
    static int output_len;

    switch (evt->event_id)
    {
        case HTTP_EVENT_ON_DATA:
            ESP_LOGI(TAG, "HTTP_EVENT_ON_DATA, len=%d", evt->data_len);
            if (!esp_http_client_is_chunked_response(evt->client)){
                if (evt->user_data){
                    memcpy(evt->user_data + output_len, evt->data, evt->data_len);
                }else{
                    if(output_buffer == NULL){
                        output_buffer = (char *) malloc(esp_http_client_get_content_length(evt->client));
                        output_len = 0;
                        if(output_buffer == NULL){
                            ESP_LOGE(TAG, "Failled to alocate memory for output buffer");
                            return ESP_FAIL;
                        }
                    }
                    memcpy(output_buffer + output_len, evt->data, evt->data_len);
                    phplen = evt->data_len;
                    for (int8_t i = 0; i < evt->data_len; i++)
                    {
                        phpinfo[i] = output_buffer[i];
                    }
                }
                output_len += evt->data_len;
            }
            break;

        case HTTP_EVENT_ON_FINISH:
            ESP_LOGD(TAG, "HTTP_EVENT_ON_FINISH");
            if (output_buffer != NULL){
                free(output_buffer);
                output_buffer = NULL;
            }
            output_len = 0;
            break;

        case HTTP_EVENT_DISCONNECTED:
            ESP_LOGI(TAG, "HTTP_EVENT_DISCONECTED");
            int mbedtls_err = 0;
            esp_err_t err = esp_tls_get_and_clear_last_error(evt->data, &mbedtls_err, NULL);
            if (err != 0){
                ESP_LOGI(TAG, "Last esp error code: 0x%x", err);
                ESP_LOGI(TAG, "Last mbedtls failure: 0x%x", mbedtls_err);
            }
            if (output_buffer != NULL){
                free(output_buffer);
                output_buffer = NULL;
            }
            output_len = 0;
            break;

        default:
            break;

    }
    return ESP_OK;
}

static void find_dev_status(void){

    for (int8_t i=0; i < phplen; i++)
    {
        if(phpinfo[i] == '#' && phpinfo[i+1] == '0' && phpinfo[i+2] == '1' ){
            printf("Finded: %c%c%c\n", phpinfo[i], phpinfo[i+1], phpinfo[i+2]);
            i = i+4;
            if(phpinfo[i] == 'n'){
                printf("Green = on\n");
                green_led_state = 1;

            }else if(phpinfo[i] == 'f'){
                printf("Green = off\n");
                green_led_state = 0;               
            }
            gpio_set_level(GREEN_LED_GPIO, green_led_state); 

        }else if(phpinfo[i] == '#' && phpinfo[i+1] == '0' && phpinfo[i+2] == '2' ){
            printf("Finded: %c%c%c\n", phpinfo[i], phpinfo[i+1], phpinfo[i+2]);
            i = i+4;
            if(phpinfo[i] == 'n'){
                printf("Red = on\n");
                red_led_state = 1;

            }else if(phpinfo[i] == 'f'){
                printf("Red = off\n");
                red_led_state = 0;               
            }
            gpio_set_level(RED_LED_GPIO, red_led_state);
        } 
    }
}

static void client_get_function()
{
    esp_http_client_config_t config_get = {
        .url = IP_FILE_PHP,
        .method = HTTP_METHOD_GET,
        .event_handler = client_event_get_handler
    };
        
    esp_http_client_handle_t client_get = esp_http_client_init(&config_get);

    printf("1 ...........\n");
    esp_http_client_perform(client_get);
    printf("2 ...........\n\n");
    esp_http_client_cleanup(client_get);

    find_dev_status();
}

// -------------------------- MAIN ------------------------------------------------------------------------

void app_main(void)
{
    configure_gpios();

    nvs_flash_init();
    wifi_connection();

    vTaskDelay(3000 / portTICK_PERIOD_MS);
    printf("WIFI was initiated ...........\n\n");
    onboard_led_state = 0; 
    gpio_set_level(ONBOARD_LED_GPIO, onboard_led_state); 

    while(1){
        client_get_function();
        vTaskDelay(2000 / portTICK_PERIOD_MS);
    }
}
