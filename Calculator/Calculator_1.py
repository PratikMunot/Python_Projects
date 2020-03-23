from tkinter import *
from tkinter import ttk
# # frame is used to group all the weidgets - it acts as container
# class Application(Frame):
#     def __init__(self,master):
#         #
#         super(Application,self).__init__(master)
#         self.task = ""
#         self.UserIn = StringVar()
#         self.grid()
#         self.create_widgets()

class Calculator:
    calc_value = 0.0

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self,value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0,"end")
        self.number_entry.insert(0,entry_val)
    def AC_button_press(self):
        self.number_entry.delete(0, "end")

    def isfloat(self,str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self,value):
        if self.isfloat(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.calc_value = float(self.entry_value.get())

        if value == '/':
            print("/ Pressed")
            self.div_trigger = True
        elif value == '*':
            print("* Pressed")
            self.mult_trigger = True
        elif value == '+':
            print("+ Pressed")
            self.add_trigger = True
        elif value == '-':
            print("- Pressed")
            self.sub_trigger = True

        self.number_entry.delete(0,"end")

    def equal_button_press(self):
        if self.add_trigger or self.mult_trigger or self.sub_trigger or self.div_trigger :
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            elif self.div_trigger:
                solution = self.calc_value / float(self.entry_value.get())

            print(self.calc_value," ",float(self.entry_value.get())," ",solution)

            self.number_entry.delete(0,"end")
            self.number_entry.insert(0, round(solution,5))

    def __init__(self,root):
        self.entry_value = StringVar(root,value="")
        root.title("Pratik_Munot Calculator")
        root.geometry("285x245")
        root.resizable(width=False,height=False)

        style = ttk.Style()
        style.configure("TButton",font="Times 15 bold",padx=10)#,padx=5,pady=5)
        style.configure("TEntry", font="Times 15 bold",padding=5)#, padding=5)

        self.number_entry = ttk.Entry(root,font="20",textvariable=self.entry_value,width=30)
        self.number_entry.grid(row=0,columnspan=4)

        self.button7 = ttk.Button(root,width=5,text="7",command = lambda :self.button_press('7')).grid(row=1,column=0,padx=5,pady=5)
        self.button8 = ttk.Button(root,width=5, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1,padx=5,pady=5)
        self.button9 = ttk.Button(root,width=5, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2,padx=5,pady=5)
        self.button_div = ttk.Button(root,width=5, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3,padx=5,pady=5)

        self.button4 = ttk.Button(root,width=5, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0, padx=5,pady=5)
        self.button5 = ttk.Button(root,width=5, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1, padx=5,pady=5)
        self.button6 = ttk.Button(root,width=5, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2, padx=5,pady=5)
        self.button_mult = ttk.Button(root,width=5, text="*", command=lambda: self.math_button_press('*')).grid(row=2,column=3,padx=5, pady=5)

        self.button1 = ttk.Button(root,width=5, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0, padx=5,pady=5)
        self.button2 = ttk.Button(root,width=5, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1, padx=5,pady=5)
        self.button3 = ttk.Button(root,width=5, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2, padx=5,pady=5)
        self.button_add = ttk.Button(root,width=5, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3,padx=5, pady=5)

        self.button_dot = ttk.Button(root,width=5, text=".", command=lambda: self.button_press('.')).grid(row=4, column=0, padx=5,pady=5)
        self.button0 = ttk.Button(root,width=5, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1, padx=5,pady=5)
        self.button_equal = ttk.Button(root,width=5, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2, padx=5,pady=5)
        self.button_sub = ttk.Button(root,width=5, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3, padx=5, pady=5)

        self.button_clear = ttk.Button(root, width=12, text="AC", command=lambda: self.AC_button_press()).grid(row=5,column=0,columnspan=2,padx=5,pady=5)
        self.button_equal = ttk.Button(root,width=12, text="=", command=lambda: self.equal_button_press()).grid(row=5, column=2,columnspan=2, padx=5,pady=5)

root = Tk()
c = Calculator(root)
root.mainloop()


