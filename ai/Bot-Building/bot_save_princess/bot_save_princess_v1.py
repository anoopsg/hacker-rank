#!/usr/bin/python


def display_path_to_princess(n, grid):
    pos_col = {}
    pos_row = {}
    found = False

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                pos_row['m'] = i
                pos_col['m'] = j
            elif grid[i][j] == 'p':
                pos_row['p'] = i
                pos_col['p'] = j

    while (not found):
        if pos_row['m'] < pos_row['p']:
            pos_row['m'] = pos_row['m'] + 1
            print('DOWN')
        elif pos_row['m'] > pos_row['p']:
            pos_row['m'] = pos_row['m'] - 1
            print('UP')

        if pos_col['m'] < pos_col['p']:
            pos_col['m'] = pos_col['m'] + 1
            print('RIGHT')
        elif pos_col['m'] > pos_col['p']:
            pos_col['m'] = pos_col['m'] - 1
            print('LEFT')

        if pos_col['m'] == pos_col['p'] and pos_row['m'] == pos_row['m']:
            found = True


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

display_path_to_princess(m, grid)
