import random
import os
import itertools

def initialize_grid(size):
    grid = [[0] * size for _ in range(size)]
    return grid

def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

def print_grid(grid):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in grid:
        print(" ".join(str(cell).rjust(4) if cell != 0 else '.'.rjust(4) for cell in row))
    print("\n")

def combine_tiles(row):
    new_row = []
    i = 0
    while i < len(row):
        if i < len(row) - 1 and row[i] == row[i + 1]:
            new_row.append(row[i] * 2)
            i += 2
        else:
            new_row.append(row[i])
            i += 1
    new_row.extend([0] * (len(row) - len(new_row)))
    return new_row

def move_left(grid):
    new_grid = []
    for row in grid:
        new_row = combine_tiles([cell for cell in row if cell != 0])
        new_grid.append(new_row)
    return new_grid

def transpose_grid(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

def move(grid, direction):
    if direction == 'up':
        grid = transpose_grid(grid)
        grid = move_left(grid)
        grid = transpose_grid(grid)
    elif direction == 'down':
        grid = transpose_grid(grid)
        grid = move_left(grid[::-1])
        grid = transpose_grid(grid)[::-1]
    elif direction == 'left':
        grid = move_left(grid)
    elif direction == 'right':
        grid = [row[::-1] for row in grid]
        grid = move_left(grid)
        grid = [row[::-1] for row in grid]
    return grid

def is_game_over(grid):
    for row in grid:
        if 2048 in row:
            return True
    for i in range(len(grid) - 1):
        for j in range(len(grid[0]) - 1):
            if grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]:
                return False
    return True

def main():
    size = 4
    grid = initialize_grid(size)
    add_new_tile(grid)
    add_new_tile(grid)
    
    while not is_game_over(grid):
        print_grid(grid)
        direction = input("Enter direction (up/down/left/right): ").strip().lower()
        if direction in ['up', 'down', 'left', 'right']:
            new_grid = move(grid, direction)
            if new_grid != grid:
                add_new_tile(new_grid)
                grid = new_grid
    
    print("Game Over! Your score:", max(itertools.chain(*grid)))

if __name__ == "__main__":
    main()
