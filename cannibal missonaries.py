from collections import deque

def is_valid_state(state):
    missionaries_left, cannibals_left, missionaries_right, cannibals_right = state
    return (missionaries_left >= cannibals_left and missionaries_right >= cannibals_right) and (missionaries_left + missionaries_right == 3) and (cannibals_left + cannibals_right == 3)

def solve_missionaries_cannibals():
    initial_state = (3, 3, 0, 0)  
    goal_state = (0, 0, 3, 3)  

    queue = deque([(initial_state, [])])  

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]  

        for next_state in generate_next_states(state):
            if is_valid_state(next_state):
                queue.append((next_state, path + [state]))

    return None  

def generate_next_states(state):
    missionaries_left, cannibals_left, missionaries_right, cannibals_right = state
    next_states = []

    next_states.append((missionaries_left - 1, cannibals_left, missionaries_right + 1, cannibals_right))

    next_states.append((missionaries_left, cannibals_left - 1, missionaries_right, cannibals_right + 1))

    next_states.append((missionaries_left - 2, cannibals_left, missionaries_right + 2, cannibals_right))

    next_states.append((missionaries_left, cannibals_left - 2, missionaries_right, cannibals_right + 2))

    return next_states

solution = solve_missionaries_cannibals()
if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found")
