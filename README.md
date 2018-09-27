[TOC]







|   Service  | Master   |  Develop  |
| --------   | -----:   | :----: |
|   Build    | ![Develop Build](https://img.shields.io/badge/build-passing-brightgreen.svg)|![Master Build](https://img.shields.io/travis/:user/:repo.svg)    |
|  Platform  | ![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)    |   ![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)    |
|  Download  | ![Github All Releases](https://img.shields.io/badge/downloads-233k-brightgreen.svg) | ![Github All Releases](https://img.shields.io/badge/downloads%20-250k-brightgreen.svg)     |
|  Release   | ![release](https://img.shields.io/badge/release-v0.1-blue.svg)  | ![release](https://img.shields.io/badge/release-v0.2-blue.svg)    |


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

每次都遍历整个棋盘，寻找到：令我方决策分最高的点，最高分为`my_max_score`；令地方最高分的点，最高分为`human_max_score`。
比较两个分数。如果`my_max_score` > `human_max_score`，则选择进攻。下`my_max_score`的点。如果有多个点`my_max_score`相同，则选其中`human_max_score`最大的点。
反之，则选择防守。下`human_max_score`最大的点。如果有多个相同，则选择`my_max_score`最大的点。

优化：只在有棋子的地方的周围遍历。

## 打分方法
在棋盘空的位置 -> `chessboard == COLOR_NONE` 预下棋。对该位置四个方向上，各取4个格子。判断这5个（加上中心格子）形成的棋型是什么，进行打分。取这个位置的分`pos_score`为4个方向的`score`加起来的值。
然后在这些空的位置中取`pos_score`最高分的。

## 具体打分

成五：五子连珠 - ooooo - 胜利 - 100分

活四：构成两端不被拦截的四子连珠 - ?oooo? - 后一步就赢了 - 90分

	双死四： 后一步就赢了 - 90分
	死四 + 活三：后两步 / 后一步就赢了 - 80分

	双活三：后两步就赢了 - 70分

	活三 + 死三：可以形成两个死四 / 形成一个活四 有可能在后两步赢 - 60分

死四：一端拦截的四子连珠 - ?xoooo? - 有可能在后一步赢 - 50分

跳死四：?oxooo? - 40分

单活三：两端不拦截的三子 - ?ooo? - 拦了一端，变成死四 - 30分

跳活三：o?oo - 20分 

双活二： 15分

活二：两端不拦截的二子 - 10分

跳活二： ?o?o? - 8分

死三：一端拦截的三子 - ?xooo? - 5分 

死二：一端拦截的二子 ?xoo? - 3分

其余：- 2分

单子：单独一颗棋子 - ?o? - 1分



# 变量

- 棋盘：15 * 15 

用`chessboard`来表示棋盘。

``` python
chessboard
COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
```

- 得分

得到100分的一方算胜利



# 算法
博弈树

极大值极小值搜索算法

Alpha Beta剪枝算法