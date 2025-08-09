                                                            #_______________________________________________
                                                            #               Submitted by:
                                                            #   Name: Prashanna Raj pandit
                                                            #_______________________________________________



# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # Output:
    # ('Start:', (5, 5))
    # ('Is the start a goal?', False)
    # ("Start's successors:", [((5, 4), 'South', 1), ((4, 5), 'West', 1)])

    fringe=util.Stack()                                                       # creating a stack data structure to sore finge nodes
    explored=[]                                                               # this is list of explored nodes
    startNode={"state":problem.getStartState(),"cost":0}                      # creating a startNode which is a dictionary. it contains a state(i.e.position) and cost to that position. direction is not set to the start node.
    
    fringe.push(startNode)                                                    # push the node into the Stack

    while fringe:                                                             # Iterate until there is no fringe in the Stack
        currentNode=fringe.pop()                                              # pop the recent node from the stack and traverse the deepest node in graph
        if currentNode["state"] not in explored:                              # if this node is not explored then put it in explored list and find the sucessors otherwise pop the next node from stack
            explored.append(currentNode["state"])
            if problem.isGoalState(currentNode["state"]):                     #if the node is the goal node then return the list of actions(i.e directions) from start to the goal node otherwise find the child of this node
                direction=[]
                while "parent" in currentNode:                                # this while loop runs until there is no parent of node (i.e until the goal node back traverse the start node)
                    direction.append(currentNode["direction"])
                    currentNode=currentNode["parent"]
                direction.reverse()
                return direction
            for sucessor in problem.getSuccessors(currentNode["state"]):      # sucessor is a list of tuples -> [(state, direction, cost)] as shown in ("Start's successors:", [((5, 4), 'South', 1), ((4, 5), 'West', 1)]))
                children={"state":sucessor[0],"direction":sucessor[1],"cost":sucessor[2],"parent":currentNode}  # creating a child (node) dictionary after unpacking list from sucessor function and adding a parent key for back tracking
                fringe.push(children)                                          # push children node in to the stack

    raise Exception("Failure! the fringe is empty")                            # raise exception when the stack becomes empty before finding the solution


    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # output: ('Start:', (34, 16))
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # output: ('Is the start a goal?', False)
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # output: ("Start's successors:", [((34, 15), 'South', 1), ((33, 16), 'West', 1)])

    fringe=util.Queue()                                               # Creating a Queue data structure to store fringe nodes
    explored=[]                                                       # creating a set to store the explored nodes

    node={"state":problem.getStartState(),"cost":0}                   # creating a dictionary node to store the state and cost of node. here we are storing starting node as {"state":(34,16),"cost":0} 
                                                                      # In the corners problem the state is represented as a tuple of starting position of the pacman and the list of corners as goal.
    fringe.push(node)                                                 # push the node into the Queue

    while fringe:                                                     # Iterate until there is no fringe in the Queue.
    
        node=fringe.pop()                                             # pop to explore the shallowest node in graph
        if node["state"] not in explored:                             # if this node is not explored then put it in explored set and find the sucessors otherwise pop the next node from queue.
            explored.append(node["state"])
            if problem.isGoalState(node["state"]):                    #if the node is the goal node then return the list of actions(i.e directions) to the goal node otherwise find the child of this node
                direction=[]
                while "parent" in node:                               # this while loop runs until there is no parent of node (i.e until the goal node back traverse the start node)
                    direction.append(node["direction"])
                    node=node["parent"]
                direction.reverse()
                return direction
            
            for sucessor in problem.getSuccessors(node["state"]):     # sucessor is a list of tuples -> [(state, direction, cost)] as shown in ("Start's successors:", [((34, 15), 'South', 1), ((33, 16), 'West', 1)])
                children={"state":sucessor[0],"direction":sucessor[1],"cost":sucessor[2],"parent":node}  # creating a child (node) dictionary after unpacking list from sucessor function.
                fringe.push(children)                                   # push children node in to queue

    raise Exception("failure !")                                        # raise exception when the queue becomes empty before finding the solution

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priorityQueue=util.PriorityQueue()                                  #for UCS, we create a priority Queue data structure. it pop's out the least cost state
    explored=set()                                                      # creating a set to track the explored states.

    startNode={"state":problem.getStartState(),"direction":[],"cost":0} # this time we create a node dictionary which contain state, list of directions e.g.[South,West] to that state and the cost required to that state
    
    priorityQueue.push(startNode,startNode["cost"])                     # pushing node into the priority queue and passing cost as it's priority
    
    while priorityQueue:                                                #Iterate until there is no fringe in the Priority Queue.
        node=priorityQueue.pop()                                        # pop the node which have least cost in the fringe. this is done by priority queue
        if node["state"] not in explored:                               # if this node is not explored then put it in explored set and find the sucessors otherwise pop the next node from queue
            explored.add(node["state"])
        
            if problem.isGoalState(node["state"]):                      # if this is a goal node than retuen the list of directions, which is required to get this node, from node dictionary
                return node["direction"]

            for sucessor in problem.getSuccessors(node["state"]):       #sucessor is a list of tuples -> [(state, direction, cost)] as shown in ("Start's successors:", [((34, 15), 'South', 1), ((33, 16), 'West', 1)])
                children={"state":sucessor[0],"direction":node["direction"]+[sucessor[1]],"cost":sucessor[2]+node["cost"]}  #creating a child dictionary and concatenating list of previous directions with the list of direction to this node.
                                                                                                                            # we are also adding the path cost to get total cost to this node
                priorityQueue.push(children,children["cost"])                # pushing child node to priority queue

    raise Exception("failure !")                                        # raise exception when the queue becomes empty before finding the solution
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priorityQueue=util.PriorityQueue()                                  #for A*, we create a priority Queue data structure. it pop's out the least cost state
    explored=[]                                                      # creating an explored list to track the explored states.

    startNode={"state":problem.getStartState(),"direction":[],"cost":0,"totalCost":0} # this time we create a node dictionary which contain state, list of directions e.g.[South,West] to that state,
                                                                                        # the cumulative cost required to that state and total cost i.e  cummumative cost + heuristic cost
    
    priorityQueue.push(startNode,startNode["totalCost"])            #pushing node and total cost as an argument in priority queue
    
    while priorityQueue:                                                #Iterate until there is no fringe in the Priority Queue.
        node=priorityQueue.pop()                                        # pop the node which have least cost in the fringe. this is done by priority queue
        if node["state"] not in explored:                               # if this node is not explored then put it in explored set and find the sucessors otherwise pop the next node from queue
            explored.append(node["state"])
        
            if problem.isGoalState(node["state"]):                      # if this is a goal node than retuen the list of directions, which is required to get this node, from node dictionary
                return node["direction"]
                    
            for sucessor in problem.getSuccessors(node["state"]):       #sucessor is a list of tuples -> [(state, direction, cost)] as shown in ("Start's successors:", [((34, 15), 'South', 1), ((33, 16), 'West', 1)])
                children={"state":sucessor[0],                          #sucessor[0]-> state    
                          "direction":node["direction"]+[sucessor[1]],  #sucessor[1]->direction
                          "cost":sucessor[2]+node["cost"],              #sucessor[2]-> cost
                          "totalCost":sucessor[2]+node["cost"]+heuristic(sucessor[0],problem)}  #creating a child dictionary and concatenating list of previous directions with the list of direction to this node.
                          # Here the totalCost f(n)=total cummulative path cost g(n)+ heuristic h(n); here the heuristic function takes two parameters-> state and problem.
                           
                priorityQueue.push(children,children["totalCost"])                # pushing child node to the priority queue

    raise Exception("failure !")  

    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
