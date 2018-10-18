[TOC]







|   Service  |  Master  |  Develop  |
| :------:   | :-----:  | :-------: |
|   Build    | ![Develop Build](https://img.shields.io/badge/build-passing-brightgreen.svg)|![Develop Build](https://img.shields.io/badge/build-passing-brightgreen.svg) |
|  Platform  | ![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)  |   ![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)    |
|  Download  | ![Github All Releases](https://img.shields.io/badge/downloads-717K-brightgreen.svg) | ![Github All Releases](https://img.shields.io/badge/downloads%20-717K-brightgreen.svg)     |
|  Release   | ![release](https://img.shields.io/badge/release-v2.0-blue.svg)  | ![release](https://img.shields.io/badge/release-v2.1-blue.svg)    |


# AI_Project_01

实现五子棋AI算法

# 所需知识

博弈树

最小-最大搜索

Alpha-Beta剪枝

# 胜负判断

每下一步棋就进行一次判断。

优化：只需对这一颗棋子的附近进行判断。

（在ai平台上不用自己写判断。）


# 下棋思路
## 打分思路

每次都遍历整个棋盘，寻找到：令我方决策分最高的点，最高分为`max(my_score)`；令敌方最高分的点，最高分为`max(enemy_score)`。
比较两个分数。如果`max(my_score)` > `max(enemy_score)`，则选择进攻。下`max(my_score)`的点。如果有多个点`my_score`相同，则选其中`enemy_score`最大的点。
反之，则选择防守。下`enemy_score`最大的点。如果有多个相同，则选择`my_score`最大的点。

优化：只在有棋子的地方的周围遍历。

## 打分方法
在棋盘空的位置 -> `chessboard == COLOR_NONE` 预下棋。对该位置四个方向上，各取13个格子。判断这13个（加上中心格子）形成的棋型是什么，进行打分。取这个位置的分`idx_score`为4个方向的`score`加起来的值。

## 具体打分


```python
# 2 is black, 1 is white, 0 is none.

black_score = {
    '22222': 50000,
    '022220': 4320,
    '02220': 800,
    '022020': 720,
    '020220': 720,
    '22220': 800,
    '02222': 800,
    '22022': 720,
    '022202': 720,
    '22202': 700,
    '202220': 720,
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
    '011101': 720,
    '11101': 700,
    '101110': 720,
    '001100': 120,
    '01010': 100,
    '00100': 20
}
```

# 变量

- 棋盘：15 * 15 

用`chessboard`来表示棋盘。(2d nparray)

``` python
chessboard
COLOR_BLACK = 2
COLOR_WHITE = 1
COLOR_NONE = 0
```



# 算法
博弈树

极大值极小值搜索算法

Alpha Beta剪枝算法