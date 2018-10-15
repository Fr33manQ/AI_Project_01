[TOC]







|   Service  | Master   |  Develop  |
| --------   | -----:   | :----: |
|   Build    | ![Develop Build](https://img.shields.io/badge/build-passing-brightgreen.svg)|![Develop Build](https://img.shields.io/badge/build-passing-brightgreen.svg) |
|  Platform  | ![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)    |   ![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)    |
|  Download  | ![Github All Releases](https://img.shields.io/badge/downloads-2.99k-brightgreen.svg) | ![Github All Releases](https://img.shields.io/badge/downloads%20-2.99k-brightgreen.svg)     |
|  Release   | ![release](https://img.shields.io/badge/release-v1.0-blue.svg)  | ![release](https://img.shields.io/badge/release-v1.1-blue.svg)    |


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

每次都遍历整个棋盘，寻找到：令我方决策分最高的点，最高分为`max(my_score)`；令敌方最高分的点，最高分为`max(enemy_score)`。一个点的得分为`max(my_score) + max(enemy_score)`
比较两个分数。如果`max(my_score)` > `max(enemy_score)`，则选择进攻。下`max(my_score)`的点。如果有多个点`my_score`相同，则选其中`enemy_score`最大的点。
反之，则选择防守。下`enemy_score`最大的点。如果有多个相同，则选择`my_score`最大的点。

优化：只在有棋子的地方的周围遍历。

## 打分方法
在棋盘空的位置 -> `chessboard == COLOR_NONE` 预下棋。对该位置四个方向上，各取13个格子。判断这13个（加上中心格子）形成的棋型是什么，进行打分。取这个位置的分`idx_score`为4个方向的`score`加起来的值。
然后在这些空的位置中取`idx_score`最高分的。

## 具体打分


```python
# 2 is black, 1 is white, 0 is none.

black_score = {
    '22222': 50000,
    '022220': 4320,
    '02220': 720,
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
    '002020': 120,
    '020200': 120,
    '000200': 20,
    '002000': 20
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