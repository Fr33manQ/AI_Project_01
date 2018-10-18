
# /*
#  * @Author: CoreyQiu 
#  * @Date: 2018-09-07 19:21:03 
# * @Last Modified by:   CoreyQiu
# * @Last Modified time: 2018-09-08 14: 40: 15
# */

import tkinter as tk
from tkinter import messagebox
import sys
import numpy as np

import data
from algorithm import AI

choose_first = True  # player choose if he/she play first

root = tk.Tk()
root.title('Gobang') # 15 * 15 的棋盘  15 * 40 = 600  + 两端的空白 - 多出的一行
board = tk.Canvas(root, width=620-40, height=620-40, bg='#dacfa0')
menu_container = tk.Canvas(root, width=580, height=10)  # Menu


class canvas():
    def __init__(self):
        
        self.chessboard = np.zeros((15, 15), dtype=np.int)
        self.init_canvas()
        root.mainloop()  # 进入主循环
        pass
    def init_canvas(self):
        for i in range(15):
            board.create_line(10, 10+i*40, 610-40, 10+i*40)
        for i in range(15):
            board.create_line(10+i*40, 10, 10+i*40, 610-40)
        for i in range(3, 12, 8):
            board.create_oval(i*40+10-3, 127, i*40+10+3, 133, fill='black')
            board.create_oval(i*40+10-3, 127+320, i*40+10+3, 133+320, fill='black')
        board.create_oval(287, 287, 293, 293, fill='black')

        board.bind('<Button-1>', self.click)

        give_up = tk.Button(menu_container,width=10,height=2,text='投降',command=self.giveUp)
        exit_button = tk.Button(menu_container,width=10,height=2,text='退出',command=sys.exit)
        # replay = tk.Button(menu_container, width=10, height=2, text='重开', command=init_board)



        board.pack(padx='2',pady='2')  # 放到主窗口中
        menu_container.pack(padx='2',pady='2')
        give_up.pack(side='left',padx='2',pady='3')
        # replay.pack(side='right', padx='2', pady='3')
        exit_button.pack(side='right',padx='2',pady='3')

    def click(self,event):
        paint_x = ((event.x+10) // 40) * 40 + 10
        paint_y = ((event.y+10) // 40) * 40 + 10
        # print(paint_x//40,paint_y//40)

        chess_color = 'black' if choose_first else 'white'
        enemy_color = 'white' if choose_first else 'black'
        board.create_oval(paint_x-13, paint_y-13, paint_x+13, paint_y+13, fill=chess_color)
        # print(event.x,event.y)

        ai = AI(15, chess_color, 500)
        self.chessboard[paint_x//40, paint_y//40] = 1 if choose_first else -1
        ai.go(self.chessboard)
        self.chessboard[ai.candidate_list] = -1 if choose_first else 1
        enemy_x, enemy_y = ai.candidate_list[-1]
        print(enemy_x, enemy_y)
        board.create_oval(enemy_x*40+10-13, enemy_y*40+10-13,enemy_x*40+10+13, enemy_y*40+10+13, fill=enemy_color)
        print(paint_x, paint_y)
        print(enemy_x*40, enemy_y*40)

    def giveUp(self):
        messagebox.showinfo("Score", "You Lose!")
        data.ai_score = 100
        sys.exit()
        pass
        



# def start():
#     starting = tk.Tk()
#     starting.title('Choose Your Turn')
#     prompt = tk.Label(starting,text='选择先手或是后手')
#     first=tk.Button(starting,text='先手',command=choosing_first)
#     second=tk.Button(starting, text='后手',command=choosing_second)
    
#     prompt.pack()
#     first.pack(side='left')
#     second.pack(side='right')

#     starting.mainloop()


# def choosing_first():
#     choose_first=True
#     sys.exit()
#     main()

# def choosing_second():
#     choose_first=False
#     sys.exit()
#     main()
#     pass






    







canvas()

