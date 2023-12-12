from tkinter import *
from tkinter import messagebox
from PIL import Image

firstWidth = 775
firstHeight = 600

data_frame_width = 300
data_frame_height =350

def center_window(width=500, height=240):

    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = Tk()
root.title("ElectroBouTool")
center_window(firstWidth, firstHeight)
root.resizable(FALSE, FALSE)
root.iconbitmap("resources\lightning-bolt-16.ico")

#---------------------------------- MENU ACTIONS ---------------------------------------------
def menuInit():
    hide_all_frames()
    main_frame.pack(fill="both", expand=True)

def menuExit():
    data=messagebox.askquestion("Exit", "Do you want to exit?")

    if data=="yes":
        root.quit()

def menuDivider():
    hide_all_frames()
    divider_frame.pack(fill="both", expand=True)

    entri_divider_frame.pack()
    entri_divider_frame.pack_propagate(False)
    entri_divider_frame.place(x=350, y=15)

    labelVin = Label(entri_divider_frame, text="Vin:", bg="white", font=('Arial', 25))
    labelVin.grid(row=0, column=0, padx=10, pady=10)
    squareVin=Entry(entri_divider_frame, width=10, highlightthickness=2, font=('Arial', 20), justify='center', textvariable=varVin)
    squareVin.grid(row=0, column=1, padx=10, pady=10)
    labelVinUnits = Label(entri_divider_frame, text="V", bg="white", font=('Arial', 25))
    labelVinUnits.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    labelR1 = Label(entri_divider_frame, text="R1:", bg="white", font=('Arial', 25))
    labelR1.grid(row=1, column=0, padx=10, pady=10)
    squareR1=Entry(entri_divider_frame, width=10, highlightthickness=2, font=('Arial', 20), justify='center', textvariable=varR1)
    squareR1.grid(row=1, column=1, padx=10, pady=10)
    labelR1Units = Label(entri_divider_frame, text="Ohms", bg="white", font=('Arial', 25))
    labelR1Units.grid(row=1, column=2, padx=10, pady=10)

    labelR2 = Label(entri_divider_frame, text="R2:", bg="white", font=('Arial', 25))
    labelR2.grid(row=2, column=0, padx=10, pady=10)
    squareR2=Entry(entri_divider_frame, width=10, highlightthickness=2, font=('Arial', 20), justify='center', textvariable=varR2)
    squareR2.grid(row=2, column=1, padx=10, pady=10)
    labelR2Units = Label(entri_divider_frame, text="Ohms", bg="white", font=('Arial', 25))
    labelR2Units.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    labelVout = Label(entri_divider_frame, text="Vout:", bg="white", font=('Arial', 25))
    labelVout.grid(row=3, column=0, padx=10, pady=10)
    squareVout=Entry(entri_divider_frame, width=10, highlightthickness=2, font=('Arial', 20), justify='center', textvariable=varVout)
    squareVout.grid(row=3, column=1, padx=10, pady=10)
    labelVoutUnits = Label(entri_divider_frame, text="V", bg="white", font=('Arial', 25))
    labelVoutUnits.grid(row=3, column=2, padx=10, pady=10, sticky="w")

    button_calculate=Button(entri_divider_frame, text="Calculate", font=('Arial', 12), command=calculateDivider)
    button_calculate.grid(row=4, column=1, sticky="w", padx=10, pady=10)

    button_reset=Button(entri_divider_frame, text="Clear all", font=('Arial', 12), command=clearAll)
    button_reset.grid(row=4, column=2, sticky="w", padx=10, pady=10)

