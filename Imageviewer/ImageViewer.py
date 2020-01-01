from tkinter import *
from PIL import ImageTk, Image
from _ast import Lambda

window = Tk()
window.geometry("1500x800")

my_image1 = ImageTk.PhotoImage(Image.open("Image1.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("Image2.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("Image3.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("Image4.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("Image5.jpg"))

my_list = [my_image1, my_image2, my_image3, my_image4, my_image5]
count = 1
label_ref = Label(text="Image " + str(count) + " of " + str(len(my_list))).grid(row=6, column=3)

label = Label(image=my_image1).grid(row=0, column=2, columnspan=4, rowspan=5)
label_space1 = Label(text="      ").grid(row=2, column=1)
label_space2 = Label(text="      ").grid(row=2, column=6)


def forward(image_number):
    global label
    global image_num
    global button_forward
    global label_ref
    global count
    if image_number == 4:
        button_forward = Button(window, text=">>", state=DISABLED)
    else:
        label = Label(image=my_list[image_number+1])
        label.grid(row=0, column=2, columnspan=4, rowspan=5)
        count += 1
        label_ref = Label(text="Image " + str(count) + " of " + str(len(my_list))).grid(row=6, column=3)
        image_num += 1


def back(image_number):
    global label
    global image_num
    global label_ref
    global button_back
    global count
    if image_number == 0:
        button_back = Button(window, text=">>", state=DISABLED)
    else:
        label = Label(image=my_list[image_number - 1])
        label.grid(row=0, column=2, columnspan=4, rowspan=5)
        count -= 1
        label_ref = Label(text="Image " + str(count) + " of " + str(len(my_list))).grid(row=6, column=3)
        image_num -= 1


image_num = 0
button_forward = Button(window, text=">>", command=lambda: forward(image_num)).grid(row=2, column=7)
button_exit = Button(window, text="Exit", command=window.quit).grid(row=5, column=1)
button_back = Button(window, text="<<", command=lambda: back(image_num)).grid(row=2, column=0)

window.mainloop()