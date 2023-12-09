from tkinter import *
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

def menuDivider():
    hide_all_frames()

    divider_frame.pack(fill="both", expand=True)

    entri_divider_frame.pack()
    entri_divider_frame.pack_propagate(False)
    entri_divider_frame.place(x=firstWidth-315, y=15)

    labelVin = Label(entri_divider_frame, text="Vin:", bg="white")
    labelVin.grid(row=0, column=0, padx=10, pady=10)
    squareVin=Entry(entri_divider_frame, highlightthickness=2)
    squareVin.grid(row=0, column=1, padx=10, pady=10)
    labelVinUnits = Label(entri_divider_frame, text="V", bg="white")
    labelVinUnits.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    labelR1 = Label(entri_divider_frame, text="R1:", bg="white")
    labelR1.grid(row=1, column=0, padx=10, pady=10)
    squareR1=Entry(entri_divider_frame, highlightthickness=2)
    squareR1.grid(row=1, column=1, padx=10, pady=10)
    labelR1Units = Label(entri_divider_frame, text="Ohms", bg="white")
    labelR1Units.grid(row=1, column=2, padx=10, pady=10)

    labelR2 = Label(entri_divider_frame, text="R2:", bg="white")
    labelR2.grid(row=2, column=0, padx=10, pady=10)
    squareR2=Entry(entri_divider_frame, highlightthickness=2)
    squareR2.grid(row=2, column=1, padx=10, pady=10)
    labelR2Units = Label(entri_divider_frame, text="Ohms", bg="white")
    labelR2Units.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    labelVout = Label(entri_divider_frame, text="Vout:", bg="white")
    labelVout.grid(row=3, column=0, padx=10, pady=10)
    squareVout=Entry(entri_divider_frame, highlightthickness=2)
    squareVout.grid(row=3, column=1, padx=10, pady=10)
    labelVoutUnits = Label(entri_divider_frame, text="V", bg="white")
    labelVoutUnits.grid(row=3, column=2, padx=10, pady=10, sticky="w")

def menuResistor():
    hide_all_frames()
    resistor_frame.pack(fill="both", expand=True)

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
menuFile.add_command(label="Exit", command=root.quit)

menuTools = Menu(menubar, tearoff="off")
menubar.add_cascade(label ="Tools", menu=menuTools)
menuTools.add_command(label="Divider", command=menuDivider)
menuTools.add_command(label="Resistor calculate", command=menuResistor)

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

#---------------------------------- MAIN FRAME ---------------------------------------------

main_frame = Frame(root, width=firstWidth, height=firstHeight, bg="green")
main_frame.pack(fill="both", expand=True)

#---------------------------------- DIVIDER TOOL ---------------------------------------------

divider_frame = Frame(root, width=firstWidth, height=firstHeight, bg="red")

bg = PhotoImage(file="resources/backgrounddt.png")
bg_label_divider = Label(divider_frame, image=bg)
bg_label_divider.place(x=0, y=0, relwidth=1, relheight=1)

entri_divider_frame = Frame(divider_frame, width=300, height=300, bd=5, bg="white")

#---------------------------------- CALCULATOR RESISTOR TOOL ---------------------------------------------

resistor_frame = Frame(root, width=firstWidth, height=firstHeight, bg="blue")

#---------------------------------- DDBB MANAGER TOOL ---------------------------------------------

auto_lights_frame = Frame(root, width=firstWidth, height=firstHeight, bg="yellow")

root.mainloop()
