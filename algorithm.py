# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Corey <390583019@qq.com>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/26 20:48:03 by Corey             #+#    #+#              #
#    Updated: 2018/10/17 14:23:52 by Corey            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import numpy as np
import random
import time

COLOR_BLACK = 2
COLOR_WHITE = 1
COLOR_NONE = 0
DEPTH = 0  # search depth

black_score = {
    '22222': 50000,
    '022220': 4320,
    '02220': 800,
    '022020': 720,
    '020220': 720,
    '22220': 800,
    '02222': 800,
    '22022': 720,
    '022202': 800,
    '22202': 720,
    '202220': 800,
    '20222': 720,
    '002200': 120,
    '02020': 100,
    '00200':20
}

white_score = {
    '11111': 50000,
    '011110': 4320,
    '01110': 800,
    '011010': 720,
    '010110': 720,
    '11110': 800,
    '01111': 800,
    '11011': 720,
    '011101': 800,
    '11101': 720,
    '101110': 800,
    '10111': 720,
    '001100': 120,
    '01010': 100,
    '00100': 20
    # '001100': 120,
    # '001010': 120,
    # '010100': 120,
    # '000100': 20,
    # '001000': 20
    # '001110': 719,
}


class AI():
    """My gobang AI Algorithm"""

    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size  # 15 * 15
        self.color = color  # the ai's color black/white. -1 is black.
        self.time_out = time_out  # the limit time
        # the position list. System will get the end of candidate_list as decision .
        self.candidate_list = []
        pass

    def go(self, chessboard):
        print('chessboard: ')
        print(chessboard)
        chessboard[chessboard<0] = 2
        start = starting(chessboard)
        self.candidate_list.clear()
        start_time = time.time()

        # algorithm here
        # staring library
        if start.starting_list():
            new_pos = start.starting_list()
            self.candidate_list.append(new_pos)
            print('final_idx: ', new_pos)
            run_time = time.time() - start_time
            print('Run time: ', run_time, 's')
            return

        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))

        # the list of every empty point's score     
        idx_my_score_list = [evaluate(idxs, True, chessboard) for idxs in idx]
        idx_enemy_score_list = [evaluate(idxs, False, chessboard) for idxs in idx]
        
        if max(idx_my_score_list) >= max(idx_enemy_score_list):
            score_dict = dict(zip(list(zip(idx_my_score_list,idx_enemy_score_list)),idx))   
        else:
            score_dict = dict(zip(list(zip(idx_enemy_score_list,idx_my_score_list)),idx))
        new_pos = score_dict[max(score_dict)]
        
        print('final_idx: ', new_pos)
        self.candidate_list.append(new_pos)
        run_time = time.time() - start_time
        print('Run time: ', run_time,'s')

        # for debug
        # print('my score list: ', idx_my_score_list)
        # print('enemy score list: ', idx_enemy_score_list)
        # print(score_dict)
        pass

