from tkinter import *
from PIL import ImageTk,Image
import os


def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter += 1

def rotate_img_prev():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter -= 1

counter = 1
root =Tk()
root.title('Wallpaper Viewer')

root.geometry('400x500')
root.configure(bg="black")

# Directory containing the images
image_dir = 'python-gui-tkinter-main/wallpapers'

# Get the list of files in the directory
files = os.listdir(image_dir)

# List to store the processed images
img_array = []
# Process each file in the directory
for file in files:
    img_path = os.path.join(image_dir, file)
    if os.path.isfile(img_path):  # Check if it is a file
        try:
            img = Image.open(img_path)
            resized_img = img.resize((300, 300))
            img_array.append(ImageTk.PhotoImage(resized_img))
        except Exception as e:
            print(f"Error processing {file}: {e}")

img_label = Label(root,image= img_array[0])
img_label.pack(pady=20)

nxt_btn = Button(root,text='Next', bg='white',fg='black',width=28,height=2, command=rotate_img)
nxt_btn.pack()

prev_btn = Button(root,text='Previous', bg='white',fg='black',width=28,height=2, command=rotate_img_prev)
prev_btn.pack(pady=(15,5))

root.mainloop()