import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 50, 150, 150, fill="#ff0000")
canvas.create_text(100, 100, text="červený", fill="yellow", font="Arial 20")
canvas.create_rectangle(160, 50, 260, 150, fill="#0000ff")
canvas.create_text(210, 100, text="modrý", fill="yellow", font="Arial 20")

tkinter.mainloop()