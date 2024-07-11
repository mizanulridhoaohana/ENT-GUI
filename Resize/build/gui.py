
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/media/mizanul/Local Disk/ENT Project/ENT-GUI/Resize/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("940x709")
window.configure(bg = "#85C13D")


canvas = Canvas(
    window,
    bg = "#85C13D",
    height = 709,
    width = 940,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    x=47.0,
    y=251.0,
    width=366.0,
    height=261.0
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
    x=437.0,
    y=251.0,
    width=215.0,
    height=261.0
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
    x=676.0,
    y=251.0,
    width=221.0,
    height=124.0
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
    x=676.0,
    y=389.0,
    width=221.0,
    height=123.0
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
    x=229.0,
    y=558.0,
    width=225.0,
    height=81.0
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
    x=491.0,
    y=558.0,
    width=225.0,
    height=81.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    469.0,
    89.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    912.9375,
    21.5283203125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    892.052734375,
    21.5255126953125,
    image=image_image_3
)

canvas.create_text(
    17.4384765625,
    8.0,
    anchor="nw",
    text="9:41",
    fill="#FFFFFF",
    font=("SFProText Semibold", 15 * -1)
)

canvas.create_text(
    130.0,
    158.5,
    anchor="nw",
    text="RS. Universitas Mataram",
    fill="#FFFFFF",
    font=("Nunito Black", 14 * -1)
)

canvas.create_text(
    130.0,
    185.5,
    anchor="nw",
    text="Unit THT",
    fill="#F1F1F1",
    font=("Nunito SemiBold", 12 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    89.0,
    180.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
