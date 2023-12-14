from tkinter import*
root = Tk()
root.title("Calculator")
r = 1
c = 0
counter = 1



class Custom_button:
    def __init__ (self,name,row_num,col_num):
        self.name = name
        self.row_num = row_num
        self.col_num = col_num

    def draw_button(self):
        if self.name == "C" or self.name == "⌫":
            button = Button(root, text = self.name, command = self.button_clicked, width = 12, height = 2)
            button.grid(row = self.row_num, column = self.col_num, columnspan = 2)           
        else:
            button = Button(root, text = self.name, command = self.button_clicked, width = 5, height = 2)
            button.grid(row = self.row_num, column = self.col_num)

    def button_clicked(self):
        print(self.name)
        eq = entry.get()
        if self.name == "=":
            entry.delete(0,END)
            entry.insert(END,eval(eq))
        elif self.name == "C":
            entry.delete(0,END)
        elif self.name == "⌫":
            entry.delete(len(eq) - 1,END)
        else:
            entry.insert(END,self.name)


entry = Entry(root, width = 13, font="lucida 20 bold")
entry.grid(row = 0, column = 0, columnspan = 4)
calc = Custom_button("C",5,2)
calc.draw_button()
back = Custom_button("⌫",5,0)
back.draw_button()

for a in range(1,4,1):
    for b in range(1,4,1):
        digits = Custom_button(counter, r, c)
        digits.draw_button()
        c += 1
        counter += 1
    c = 0
    r += 1

other_buttons = [
Custom_button("+",1,3),
Custom_button("-",2,3),
Custom_button("*",3,3),
Custom_button(".",4,0),
Custom_button(0,4,1),
Custom_button("=",4,2),
Custom_button("/",4,3),

]

for n in other_buttons:
    n.draw_button()
        
    

root.mainloop()
