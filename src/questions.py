# Shopify OA Summer 2025
from collections import deque


def solve(width, height, nb_blocks, grid):
    def can_exit(grid, block_positions, block, width, height):
        # Check if the block can exit to the right without colliding with other blocks
        for (x, y) in block_positions[block]:
            for i in range(y + 1, width):
                if grid[x][i] != '.':
                    return False
        return True

    def remove_block(grid, block_positions, block):
        # Remove the block from the grid
        for (x, y) in block_positions[block]:
            grid[x][y] = '.'

    def find_removal_order(width, height, nb_blocks, grid):
        # Parse the grid to find block positions
        block_positions = {i: [] for i in range(nb_blocks)}
        for i in range(height):
            for j in range(width):
                if grid[i][j].isdigit():
                    block_positions[int(grid[i][j])].append((i, j))
        
        removal_order = []
        while len(removal_order) < nb_blocks:
            for block in range(nb_blocks):
                if block not in removal_order and can_exit(grid, block_positions, block, width, height):
                    removal_order.append(block)
                    remove_block(grid, block_positions, block)
                    break
        
        return removal_order
    
    queue = deque(find_removal_order(width, height, nb_blocks, grid))
    return queue.popleft()