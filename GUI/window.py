from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1350x720")
window.configure(bg = "#ffc19a")
canvas = Canvas(
    window,
    bg = "#ffc19a",
    height = 720,
    width = 1350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    153.0, -31.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    -269.5, -180.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e5cdcb",
    highlightthickness = 0)

entry0.place(
    x = -289.0, y = -194,
    width = 39.0,
    height = 26)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    154.5, -131.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e5cdcb",
    highlightthickness = 0)

entry1.place(
    x = 135.0, y = -145,
    width = 39.0,
    height = 26)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    581.5, -123.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e5cdcb",
    highlightthickness = 0)

entry2.place(
    x = 562.0, y = -137,
    width = 39.0,
    height = 26)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 636, y = -252,
    width = 125,
    height = 50)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 666, y = -137,
    width = 66,
    height = 33)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 696, y = -175,
    width = 56,
    height = 28)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 239, y = -150,
    width = 66,
    height = 33)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 269, y = -187,
    width = 56,
    height = 28)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 269, y = -225,
    width = 56,
    height = 28)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = -185, y = -199,
    width = 66,
    height = 33)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = -155, y = -236,
    width = 56,
    height = 28)

img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = -155, y = -274,
    width = 56,
    height = 28)

img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 309, y = 240,
    width = 25,
    height = 25)

img10 = PhotoImage(file = f"img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 309, y = 184,
    width = 25,
    height = 25)

img11 = PhotoImage(file = f"img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b11.place(
    x = 309, y = 212,
    width = 25,
    height = 25)

img12 = PhotoImage(file = f"img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b12.place(
    x = 309, y = 156,
    width = 25,
    height = 25)

img13 = PhotoImage(file = f"img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b13.place(
    x = 309, y = 128,
    width = 25,
    height = 25)

window.resizable(False, False)
window.mainloop()
