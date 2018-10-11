# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Corey <390583019@qq.com>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/26 20:48:03 by Corey             #+#    #+#              #
#    Updated: 2018/10/11 22:26:09 by Corey            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python



import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
DEPTH = 0 # search depth


# random.seed(0)

evaluate_score = {
    '-1-1-1-1-1': 50000,
    '0-1-1-1-10': 4320,
    '0-1-1-100': 720,
    '00-1-1-10': 720,
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

class AI(object):
    """My gobang AI Algorithm"""
    def __init__(self,chessboard_size,color,time_out):
        self.chessboard_size = chessboard_size # 15 * 15
        self.color = color # the ai's color black/white. -1 is black.
        self.time_out = time_out # the limit time
        self.candidate_list = [] # the position list. System will get the end of candidate_list as decision .
        self.my_max_score = 0
        self.human_max_score = 0
        self.pos_score = 0
        self.isAI = True
        pass



    def go(self,chessboard):
        self.candidate_list.clear()
        start_time = time.time()
        # algorithm here
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0],idx[1]))
        idx_score = [evaluate(idxs, True) for idxs in idx]
        max_idx_score = max(idx_score)
        score_dict = dict(zip(idx,idx_score))
       
       
        new_pos = None
        self.candidate_list.append(new_pos)     
        run_time = time.time() - start_time
        pass






    def MinMax(node,depth,isAI):
        if depth ==0:
            return evaluate(node,isAI)

        score = float('-inf') if isAI else float('inf')

        for subnode in node:
            value = MinMax(subnode,depth-1,not isAI)
            score = max(score, value) if isAI else min(score, value)


    def evaluate(node,isAI):
        horizonal_list = []
        vertical_list = []
        diagonal_list = []
        idx_score = 0
        for i in range(-2,3):
            horizonal_list.append((node[0],node[1]+i))
            vertical_list.append((node[0]+i,node[1]))
            diagonal_list.append((node[0]+i,node[1]+i))
        horizonal = ''.join(str(horizonal_item) for horizonal_item in horizonal_list)
        vertical = ''.join(str(vertical_item) for vertical_item in vertical_list)
        diagonal = ''.join(str(diagonal_item) for diagonal_item in diagonal_list)
        if 
        pass


# random version
# def go(self,chessboard):
#     self.candidate_list.clear()

#     idx = np.where(chessboard == COLOR_NONE)
#     idx = list(zip(idx[0],idx[1]))

#     pos_idx = random.randint(0, len(idx)-1)
#     new_pos = idx[pos_idx]

#     assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE

#     self.candidate_list.append(new_pos)
    
#     pass
    
