from tkinter import *

first_num = second_num = operator = expression = None

# Get Digit Function
def get_digit(digit):
    current = res_label['text']
    new = current + str(digit)
    res_label.config(text=new)

# Clear Screen Function
def clear():
    res_label.config(text="")
    exp_label.config(text="")

# Get Operator Function
def get_operator(op):
    global first_num, operator, expression
    first_num = int(res_label['text'])
    operator = op
    expression = str(first_num) + operator
    res_label.config(text="")
    exp_label.config(text = expression)

# Result Calculation fuction
def get_result():
    global first_num, second_num, operator, expression

    second_num = int(res_label['text'])

    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    else:
        if(second_num == 0):
            result = "Error"
        else:
            result = first_num / second_num


    expression = expression + str(second_num) + '='
    res_label.config(text=result)
    exp_label.config(text=expression)


root = Tk()
root.title("Calculator")
root.iconbitmap('python-gui-tkinter-main/calculator.ico')
root.geometry("279x360")
root.resizable(0,0)
root.configure(background='black')


# Row 0
# Display Expression
exp_label = Label(root,text='',bg='black',fg='white')
exp_label.grid(row=0,column=0,columnspan=10,sticky='W')
exp_label.config(font=('verdana',30))


# Row 1
# Display Result
res_label = Label(root,text='',bg='black',fg='white')
res_label.grid(row=1,column=0,columnspan=10,sticky='W')
res_label.config(font=('verdana',30))


# Row 2
# Button 7
btn7 = Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(7))
btn7.grid(row=2,column=0)
btn7.config(font=('verdana',14))

# Button 8
btn8 = Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(8))
btn8.grid(row=2,column=1)
btn8.config(font=('verdana',14))

# Button 9
btn9 = Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(9))
btn9.grid(row=2,column=2)
btn9.config(font=('verdana',14))

# Button Division
btn_div = Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2, command = lambda : get_operator('/'))
btn_div.grid(row=2,column=3)
btn_div.config(font=('verdana',14))


# Row3
# Button 4
btn4 = Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(4))
btn4.grid(row=3,column=0)
btn4.config(font=('verdana',14))

# Button 5
btn5 = Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(5))
btn5.grid(row=3,column=1)
btn5.config(font=('verdana',14))

# Button 6
btn6 = Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(6))
btn6.grid(row=3,column=2)
btn6.config(font=('verdana',14))

# Button Multiplication
btn_mul = Button(root,text='x',bg='#00a65a',fg='white',width=5,height=2, command = lambda : get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))


# Row 4
# Button 1
btn1 = Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(1))
btn1.grid(row=4,column=0)
btn1.config(font=('verdana',14))

# Button 2
btn2 = Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(2))
btn2.grid(row=4,column=1)
btn2.config(font=('verdana',14))

# Button 3
btn3 = Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(3))
btn3.grid(row=4,column=2)
btn3.config(font=('verdana',14))

# Button Subtraction
btn_sub = Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2, command = lambda : get_operator('-'))
btn_sub.grid(row=4,column=3)
btn_sub.config(font=('verdana',14))


# Row 5
# Button Clear
btn_clr = Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2, command = lambda: clear())
btn_clr.grid(row=5,column=0)
btn_clr.config(font=('verdana',14))

# Button 0
btn0 = Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2, command = lambda :get_digit(0))
btn0.grid(row=5,column=1)
btn0.config(font=('verdana',14))

# Button Equals
btn_eql = Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2, command = lambda: get_result())
btn_eql.grid(row=5,column=2)
btn_eql.config(font=('verdana',14))

# Button Addition
btn_add = Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2, command = lambda : get_operator('+'))
btn_add.grid(row=5,column=3 )
btn_add.config(font=('verdana',14))

root.mainloop()