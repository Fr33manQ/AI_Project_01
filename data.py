# /*
#  * @Author: CoreyQiu 
#  * @Date: 2018-09-07 19:30:57 
#  * @Last Modified by:   CoreyQiu 
#  * @Last Modified time: 2018-09-07 19:30:57 
#  */

import tkinter as tk



chessboard=[]
for i in range(15):
    chessboard.append([])
    for j in range(15):
        chessboard[i].append([True,False,False])
# 15 * 15 3-d array. the 3rd dimension represents no chess / black chess / white chess


decision_scores = {
    '5': 100,
    'alive4': 90,
    '2dead4': 90,
    'dead4alive3': 80,
    '2alive3': 70



}

player_score = 0
ai_score = 0
# when someone reaches 100 score, he/she wins. 
