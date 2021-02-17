import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def vypis_subor(meno_suboru):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    riadok = subor.readline()
    medzera = 0
    while riadok != "":
        medzera += 18
        canvas.create_text(50, medzera, text=riadok, anchor="nw", font=("arial", 12))
        riadok = subor.readline()


vypis_subor("subory/text3.txt")

canvas.mainloop()