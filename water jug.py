from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_capacity):
    queue = deque([(0, 0)])
    visited = set((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target_capacity or jug2 == target_capacity:
            return True

        # Fill jug1
        if jug1 < jug1_capacity:
            new_jug1 = jug1_capacity
            new_jug2 = jug2
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))
                visited.add((new_jug1, new_jug2))

        # Fill jug2
        if jug2 < jug2_capacity:
            new_jug1 = jug1
            new_jug2 = jug2_capacity
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))
                visited.add((new_jug1, new_jug2))

        # Empty jug1
        if jug1 > 0:
            new_jug1 = 0
            new_jug2 = jug2
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))
                visited.add((new_jug1, new_jug2))

        # Empty jug2
        if jug2 > 0:
            new_jug1 = jug1
            new_jug2 = 0
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))
                visited.add((new_jug1, new_jug2))

        # Pour jug1 into jug2
        if jug1 > 0 and jug2 < jug2_capacity:
            amount = min(jug1, jug2_capacity - jug2)
            new_jug1 = jug1 - amount
            new_jug2 = jug2 + amount
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))
                visited.add((new_jug1, new_jug2))

        # Pour jug2 into jug1
        if jug2 > 0 and jug1 < jug1_capacity:
            amount = min(jug2, jug1_capacity - jug1)
            new_jug1 = jug1 + amount
            new_jug2 = jug2 - amount
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))
                visited.add((new_jug1, new_jug2))

    return False

# Test the function
jug1_capacity = 4
jug2_capacity = 3
target_capacity = 2
result = water_jug_problem(jug1_capacity, jug2_capacity, target_capacity)
print(result)