def menuResistor():
    hide_all_frames()
    resistor_frame.pack(fill="both", expand=True)

    entri_res_frame.pack()
    entri_res_frame.pack_propagate(False)
    entri_res_frame.place(x=350, y=15)

    res_labelR1 = Label(entri_res_frame, text="R1:", bg="white", font=('Arial', 25))
    res_labelR1.grid(row=1, column=0, padx=10, pady=10)
    res_squareR1=Entry(entri_res_frame, width=10, highlightthickness=2, font=('Arial', 20), justify='center', textvariable=res_varR1)
    res_squareR1.grid(row=1, column=1, padx=10, pady=10)
    res_labelR1Units = Label(entri_res_frame, text="Ohms", bg="white", font=('Arial', 25))
    res_labelR1Units.grid(row=1, column=2, padx=10, pady=10)

    res_labelR2 = Label(entri_res_frame, text="R2:", bg="white", font=('Arial', 25))
    res_labelR2.grid(row=2, column=0, padx=10, pady=10)
    res_squareR2=Entry(entri_res_frame, width=10, highlightthickness=2, font=('Arial', 20), justify='center', textvariable=res_varR2)
    res_squareR2.grid(row=2, column=1, padx=10, pady=10)
    res_labelR2Units = Label(entri_res_frame, text="Ohms", bg="white", font=('Arial', 25))
    res_labelR2Units.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    res_labelVout = Label(entri_res_frame, text="Req =", bg="white", font=('Arial', 25))
    res_labelVout.grid(row=3, column=0, padx=10, pady=10)
    res_squareVout=Entry(entri_res_frame, width=10, highlightthickness=2, font=('Arial', 20), justify='center', textvariable=res_varReq)
    res_squareVout.grid(row=3, column=1, padx=10, pady=10)
    res_labelVoutUnits = Label(entri_res_frame, text="Ohms", bg="white", font=('Arial', 25))
    res_labelVoutUnits.grid(row=3, column=2, padx=10, pady=10, sticky="w")

    res_button_calculate=Button(entri_res_frame, text="Calculate", font=('Arial', 12), command=calculateResistor)
    res_button_calculate.grid(row=4, column=1, sticky="w", padx=10, pady=10)

    res_button_reset=Button(entri_res_frame, text="Clear all", font=('Arial', 12), command=res_clearAll)
    res_button_reset.grid(row=4, column=2, sticky="w", padx=10, pady=10)

def menuLights():
    hide_all_frames()
    auto_lights_frame.pack(fill="both", expand=True)

def doNothing():
    pass

def hide_all_frames():
    main_frame.pack_forget()
    divider_frame.pack_forget()
    entri_divider_frame.pack_forget()    
    resistor_frame.pack_forget()
    auto_lights_frame.pack_forget()

#---------------------------------- MENU ACTIONS END ---------------------------------------------

menubar = Menu(root)
root.config(menu=menubar)

menuFile = Menu(menubar, tearoff="off")
menubar.add_cascade(label ="File", menu=menuFile)
menuFile.add_command(label="Init", command=menuInit)
menuFile.add_separator()
menuFile.add_command(label="Exit", command=menuExit)

menuTools = Menu(menubar, tearoff="off")
menubar.add_cascade(label ="Tools", menu=menuTools)
menuTools.add_command(label="Divider calculator", command=menuDivider)
menuTools.add_command(label="Resistor calculator", command=menuResistor)

menuAutomation = Menu(menubar, tearoff="off")
menubar.add_cascade(label ="Automation", menu=menuAutomation)
menuAutomation.add_command(label="Lights", command=menuLights)
menuAutomation.add_command(label="Windows", command=doNothing)

menuEdit = Menu(menubar, tearoff="off")
menubar.add_cascade(label ="Edit", menu=menuEdit)
menuEdit.add_command(label="Clear", command=doNothing)
menuEdit.add_command(label="Copy", command=doNothing)

menuHelp = Menu(menubar, tearoff="off")
menubar.add_cascade(label ="Help", menu=menuHelp)
menuHelp.add_command(label="License", command=doNothing)
menuHelp.add_command(label="About", command=doNothing)

#---------------------------------- MAIN FRAME ------------------------------------------------

main_frame = Frame(root, width=firstWidth, height=firstHeight, bg="green")

bgmain = PhotoImage(file="resources/mainwin.png")
bg_label_main = Label(main_frame, image=bgmain)
bg_label_main.place(x=0, y=0, relwidth=1, relheight=1)

main_frame.pack(fill="both", expand=True)

main_button_divider=Button(main_frame, text="Divider calculator", font=('Arial', 12), command=menuDivider)
main_button_divider.place(x=165, y=400)

