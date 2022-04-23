
from math_lib import math_functions 
from tkinter import *
from idlelib.tooltip import Hovertip
gui = Tk()
expression=""
expression_eval=""

def display_clear(): 
    global expression
    global expression_eval
    expression = ""
    expression_eval = ""
    calculator_text.set("")

def display_remove():
    global expression
    global expression_char
    expression = expression[:-1]
    expression_eval = expression_eval[:-1]
    calculator_text.set(expression)

def display_text(item):
    global expression
    global expression_eval
    item = str(item)
    expression = expression + item
    expression_eval = expression_eval + item[0]
    calculator_text.set(expression)


#evaluates string from display
def evaluate():
        global expression_eval
        character_array = []
        number = ""

        #parses expression into array
        for character in range(len(expression_eval)):
            #checks if character is a number or .
            if (ord(expression_eval[character]) >= 48 and ord(expression_eval[character]) <= 57) or ord(expression_eval[character]) == ord('.'):
                number = number + expression_eval[character]
                #evaluates last number at the end of the expression
                if (character == (len(expression_eval)-1)):
                    number = float(number)
                    character_array.append(number)
                    number=""
            #when character is not a number
            elif ((ord(expression_eval[character]) <= 48 or ord(expression_eval[character]) >= 57) and ord(expression_eval[character]) != ord('.')):
                if number != "":
                    #evaluates and appends number to array
                    number = float(number)
                    #appends operand to array
                    character_array.append(number)
                    character_array.append(expression_eval[character])
                    number=""
                else:
                    character_array.append(expression_eval[character])
            

        """
        TO DO <xblask05>
        function to calculate the expression
        1. for loop going through expression array
            -searching for operators with higher precedence (*,/,log,sqrt,^,!)
            -evaluating said expressions 
            -replacing expression with result and deleting the rest of operator arguments
        
        2. for loop for basic operations
            -after all prioritised operations are done, another for loop will be used to evaluate
             the result of the expression now contaning only the basic operations (+,-)

        """


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
        display_text("^")
    elif (event.keysym == "s"):
        display_text("sqrt(")

    elif event.keysym == 'f':
         display_text("!")
    
    elif event.keysym == "minus" or event.keysym == "plus" or event.keysym == "slash" or event.keysym == "asterisk"   or event.keysym == "parenleft" or event.keysym == "parenright" or event.keysym == "period":
        display_text(str(event.char))

    elif event.keysym == "Return":
        evaluate()

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
log = Button(buttons_frame, text = "log()", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("log("))
log.grid(row = 0, column = 0, padx = 1, pady = 1)
log_tip = Hovertip(log,'This button enters a natural logarithm function, fill and close the parenthesis with a number to get its natural logarithm')

square = Button(buttons_frame, text = "x^", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("^"))
square.grid(row = 0, column = 2, padx = 1, pady = 1)
square_tip = Hovertip(square,'This button enters an exponentiation sign, use this to create an exponentiation expression')

sqrt = Button(buttons_frame, text = "sqrt()", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("sqrt("))
sqrt.grid(row = 0, column = 1, padx = 1, pady = 1)
sqrt = Hovertip(sqrt,'This button enters a square root function, fill and close the parenthesis with a number to get its square root')

