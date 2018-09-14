# /*
#  * @Author: CoreyQiu 
#  * @Date: 2018-09-14 13:01:48 
#  * @Last Modified by:   CoreyQiu 
#  * @Last Modified time: 2018-09-14 13:01:48 
#  */

# random version

import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0

random.seed(0)

class AI(object):
    """My AI Algorithm Class"""
    def __init__(self,chessboard_size,color,time_out):
        self.chessboard_size = chessboard_size # 15 * 15
        self.color = color # the ai's color black/white
        self.time_out = time_out # the limit time
        self.candidate_list = []
        pass

    def go(self,chessboard):
        self.candidate_list.clear()

        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0],idx[1]))

        pos_idx = random.randint(0, len(idx)-1)
        new_pos = idx[pos_idx]

        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE

        self.candidate_list.append(new_pos)
        
        pass
    
