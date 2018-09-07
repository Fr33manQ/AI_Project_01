# /*
#  * @Author: CoreyQiu 
#  * @Date: 2018-09-07 19:21:03 
#  * @Last Modified by:   CoreyQiu 
#  * @Last Modified time: 2018-09-07 19:21:03 
#  */


import tkinter as tk
from tkinter import messagebox


def init_canvas():
    root = tk.Tk()
    board = tk.Canvas(root, width=620-40, height=620-40,bg='#dacfa0') # 15 * 15 的棋盘  15 * 40 = 600  + 两端的空白 - 多出的一行
    menu_container =tk.Canvas(root,width=580,height=10) # Menu

    for i in range(15):
        board.create_line(10, 10+i*40, 610-40, 10+i*40)
    for i in range(15):
        board.create_line(10+i*40, 10, 10+i*40, 610-40)
    for i in range(3,12,8):
        board.create_oval(i*40+10-3, 127, i*40+10+3, 133, fill='black')
        board.create_oval(i*40+10-3, 127+320, i*40+10+3, 133+320, fill='black')
    board.create_oval(287,287,293,293,fill='black')

    give_up = tk.Button(root,width=10,height=2,text='投降',command=giveUp)
    board.pack()  # 放到主窗口中
    give_up.pack()
    menu_container.pack()
    
    root.mainloop() # 进入主循环
    pass

def giveUp():
    messagebox.showinfo("信息", "你输了")
    pass

init_canvas()



