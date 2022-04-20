
from math_lib import math_functions 
from tkinter import *
gui = Tk()
expression=""

def display_clear(): 
    global expression
    expression = ""
    calculator_text.set("")

def display_remove():
    global expression
    expression = expression[:-1]
    calculator_text.set(expression)

def display_text(item):
    global expression
    expression = expression + str(item)
    print(expression)
    calculator_text.set(expression)


#evaluates string from display
def evaluate():
        global expression
        character_array = []
        number = ""

        #parses expression into array
        for character in range(len(expression)):
            #checks if character is a number or .
            if (ord(expression[character]) >= 48 and ord(expression[character]) <= 57) or ord(expression[character]) == ord('.'):
                number = number + expression[character]
                #evaluates last number at the end of the expresion
                if (character == (len(expression)-1)):
                    number = float(number)
                    character_array.append(number)
                    number=""
            #when character is not a number
            elif ((ord(expression[character]) <= 48 or ord(expression[character]) >= 57) and ord(expression[character]) != ord('.')):
                if number != "":
                    #evaluates and appends number to array
                    number = float(number)
                    #appends operand to array
                    character_array.append(number)
                    character_array.append(expression[character])
                    number=""
                else:
                    character_array.append(expression[character])
            

            
        #calculates result
        result = character_array[0]

        #iters by 2
        for character in range(1,len(character_array),2):
            #creates a pair of operator and operad to use in basic math functions 
            operator = character_array[character]
            operand = character_array[character+1]

            if (operator == "+"):
                result = math_functions.plus(result,operand)
            elif (operator == "-"):
                result = math_functions.minus(result,operand)
            elif (operator == "/"):
                result = math_functions.divide(result,operand)
            if (operator == "*"):
                result = math_functions.multiply(result,operand)

        #displays result
        result = str(result)
        calculator_text.set(result)
        
    
#reads keyboard input  
def key(event):
    for k in range (10):
        if (event.char == str(k)):
            display_text(str(event.char))
    if (event.keysym == "l"):
        display_text("log(")
    elif (event.keysym == "p"):
        display_text("²")
    elif (event.keysym == "s"):
        display_text("√")
    
    elif event.keysym == "minus" or event.keysym == "plus" or event.keysym == "slash" or event.keysym == "asterisk"   or event.keysym == "parenleft" or event.keysym == "parenright" or event.keysym == "period":
        display_text(str(event.char))

    elif event.keysym == "Return":
        evaluate()
        print("eval")

    elif event.keysym == "BackSpace":
        display_remove()

    elif event.keysym == 'c':
        display_clear()

gui.configure(bg="#1A1D23")
gui.geometry("312x413")  
gui.resizable(0, 0)  
gui.title("Calculator")
gui.bind("<Key>",key)

calculator_text = StringVar()


input_frame = Frame(gui, width=312, bd=0)
input_frame.pack(side='top')


display = Entry(input_frame, font=('arial', 18), width=50, bg="#1A1D23", justify='right', fg='white', bd=0, textvariable=calculator_text)
display.grid(row=0, column=0)
display.pack(ipady=30) 



buttons_frame = Frame(gui, width=312, height=272.5, bg="#1A1D23")

#first row
parenLeft = Button(buttons_frame, text = "(", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("("))
parenLeft.grid(row = 0, column = 0, padx = 1, pady = 1)

parenRight = Button(buttons_frame, text = ")", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text(")"))
parenRight.grid(row = 0, column = 1, padx = 1, pady = 1)

clear = Button(buttons_frame, text = "CE", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_clear())
clear.grid(row = 0, column = 2, padx = 1, pady = 1)

remove = Button(buttons_frame, text = "<=|", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2",  command= lambda: display_remove())
remove.grid(row = 0, column = 3, padx = 1, pady = 1)



#second row
log = Button(buttons_frame, text = "log()", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("log"))
log.grid(row = 1, column = 0, padx = 1, pady = 1)

square = Button(buttons_frame, text = "x²", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("²"))
square.grid(row = 1, column = 2, padx = 1, pady = 1)

power = Button(buttons_frame, text = "√x", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("√"))
power.grid(row = 1, column = 1, padx = 1, pady = 1)

divide = Button(buttons_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2",  command= lambda: display_text("/"))
divide.grid(row = 1, column = 3, padx = 1, pady = 1)



#third row
seven = Button(buttons_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(7))
seven.grid(row = 2, column = 0, padx = 1, pady = 1)

eight = Button(buttons_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(8))
eight.grid(row = 2, column =1 , padx = 1, pady = 1)

nine = Button(buttons_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text(9))
nine.grid(row = 2, column = 2, padx = 1, pady = 1) 

multiply = Button(buttons_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("*"))
multiply.grid(row = 2, column = 3, padx = 1, pady = 1)



#fourth row
four = Button(buttons_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(4))
four.grid(row = 3, column = 0, padx = 1, pady = 1)

five = Button(buttons_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(5))
five.grid(row = 3, column = 1, padx = 1, pady = 1)

six = Button(buttons_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text(6))
six.grid(row = 3, column = 2, padx = 1, pady = 1)

minus = Button(buttons_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2",  command= lambda: display_text("-"))
minus.grid(row = 3, column = 3, padx = 1, pady = 1)



#fifth row
one = Button(buttons_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(1))
one.grid(row = 4, column = 0, padx = 1, pady = 1)

two = Button(buttons_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(2))
two.grid(row = 4, column = 1, padx = 1, pady = 1)

three = Button(buttons_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command = lambda: display_text(3))
three.grid(row = 4, column= 2, padx = 1 , pady=1 ) 

plus = Button(buttons_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command = lambda: display_text("+"))
plus.grid(row = 4, column= 3, padx = 1 , pady=1 )



#sixth row
shift = Button(buttons_frame, text = "shift", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: evaluate())
shift.grid(row = 5, column = 0, padx = 1, pady = 1)

zero = Button(buttons_frame, text = "0", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text(0))
zero.grid(row = 5, column = 1, padx = 1, pady = 1)

point = Button(buttons_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text("."))
point.grid(row = 5, column = 2, padx = 1, pady = 1) 

equals = Button(buttons_frame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: evaluate())
equals.grid(row = 5, column = 3, padx = 1, pady = 1)


buttons_frame.pack()
gui.mainloop()