factorial = Button(buttons_frame, text = "x!", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2",  command= lambda: display_text("!"))
factorial.grid(row = 0, column = 3, padx = 1, pady = 1)
factorial_tip = Hovertip(factorial,'This button enters a factorial sign, enter this after a number to get its factorial')

#second row
parenLeft = Button(buttons_frame, text = "(", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("("))
parenLeft.grid(row = 1, column = 0, padx = 1, pady = 1)
parenLeft_tip = Hovertip(parenLeft,'This button enters an opening parenthesis, use this with a closing parenthesis to create a sub-expression')

parenRight = Button(buttons_frame, text = ")", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text(")"))
parenRight.grid(row = 1, column = 1, padx = 1, pady = 1)
parenRight_tip = Hovertip(parenRight,'This button enters a closing parenthesis, use this with an opening parenthesis to create a sub-expression')

clear = Button(buttons_frame, text = "CE", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_clear())
clear.grid(row = 1, column = 2, padx = 1, pady = 1)
clear_tip = Hovertip(clear,'This button clears all entered expressions')

divide = Button(buttons_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2",  command= lambda: display_text("/"))
divide.grid(row = 1, column = 3, padx = 1, pady = 1)
divide_tip = Hovertip(divide,'This button enters a division sign, use this to create a division expression')




#third row
seven = Button(buttons_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(7))
seven.grid(row = 2, column = 0, padx = 1, pady = 1)
seven_tip = Hovertip(seven,'This button enters the digit 7, use this in combination with other digits to create numbers')

eight = Button(buttons_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(8))
eight.grid(row = 2, column =1 , padx = 1, pady = 1)
eight = Hovertip(eight,'This button enters the digit 8, use this in combination with other digits to create numbers')

nine = Button(buttons_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text(9))
nine.grid(row = 2, column = 2, padx = 1, pady = 1) 
nine_tip = Hovertip(nine,'This button enters the digit 9, use this in combination with other digits to create numbers')

multiply = Button(buttons_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: display_text("*"))
multiply.grid(row = 2, column = 3, padx = 1, pady = 1)
multiply_tip = Hovertip(multiply,'This button enters a multiplication sign, use this to create a multiplication expression')



#fourth row
four = Button(buttons_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(4))
four.grid(row = 3, column = 0, padx = 1, pady = 1)
four = Hovertip(four,'This button enters the digit 4, use this in combination with other digits to create numbers')

five = Button(buttons_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(5))
five.grid(row = 3, column = 1, padx = 1, pady = 1)
five_tip = Hovertip(five,'This button enters the digit 5, use this in combination with other digits to create numbers')

six = Button(buttons_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text(6))
six.grid(row = 3, column = 2, padx = 1, pady = 1)
six = Hovertip(six,'This button enters the digit 6, use this in combination with other digits to create numbers')

minus = Button(buttons_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2",  command= lambda: display_text("-"))
minus.grid(row = 3, column = 3, padx = 1, pady = 1)
minus_tip = Hovertip(minus,'This button enters a minus sign, use this to create a subtraction expression')



#fifth row
one = Button(buttons_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(1))
one.grid(row = 4, column = 0, padx = 1, pady = 1)
one_tip = Hovertip(one,'This button enters the digit 1, use this in combination with other digits to create numbers')

two = Button(buttons_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command= lambda: display_text(2))
two.grid(row = 4, column = 1, padx = 1, pady = 1)
two_tip = Hovertip(two,'This button enters the digit 2, use this in combination with other digits to create numbers')

three = Button(buttons_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2", command = lambda: display_text(3))
three.grid(row = 4, column= 2, padx = 1 , pady=1 ) 
three_tip = Hovertip(three,'This button enters the digit 3, use this in combination with other digits to create numbers')

plus = Button(buttons_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command = lambda: display_text("+"))
plus.grid(row = 4, column= 3, padx = 1 , pady=1 )
plus_tip = Hovertip(plus,'This button enters a plus sign, use this to create an addition expression')



#sixth row
shift = Button(buttons_frame, text = "shift", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: evaluate())
shift.grid(row = 5, column = 0, padx = 1, pady = 1)

zero = Button(buttons_frame, text = "0", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text(0))
zero.grid(row = 5, column = 1, padx = 1, pady = 1)
zero_tip = Hovertip(zero,'This button enters the digit 0, use this in combination with other digits to create numbers')

point = Button(buttons_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "#111317", cursor = "hand2",  command= lambda: display_text("."))
point.grid(row = 5, column = 2, padx = 1, pady = 1) 
point_tip = Hovertip(point,'This button enters a floating point, use this in combination with digits to create floating point numbers')

equals = Button(buttons_frame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "#5D70FD", cursor = "hand2", command= lambda: evaluate())
equals.grid(row = 5, column = 3, padx = 1, pady = 1)
equals_tip = Hovertip(equals,'This button evaluates your expression')


buttons_frame.pack()
gui.mainloop()
