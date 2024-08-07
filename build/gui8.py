
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\ENT Project\export\build\assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1512x982")
window.configure(bg = "#DFEBD0")


canvas = Canvas(
    window,
    bg = "#DFEBD0",
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
    618.0,
    487.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1245.0,
    690.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1245.0,
    257.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    84.0,
    491.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    78.0,
    176.0,
    image=image_image_5
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
    x=62.0,
    y=236.0,
    width=34.0,
    height=34.0
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
    x=62.0,
    y=159.0,
    width=35.0,
    height=35.0
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
    x=61.0,
    y=806.0,
    width=35.0,
    height=35.0
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
    x=64.0,
    y=68.0,
    width=28.0,
    height=28.0
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
    x=64.0,
    y=884.0,
    width=28.0,
    height=28.0
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
    x=60.0,
    y=309.0,
    width=38.0,
    height=38.0
)

canvas.create_rectangle(
    46.0,
    120.0,
    113.0,
    120.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    46.0,
    860.0,
    113.0,
    860.0,
    fill="#FFFFFF",
    outline="")

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=61.0,
    y=745.0,
    width=35.0,
    height=35.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    605.0,
    486.5,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    944.0,
    829.0,
    image=image_image_7
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=928.0,
    y=813.0,
    width=31.0,
    height=31.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=1092.5,
    y=848.5,
    width=136.0,
    height=42.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=1236.5,
    y=848.5,
    width=136.0,
    height=42.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1245.5,
    800.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1092.0,
    y=777.0,
    width=307.0,
    height=45.0
)

canvas.create_text(
    1082.0,
    743.0,
    anchor="nw",
    text="Alasan",
    fill="#404040",
    font=("Nunito Bold", 19 * -1)
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=1082.0,
    y=679.0,
    width=326.0,
    height=32.0
)

canvas.create_text(
    1082.0,
    644.0,
    anchor="nw",
    text="Label Baru",
    fill="#404040",
    font=("Nunito Bold", 19 * -1)
)

canvas.create_text(
    1082.0,
    540.0,
    anchor="nw",
    text="Untuk mengoreksi hasil diagnosa sebelumnya, mohon untuk memilih label berikut yang dinilai sesuai dengan penyakit yang diderita pasien dan sertakan alasan yang jelas.",
    fill="#14181F",
    font=("Nunito Regular", 14 * -1)
)

canvas.create_text(
    1082.0,
    492.0,
    anchor="nw",
    text="Koreksi Hasil",
    fill="#404040",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    1082.0,
    92.0,
    anchor="nw",
    text="Analisa Gambar:",
    fill="#404040",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    1357.0,
    399.5,
    anchor="nw",
    text="OMA Perforasi",
    fill="#404040",
    font=("Nunito Regular", 12 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1335.0,
    411.0,
    image=image_image_8
)

canvas.create_text(
    1237.0,
    399.5,
    anchor="nw",
    text="OMA Perforasi",
    fill="#404040",
    font=("Nunito Regular", 12 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1215.0,
    411.0,
    image=image_image_9
)

canvas.create_text(
    1118.0,
    399.5,
    anchor="nw",
    text="OMA Perforasi",
    fill="#404040",
    font=("Nunito Regular", 12 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1096.0,
    411.0,
    image=image_image_10
)

canvas.create_text(
    1082.0,
    365.0,
    anchor="nw",
    text="Keterangan grafik:",
    fill="#404040",
    font=("Nunito Regular", 14 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1245.5,
    240.0,
    image=image_image_11
)
window.resizable(False, False)
window.mainloop()
