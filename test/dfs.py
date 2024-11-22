class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state          # The current state of the node
        self.parent = parent        # The parent node (for backtracking)
        self.action = action        # The action taken to get to this node
        self.path_cost = path_cost  # The cost of the path to this node

    # def __repr__(self):
    #     return f"<Node state={self.state}>"


def depth_first_search(problem):
    # Initialize the fringe with the initial state
    fringe = [Node(problem.initial)]
    closed = set()

    while fringe:
        node = fringe.pop()  # Remove the node from the fringe (LIFO)

        # Check if the goal has been reached
        if problem.goal_test(node.state):
            return node  # Return the node containing the goal state

        # If the node's state has not been explored yet
        if node.state not in closed:
            closed.add(node.state)  # Mark the state as explored

            # Expand the node, adding each child to the fringe
            for child in expand(problem, node):
                fringe.append(child)

    return None  # Return failure if no solution is found


def expand(problem, node):
    # Generate child nodes for all possible actions in the current state
    children = []
    for action in problem.actions(node.state):
        child_state = problem.result(node.state, action)
        child_node = Node(child_state, node, action, node.path_cost + problem.step_cost(node.state, action))
        children.append(child_node)
    return children


# Example usage:
class SimpleGraphProblem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        # Returns the list of possible actions (neighbors) from the given state
        return self.graph[state]

    def result(self, state, action):
        # Returns the resulting state after applying the given action
        return action

    def goal_test(self, state):
        # Returns True if the given state is the goal state
        return state == self.goal

    def step_cost(self, state, action):
        # Returns the cost of taking the action from the given state
        return 1  # Assume all steps have the same cost

# Define a simple graph as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Create a problem instance
problem = SimpleGraphProblem('A', 'G', graph)

# Run DFS to find the goal node
solution_node = depth_first_search(problem)

# Print the solution path
if solution_node:
    path = []
    node = solution_node
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print("Solution path:", path)
else:
    print("No solution found")
