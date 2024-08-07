
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\ENT Project\export\controller\build\assets\frame5")


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
    361.0,
    233.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    361.0,
    232.5,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    623.0,
    356.0,
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
    x=607.0,
    y=340.0,
    width=31.0,
    height=31.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    895.0,
    233.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    895.5,
    215.0,
    image=image_image_5
)

canvas.create_text(
    726.0,
    324.0,
    anchor="nw",
    text="Keterangan grafik:",
    fill="#404040",
    font=("Nunito Regular", 14 * -1)
)

canvas.create_text(
    726.0,
    75.0,
    anchor="nw",
    text="Analisa Gambar:",
    fill="#404040",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    1018.0,
    366.5,
    anchor="nw",
    text="OMA Perforasi",
    fill="#404040",
    font=("Nunito Regular", 12 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    996.0,
    378.0,
    image=image_image_6
)

canvas.create_text(
    886.0,
    366.5,
    anchor="nw",
    text="OMA Perforasi",
    fill="#404040",
    font=("Nunito Regular", 12 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    864.0,
    378.0,
    image=image_image_7
)

canvas.create_text(
    754.0,
    366.5,
    anchor="nw",
    text="OMA Perforasi",
    fill="#404040",
    font=("Nunito Regular", 12 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    732.0,
    378.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    351.0,
    568.0,
    image=image_image_9
)

canvas.create_text(
    67.0,
    459.0,
    anchor="nw",
    text="Hasil Diagnosa",
    fill="#404040",
    font=("Nunito Bold", 19 * -1)
)

canvas.create_text(
    67.0,
    507.0,
    anchor="nw",
    text="OMA PERFORASI",
    fill="#1E5C2A",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    67.0,
    547.0,
    anchor="nw",
    text="Tingkat keyakinan dignosa: 65%",
    fill="#404040",
    font=("Nunito Regular", 14 * -1)
)

canvas.create_text(
    67.0,
    583.0,
    anchor="nw",
    text="Note: Jika hasil diagnosa dirasa keliru, silakan untuk melakukan koreksi hasil.",
    fill="#151920",
    font=("Nunito Bold", 12 * -1)
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
    x=67.0,
    y=623.0,
    width=192.0,
    height=54.0
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
    x=267.0,
    y=623.0,
    width=192.0,
    height=54.0
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    895.0,
    570.0,
    image=image_image_10
)

canvas.create_text(
    726.0,
    459.0,
    anchor="nw",
    text="Informasi Pasien",
    fill="#404040",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    726.0,
    509.0,
    anchor="nw",
    text="Alma Liakua Mutia",
    fill="#404040",
    font=("Nunito Bold", 20 * -1)
)

canvas.create_text(
    726.0,
    543.0,
    anchor="nw",
    text="No Asuransi     : ",
    fill="#404040",
    font=("Nunito Regular", 15 * -1)
)

canvas.create_text(
    839.0,
    543.0,
    anchor="nw",
    text="000863002321023",
    fill="#404040",
    font=("Nunito Bold", 15 * -1)
)

canvas.create_text(
    726.0,
    567.0,
    anchor="nw",
    text="Jenis Asuransi  : ",
    fill="#404040",
    font=("Nunito Regular", 15 * -1)
)

canvas.create_text(
    838.0,
    567.0,
    anchor="nw",
    text="BPJS",
    fill="#404040",
    font=("Nunito Bold", 15 * -1)
)

canvas.create_text(
    726.0,
    591.0,
    anchor="nw",
    text="Kelas Asuransi : ",
    fill="#404040",
    font=("Nunito Regular", 15 * -1)
)

canvas.create_text(
    838.0,
    591.0,
    anchor="nw",
    text="Kelas 1",
    fill="#404040",
    font=("Nunito Bold", 15 * -1)
)

canvas.create_text(
    726.0,
    615.0,
    anchor="nw",
    text="Fasilitas Kesehatan : ",
    fill="#404040",
    font=("Nunito Regular", 15 * -1)
)

canvas.create_text(
    865.0,
    615.0,
    anchor="nw",
    text="Puskesmas Selaparang",
    fill="#404040",
    font=("Nunito Bold", 15 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1099.333251953125,
    22.33349609375,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1074.0,
    22.33056640625,
    image=image_image_12
)

canvas.create_text(
    21.0,
    13.0,
    anchor="nw",
    text="9:41",
    fill="#FFFFFF",
    font=("SFProText Semibold", 15 * -1)
)
window.resizable(False, False)
window.mainloop()
