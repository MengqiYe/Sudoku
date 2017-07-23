from utils import *

def grid_values(grid):
    values = []
    digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(digits)
        elif c in digits:
            values.append(c)
    assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, values))


def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        # print(box, peers[box])
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values


def only_choice(values):
    for unit in unitlist:
        for d in '123456789':
            dplaces = [box for box in unit if d in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = d
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        eliminate(values)

        # Your code here: Use the Only Choice Strategy
        only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    values = reduce_puzzle(values)
    if values == False:
        return False
    if all(len(values[b]) == 1 for b in boxes):
        return True
    n, b = min((len(values[b]), b) for b in boxes if len(values[b]) > 1)
    for v in values[b]:
        new_puzzle = values.copy()
        new_puzzle[b] = v
        s = search(new_puzzle)
        if s:
            return s


def test():
    grid = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    grid2 = grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
    display(search(grid2))