main_button_res=Button(main_frame, text="Resistor calculate", font=('Arial', 12), command=menuResistor)
main_button_res.place(x=465, y=400)

#---------------------------------- DIVIDER TOOL -----------------------------------------------

divider_frame = Frame(root, width=firstWidth, height=firstHeight, bg="red")

bg = PhotoImage(file="resources/backgrounddt.png")
bg_label_divider = Label(divider_frame, image=bg)
bg_label_divider.place(x=0, y=0, relwidth=1, relheight=1)

entri_divider_frame = Frame(divider_frame, width=300, height=300, bd=5, bg="white")

#---------------------------------- BUTTONS DIVIDER ---------------------------------------------
varVin=StringVar()
varR1=StringVar()
varR2=StringVar()
varVout=StringVar()

def calculateDivider():
    data = (varVin.get(), varR1.get(), varR2.get(), varVout.get())
    #print(data)
    j=0
    for i in range(4):
        if data[i] == '':
            j+=1
            #print(f"Campos vacios: {j}")
        

    if j==0 or j >= 2:
        messagebox.showwarning("Warninig", "Leave only one field empty.")

    else:
        stringVin = varVin.get()
        stringR1 = varR1.get()
        stringR2 = varR2.get()
        stringVout = varVout.get()

        if data[0]=='':
            #print("Despejamos Vin")
            R1 = float(stringR1)
            R2 = float(stringR2)
            Vout = float(stringVout)

            Vin = Vout/(R2/(R1+R2))
            varVin.set("{: .3f}".format(Vin))

        if data[1]=='':
            #print("Despejamos R1")
            Vin = float(stringVin)
            R2 = float(stringR2)
            Vout = float(stringVout)

            R1 = int((R2/Vout)*Vin-R2)
            varR1.set("{: d}".format(R1))

        if data[2]=='':
            #print("Despejamos R2")
            Vin = float(stringVin)
            R1 = float(stringR1)
            Vout = float(stringVout)

            R2 = int((Vout*R1)/(Vin-Vout))
            varR2.set("{: d}".format(R2))

        if data[3]=='':
            #print("Despejamos Vout")
            Vin = float(stringVin)
            R1 = float(stringR1)
            R2 = float(stringR2)

            Vout = R2/(R1+R2)*Vin
            varVout.set("{: .3f}".format(Vout))


def clearAll():
    varVin.set("")
    varR1.set("")
    varR2.set("")
    varVout.set("")
#---------------------------------- BUTTONS DIVIDER END -----------------------------------------

#---------------------------------- CALCULATOR RESISTOR TOOL ------------------------------------

resistor_frame = Frame(root, width=firstWidth, height=firstHeight, bg="blue")

bgres = PhotoImage(file="resources/resparallel.png")
bg_label_res = Label(resistor_frame, image=bgres)
bg_label_res.place(x=0, y=0, relwidth=1, relheight=1)

entri_res_frame = Frame(resistor_frame, width=300, height=300, bd=5, bg="white")

#---------------------------------- BUTTONS RESISTOR ---------------------------------------------
res_varR1=StringVar()
res_varR2=StringVar()
res_varReq=StringVar()

def calculateResistor():
    data = (res_varR1.get(), res_varR2.get())
    #print(data)
    j=0
    for i in range(2):
        if data[i] == '':
            j+=1
            #print(f"Campos vacios: {j}")

    if j >= 1:
        messagebox.showwarning("Warninig", "Insert the value of R1 and R2.")
        res_clearAll()

    else:
        res_stringR1 = res_varR1.get()
        res_stringR2 = res_varR2.get()    

        R1 = int(res_stringR1)
        R2 = int(res_stringR2)

        Req = int(1/((1/R1) + (1/R2)))
        res_varReq.set("{: d}".format(Req))

def res_clearAll():

    res_varR1.set("")
    res_varR2.set("")
    res_varReq.set("")

#---------------------------------- BUTTONS RESISTOR END -----------------------------------------

#---------------------------------- DDBB MANAGER TOOL --------------------------------------------

auto_lights_frame = Frame(root, width=firstWidth, height=firstHeight, bg="yellow")

root.mainloop()
