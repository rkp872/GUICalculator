from tkinter import *
from tkinter.messagebox import *
import math as m

# variables
font = ('Arial ', 22, 'bold ')


# Functions
def click_btn(event):
    b = event.widget
    text = b['text']
    # print(text)
    if (text == '='):
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            # print("ERROR : ",e)
            showerror("ERROR", "Invaid Syntax")
        return
    if (text == 'x'):
        textField.insert(END, '*')
        return

    textField.insert(END, text)


def all_clear():
    textField.delete(0, END)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


# Window
window = Tk()
window.title("RGR INSTRUMENTS")
window.geometry('430x523')

# Picture label
pic = PhotoImage(file='img.png')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=10)

# heading
heading = Label(window, text="RGR INSTRUMENTS", font=font, underline=0)
heading.pack(side=TOP)

# Textfileld
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

# Buttons

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)
# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white')
        btn.grid(row=i, column=j, padx=3, pady=3)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
zeroBtn.grid(row=3, column=0, padx=3, pady=3)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
dotBtn.grid(row=3, column=1, padx=3, pady=3)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
equalBtn.grid(row=3, column=2, padx=3, pady=3)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
plusBtn.grid(row=0, column=3, padx=3, pady=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
minusBtn.grid(row=1, column=3, padx=3, pady=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
multBtn.grid(row=2, column=3, padx=3, pady=3)

divBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
divBtn.grid(row=3, column=3, padx=3, pady=3)

clearBtn = Button(buttonFrame, text='<-', font=font, width=11, relief='ridge', activebackground='orange',
                  activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

AllClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='orange',
                     activeforeground='white', command=all_clear)
AllClearBtn.grid(row=4, column=2, columnspan=2, padx=3, pady=3)

# Binding all buttons
plusBtn.bind('<Button-1>', click_btn)
minusBtn.bind('<Button-1>', click_btn)
multBtn.bind('<Button-1>', click_btn)
divBtn.bind('<Button-1>', click_btn)
zeroBtn.bind('<Button-1>', click_btn)
dotBtn.bind('<Button-1>', click_btn)
equalBtn.bind('<Button-1>', click_btn)

# Scientific Mode adding

fontMenu = ('', 20)

scFrame = Frame(window)
sqrtBtn = Button(scFrame, text='√', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
sqrtBtn.grid(row=0, column=0, padx=3, pady=3)

powBtn = Button(scFrame, text='^', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
powBtn.grid(row=0, column=1, padx=3, pady=3)

factBtn = Button(scFrame, text='X!', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
factBtn.grid(row=0, column=2, padx=3, pady=3)

radBtn = Button(scFrame, text='toRad', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
radBtn.grid(row=0, column=3, padx=3, pady=3)

degBtn = Button(scFrame, text='toDeg', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
degBtn.grid(row=1, column=0, padx=3, pady=3)

sinBtn = Button(scFrame, text='sinØ', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
sinBtn.grid(row=1, column=1, padx=3, pady=3)

cosBtn = Button(scFrame, text='cosØ', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
cosBtn.grid(row=1, column=2, padx=3, pady=3)

tanBtn = Button(scFrame, text='tanØ', font=fontMenu, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
tanBtn.grid(row=1, column=3, padx=3, pady=3)
def enterClick(event):
        print('Hi')
        e=Event()
        e.widget=equalBtn
        click_btn(e)

textField.bind('<Return>',enterClick)

# functions

normalCalci = True


def calculate_sc(event):
    print("Clicked")
    btn = event.widget
    text = btn['text']
    print(text)
    answer = ""
    ex = textField.get()
    if (text == 'toDeg'):
        print('Calculate Degree')
        answer = str(m.degrees(float(ex)))
    elif (text == '^'):
        print("Calculate power")
        # answer = str(m.pow(float(ex)))
        base, pow = ex.split(',')
        print(base, pow)
        answer=m.pow(int(base),int(pow))
    elif (text == '√'):
        print("Calculate sqrt")
        answer = str(m.sqrt(float(ex)))
    elif (text == 'toRad'):
        print('calculate radian')
        answer = str(m.radians(float(ex)))
    elif (text == 'X!'):
        print("Calculate factorial")
        answer = str(m.factorial(int(ex)))
    elif (text == 'sinØ'):
        print("Calculate sinØ")
        answer = str(m.sin(m.radians(int(ex))))
    elif (text == 'cosØ'):
        answer = str(m.cos(m.radians(int(ex))))
    elif (text == 'tanØ'):
        print("Calculate tan")
        answer = str(m.tan(m.radians(int(ex))))
    textField.delete(0, END)
    textField.insert(0, answer)


def sc_click():
    global normalCalci
    print('clicked')
    if normalCalci:
        buttonFrame.pack_forget()
        scFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        window.geometry('430x650')

        print("show sc")
        normalCalci = False
    else:
        scFrame.pack_forget()
        window.geometry('430x523')
        print('show normal')
        normalCalci = True


menubar = Menu(window)
mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label='Scientific Calculator', command=sc_click)
menubar.add_cascade(label='Mode', menu=mode)
window.config(menu=menubar)

sqrtBtn.bind('<Button-1>', calculate_sc)
factBtn.bind('<Button-1>', calculate_sc)
powBtn.bind('<Button-1>', calculate_sc)
radBtn.bind('<Button-1>', calculate_sc)
degBtn.bind('<Button-1>', calculate_sc)
sinBtn.bind('<Button-1>', calculate_sc)
cosBtn.bind('<Button-1>', calculate_sc)
tanBtn.bind('<Button-1>', calculate_sc)

window.mainloop()
