import  tkinter

print('start')
win = tkinter.Tk()

canvas = tkinter.Canvas(win, bg='white', width=400, height=400)
canvas.create_line((100, 100), (100,150), fill='black')
canvas.create_line((300,300 ), (300,240), fill='black')
canvas.create_line((320, 320), (320,240), fill='black')
canvas.create_line((360, 100), (360,150), fill='black')
canvas.create_line((380, 100), (380,150), fill='black')
canvas.create_line((400, 100), (400,150), fill='black')
canvas.create_line((100, 100), (100,150), fill='black')
canvas.create_line((100, 100), (100,150), fill='black')
canvas.create_line((100, 100), (100,150), fill='black')
canvas.create_line((100, 100), (100,150), fill='black')


canvas.pack()

win.mainloop()