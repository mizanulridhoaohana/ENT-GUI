
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\ENT Project\export\controller\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1133x744")
window.configure(bg = "#85C13D")


canvas = Canvas(
    window,
    bg = "#85C13D",
    height = 744,
    width = 1133,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1099.333251953125,
    22.33349609375,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1074.0,
    22.33056640625,
    image=image_image_2
)

canvas.create_text(
    21.0,
    13.0,
    anchor="nw",
    text="9:41",
    fill="#FFFFFF",
    font=("SFProText Semibold", 15 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    566.0,
    89.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=455.0,
    y=601.0,
    width=233.0,
    height=78.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    566.0,
    365.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    306.0,
    280.0,
    image=image_image_5
)

canvas.create_text(
    88.0,
    249.0,
    anchor="nw",
    text="Sprayer",
    fill="#404040",
    font=("Nunito Bold", 34 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=424.9998474121094,
    y=346.7379150390625,
    width=113.17479705810547,
    height=113.17479705810547
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    305.9998474121094,
    413.3253173828125,
    image=image_image_6
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=45.82501220703125,
    y=346.7379150390625,
    width=113.1748046875,
    height=113.1748046875
)

canvas.create_text(
    209.99984741210938,
    381.0001220703125,
    anchor="nw",
    text="0",
    fill="#404040",
    font=("Nunito Bold", 30 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    860.1749877929688,
    280.0,
    image=image_image_7
)

canvas.create_text(
    642.1749877929688,
    249.0,
    anchor="nw",
    text="Vacuum",
    fill="#404040",
    font=("Nunito Bold", 34 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=971.1748046875,
    y=346.7379150390625,
    width=113.17479705810547,
    height=113.17479705810547
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    860.1748046875,
    413.3253173828125,
    image=image_image_8
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=600.0,
    y=346.7379150390625,
    width=113.1748046875,
    height=113.1748046875
)

canvas.create_text(
    764.1748046875,
    381.0001220703125,
    anchor="nw",
    text="0",
    fill="#404040",
    font=("Nunito Bold", 30 * -1)
)
window.resizable(False, False)
window.mainloop()
