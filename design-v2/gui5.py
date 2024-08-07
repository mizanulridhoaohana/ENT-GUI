
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\ENT Project\export\v2\build\assets\frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1512x982")
window.configure(bg = "#85C13D")


canvas = Canvas(
    window,
    bg = "#85C13D",
    height = 982,
    width = 1512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    101.0,
    192.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1434.1650390625,
    32.8797607421875,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1389.6668701171875,
    31.87451171875,
    image=image_image_3
)

canvas.create_text(
    28.024658203125,
    18.2392578125,
    anchor="nw",
    text="9:41",
    fill="#FFFFFF",
    font=("Nunito Bold", 19 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    747.0,
    100.0,
    image=image_image_4
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
    x=64.0,
    y=291.0,
    width=576.0,
    height=436.0
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
    x=682.0,
    y=291.0,
    width=362.0,
    height=434.0
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
    x=1086.0,
    y=293.0,
    width=367.0,
    height=205.0
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
    x=1086.0,
    y=522.0,
    width=367.0,
    height=205.0
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
    x=776.0,
    y=798.0,
    width=326.0,
    height=118.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=393.0,
    y=798.0,
    width=328.0,
    height=118.0
)

canvas.create_text(
    155.0,
    199.0,
    anchor="nw",
    text="Unit THT",
    fill="#F1F1F1",
    font=("Nunito SemiBold", 17 * -1)
)

canvas.create_text(
    155.0,
    163.0,
    anchor="nw",
    text="RS. Universitas Mataram",
    fill="#FFFFFF",
    font=("Nunito Black", 21 * -1)
)
window.resizable(False, False)
window.mainloop()
