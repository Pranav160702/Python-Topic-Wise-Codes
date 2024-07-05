from tkinter import *
from PIL import ImageTk,Image   #This is use to insert image in the window
from tkinter import messagebox


def handle_login():
    # print("Login button clicked")
    email = email_input.get()
    password = password_input.get()
    if email == 'jadhavpranav595@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successfully')
    else:
        messagebox.showerror('Error','Invalid Email or Password')
        

root = Tk() # Created object of 'Tk' class which iside the tkinter 

# Set title  
root.title("Login Form")

root.iconbitmap('python-gui-tkinter-main/favicon.ico')

# # Set min. size of the window
# root.minsize(200,200)

# # Set max. size of the window
# root.minsize(600,600)

# To set customized window size
root.geometry("400x600")

root.configure(background="#0096DC") #Set backgroung color to '#0096DC'

# Insert image
img = Image.open('python-gui-tkinter-main/flipkart-logo.png')
resized_img = img.resize((70,70))
fp_image = ImageTk.PhotoImage(resized_img)

img_lable = Label(root, image = fp_image)
img_lable.pack(pady = (15,10))


# Insert Text  
txt_lable = Label(root, text = 'Flipkart',fg = 'white',bg = '#0096DC')
txt_lable.pack(pady = (15,10))
txt_lable.configure(font=('verdana', 24))

# Taking Input from GUI

email_label = Label(root, text = 'Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady = (15,5))
email_label.configure(font=('verdana', 12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(2,15))


password_label = Label(root, text = 'Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady = (15,5))
password_label.configure(font=('verdana', 12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(2,15))

# Login Button
login_button = Button(root, text="Login Here", bg='white',fg='black',width='20', height='2', command=handle_login)
login_button.pack(pady=(15,10))
login_button.configure(font=('verdana',10))





root.mainloop() # Mainloop keep our GUI consistent on the screen
