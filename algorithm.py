# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Corey <390583019@qq.com>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/26 20:48:03 by Corey             #+#    #+#              #
#    Updated: 2018/09/27 09:41:29 by Corey            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0

random.seed(0)


score = {
    'win5': 100,
    'alive4': 90,
    'double_dead4': 90,
    'dead4_alive3': 80,
    'double_alive3': 70,
    'alive3_dead_3': 60,
    'dead4': 50,
    'jump_dead4': 40,
    'alive3': 30,
    'double_alive2': 15,
    'alive2': 10,
    'jump_alive2': 8,
    'dead3': 5,
    'dead2': 3,
    'others': 2,
    'single': 1

}

class AI(object):
    """My gobang AI Algorithm"""
    def __init__(self,chessboard_size,color,time_out):
        self.chessboard_size = chessboard_size # 15 * 15
        self.color = color # the ai's color black/white
        self.time_out = time_out # the limit time
        self.candidate_list = [] # the position list
        self.my_max_score = 0
        self.human_max_score = 0
        self.pos_score = 0
        pass


    # random version
    def go(self,chessboard):
        self.candidate_list.clear()

        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0],idx[1]))

        pos_idx = random.randint(0, len(idx)-1)
        new_pos = idx[pos_idx]

        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE

        self.candidate_list.append(new_pos)
        
        pass
    
