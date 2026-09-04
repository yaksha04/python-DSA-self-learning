from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = {}

        # Find S and number all L cells
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total_litter = len(litter)

        if total_litter == 0:
            return 0

        # State: row, col, collected_litter_mask, remaining_energy
        queue = deque()
        queue.append((start[0], start[1], 0, energy))

        visited = set()
        visited.add((start[0], start[1], 0, energy))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0
        target = (1 << total_litter) - 1

        while queue:
            for _ in range(len(queue)):
                r, c, mask, curr_energy = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # No energy left
                    if curr_energy == 0:
                        continue

                    new_energy = curr_energy - 1
                    new_mask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        new_mask |= 1 << litter[(nr, nc)]

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # All litter collected
                    if new_mask == target:
                        return moves + 1

                    state = (nr, nc, new_mask, new_energy)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1