def evaluate(node, black, chessboard):
    chessboard[node[0], node[1]] = 2 if black else 1
    evaluate_score = black_score if black else white_score
    # print('chessboard: ')
    # print(chessboard)
    horizonal_list = []
    vertical_list = []
    diagonal_list = []
    arc_diagonal_list = []
    idx_score = 0

    vertical_lower = -min(node[0], 5)
    vertical_upper = min(6 , 15-node[0])
    horizonal_lower = -min(node[1], 5)
    horizonal_upper = min(6 ,15-node[1])
    diagonal_lower = max(vertical_lower,horizonal_lower)
    diagonal_upper = min(vertical_upper,horizonal_upper)
    arc_diagonal_lower = -min(14-node[0], node[1],5)
    arc_diagonal_upper = min(node[0]+1, 15-node[1],6)


    for i in range(horizonal_lower,horizonal_upper):
        horizonal_list.append(chessboard[node[0], node[1]+i])
    for i in range(vertical_lower, vertical_upper):
        vertical_list.append(chessboard[node[0]+i, node[1]])
    for i in range(diagonal_lower, diagonal_upper):
        diagonal_list.append(chessboard[node[0]+i, node[1]+i])
    for i in range(arc_diagonal_lower,arc_diagonal_upper):
        arc_diagonal_list.append(chessboard[node[0]-i,node[1]+i])
    
    horizonal = ''.join(str(horizonal_item) for horizonal_item in horizonal_list)
    vertical = ''.join(str(vertical_item) for vertical_item in vertical_list)
    diagonal = ''.join(str(diagonal_item) for diagonal_item in diagonal_list)
    arc_diagonal = ''.join(str(arc_diagonal_item) for arc_diagonal_item in arc_diagonal_list)

    # for debug
    # if(horizonal):
    #     print('horizonal: ', horizonal)
    # if(vertical):
    #     print('vertical: ', vertical)
    # if(diagonal):
    #     print('diagonal: ', diagonal) 
    # if(arc_diagonal):
    #     print('arc_diagonal: ',arc_diagonal)

    for shape in evaluate_score.keys():
        if shape in horizonal:
            idx_score += evaluate_score[shape]
            # print('1 ', shape, 'score: ', evaluate_score[shape])
        if shape in vertical:
            idx_score += evaluate_score[shape]
            # print('2 ', shape, 'score: ', evaluate_score[shape])
        if shape in diagonal:
            idx_score += (evaluate_score[shape]+20)
            # print('3 ', shape, 'score: ', evaluate_score[shape])
        if shape in arc_diagonal:
            idx_score += (evaluate_score[shape]+20)
            # print('4 ', shape, 'score: ', evaluate_score[shape])
    # print(idx_score)
    chessboard[node[0], node[1]] = 0
    return idx_score

def evaluate_whole(node, black, chessboard):
    chessboard[node[0], node[1]] = 2 if black else 1
    evaluate_score = black_score if black else white_score
    whole_score = 0
    for i in range(15):
        horizonal = ''.join(str(item) for item in chessboard[i, :])
        vertical = ''.join(str(item) for item in chessboard[:, i])
        for shape in evaluate_score.keys(): 
            if shape in horizonal:
                whole_score += evaluate_score[shape]
            if shape in vertical:
                whole_score += evaluate_score[shape]


    pass


# def MinMax(node, depth, isAI):
#     if depth == 0:
#         return evaluate(node, isAI)
#     score = float('-inf') if isAI else float('inf')
#     for subnode in node:
#         value = MinMax(subnode, depth-1, not isAI)
#         score = max(score, value) if isAI else min(score, value)

class starting():
    """ Starting Library """

    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.chessboard[self.chessboard < 0] = 2
        self.return_pos = ()
        pass
    def starting_list(self):
        if len(self.chessboard[self.chessboard != 0]) == 0:
            self.return_pos = (7, 7)
            return self.return_pos
        if len(self.chessboard[self.chessboard == 1]) == COLOR_WHITE and len(self.chessboard[self.chessboard == COLOR_BLACK]) == 1:
            black_point = np.where(self.chessboard == COLOR_BLACK)
            black_point_x, black_point_y = black_point[0][0], black_point[1][0]
            white_point = np.where(self.chessboard == COLOR_WHITE)
            white_point_x, white_point_y = white_point[0][0], white_point[1][0]
            # huayue
            if ((black_point_x - white_point_x)**2 + (black_point_y - white_point_y)**2 == 1):
                self.return_pos = (white_point_x, white_point_y + 1) if black_point_y == white_point_y else (black_point_x-1, white_point_y)
            # puyue
            if ((black_point_x - white_point_x)**2 + (black_point_y - white_point_y)**2 == 2):
                self.return_pos= (black_point_x+1,white_point_y) if black_point_x > white_point_x else (black_point_x-1, white_point_y)
            return self.return_pos
        pass
    pass



