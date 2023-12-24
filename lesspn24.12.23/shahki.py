import tkinter
win = tkinter.Tk()

canvas = tkinter.Canvas(win,bg = '#fff', width=400 , height=400 )
canvas.pack()
for i in range(1,8):
    canvas.create_line((i * 50,0),(i * 50,400),fill='black')
for i in range(1,8):
    canvas.create_line((0, i * 50),(400, i * 50),fill='black')
win.mainloop()