# Sudoku Solver 🧩

数独求解器 - 使用约束传播和搜索算法解决数独谜题。

## 🎯 项目简介

本项目实现了多种数独求解算法，包括：
- 回溯算法
- 约束传播
- AI 搜索策略

## 📂 项目结构

```
Sudoku/
├── __init__.py    # 包包初始化
├── solution.py    # 核心求解算法
└── utils.py       # 工具函数
```

## 🧠 算法实现

### 约束传播 (Constraint Propagation)
```
1. 消除策略: 从格子中排除不可能的值
2. 唯一候选: 如果格子只有一个可能值，则确定
3. 隐式唯一: 如果某值在某单元只有一个位置
```

### 搜索算法
```
def search(values):
    if 已解决: return values
    选择候选数最少的格子
    for 每个候选值:
        尝试赋值并递归搜索
        if 成功: return 结果
    return 失败
```

## 🚀 快速开始

```python
from solution import solve

# 定义数独 (0 表示空格)
grid = """
4.....8.5
.3.......
...7.....
.2.....6.
....8.4..
....1....
...6.3.7.
5........
..4......
"""

solution = solve(grid)
print(solution)
```

## 📊 性能

- **简单数独**: < 1ms
- **中等数独**: < 10ms
- **困难数独**: < 100ms

## 📖 算法参考

- Peter Norvig's Sudoku Solver: http://norvig.com/sudoku.html

## 👤 作者

MengqiYe

## 📄 许可证

MIT License
