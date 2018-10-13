# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Corey <390583019@qq.com>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/26 20:48:03 by Corey             #+#    #+#              #
#    Updated: 2018/10/13 20:12:26 by Corey            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
DEPTH = 0  # search depth



black_score = {
    '-1-1-1-1-1': 50000,
    '0-1-1-1-10': 4320,
    '0-1-1-10': 720,
    # '00-1-1-10': 720,
    '0-1-10-10': 720,
    '0-10-1-10': 720,
    '-1-1-1-10': 720,
    '0-1-1-1-1': 720,
    '-1-10-1-1': 720,
    '-1-1-10-1': 720,
    '-10-1-1-1': 720,
    '00-1-100': 120,
    '00-10-10': 120,
    '0-10-100': 120,
    '000-100': 20,
    '00-1000': 20
}


white_score = {
    '11111': 49999,
    '011110': 4319,
    '01110': 719,
    # '001110': 719,
    '011010': 719,
    '010110': 719,
    '11110': 719,
    '01111': 719,
    '11011': 719,
    '11101': 719,
    '10111': 719,
    '001100': 119,
    '001010': 119,
    '010100': 119,
    '000100': 19,
    '001000': 19
}

class AI():
    """My gobang AI Algorithm"""

    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size  # 15 * 15
        self.color = color  # the ai's color black/white. -1 is black.
        self.time_out = time_out  # the limit time
        # the position list. System will get the end of candidate_list as decision .
        self.candidate_list = []
        self.my_max_score = 0
        self.human_max_score = 0
        self.pos_score = 0
        self.isAI = True
        pass

    def go(self, chessboard):
        self.candidate_list.clear()
        start_time = time.time()
        # algorithm here
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        print(idx)
        # the list of every empty point's score
        idx_score_list = [evaluate(idxs, chessboard) for idxs in idx]
        max_idx_score = max(idx_score_list)
        print('score: ')
        print(idx_score_list, max_idx_score)
        # a dict of {idx_score:idx}
        score_dict = dict(zip(idx_score_list, idx))
        new_pos = score_dict[max_idx_score]
        print('final_idx: ', new_pos)
        self.candidate_list.append(tuple(new_pos))
        run_time = time.time() - start_time
        print('Run time: ', run_time,'s')
        pass



def evaluate(node,chessboard):
    my_score = single_evaluate(node,True,chessboard)
    enemy_score = single_evaluate(node,False,chessboard)
    print(my_score+enemy_score)
    return my_score+enemy_score
    pass

def single_evaluate(node, black, chessboard):
    chessboard[node[0], node[1]] = -1 if black else 1
    evaluate_score = black_score if black else white_score
    print('chessboard: ')
    print(chessboard)
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
    if(horizonal):
        print('horizonal: ', horizonal)
    vertical = ''.join(str(vertical_item) for vertical_item in vertical_list)
    if(vertical):
        print('vertical: ', vertical)
    diagonal = ''.join(str(diagonal_item) for diagonal_item in diagonal_list)
    if(diagonal):
        print('diagonal: ', diagonal)
    arc_diagonal = ''.join(str(arc_diagonal_item) for arc_diagonal_item in arc_diagonal_list)
    if(arc_diagonal):
        print('arc_diagonal: ',arc_diagonal)

    for shape in evaluate_score.keys():
        if shape in horizonal:
            idx_score += evaluate_score[shape]
            print('1 ', shape, 'score: ', evaluate_score[shape])
        if shape in vertical:
            idx_score += evaluate_score[shape]
            print('2 ', shape, 'score: ', evaluate_score[shape])
        if shape in diagonal:
            idx_score += evaluate_score[shape]
            print('3 ', shape, 'score: ', evaluate_score[shape])
        if shape in arc_diagonal:
            idx_score += evaluate_score[shape]
            print('4 ', shape, 'score: ', evaluate_score[shape])
    chessboard[node[0], node[1]] = 0
    return idx_score
    pass


def MinMax(node, depth, isAI):
    if depth == 0:
        return evaluate(node, isAI)
    score = float('-inf') if isAI else float('inf')
    for subnode in node:
        value = MinMax(subnode, depth-1, not isAI)
        score = max(score, value) if isAI else min(score, value)


def test():
    test = AI()

