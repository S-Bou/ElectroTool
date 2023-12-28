import mysql.connector
from mysql.connector import Error
import dataconn

class DbError(Exception):
    "Exception to show when error is produced when try to query/update the DDBB"
    pass

def get_dev_status(device):

    try:
        echo = get_query("SELECT status FROM myhome WHERE dev_name = '{}';" .format(device))[0][0]
    except:
        raise DbError

    print(f"Status of device {device} -> {echo}")

    return echo

def set_dev_status(device, status):

    try:
        echo = set_query("UPDATE myhome SET status = '{}' WHERE dev_name = '{}';" .format(status, device))
    except:
        raise DbError

    print(f"Updated device {device} -> {status}")

    return True


def get_query(myquery):

    try:
        print("Init GET Query conection ....")
        connection = mysql.connector.connect(host = dataconn.ipDIR,
                                             database = dataconn.db_name,
                                             user = dataconn.user_name,
                                             password = dataconn.psw_user,
                                             connection_timeout=7)

        cursor = connection.cursor()
        cursor.execute(myquery)
        data = cursor.fetchall()

    except Error:
        raise DbError

    else:
        cursor.close()
        connection.close()
        return data

def set_query(myquery):

    try:
        print("Init SET Query conection ....")
        connection = mysql.connector.connect(host = dataconn.ipDIR,
                                             database = dataconn.db_name,
                                             user = dataconn.user_name,
                                             password = dataconn.psw_user,
                                             connection_timeout=7)

        cursor = connection.cursor()
        cursor.execute(myquery)
        connection.commit()

    except Error:
        raise DbError

    else:
        cursor.close()
        connection.close()
        return True

def main():

    try:
        # Code for do tests
        device = 'green'
        status = get_dev_status(device)
        status = 'off'
        set_dev_status(device, status)

    except KeyboardInterrupt:
        print("Keyboard interrupt")

if (__name__ == '__main__'):
    main()
