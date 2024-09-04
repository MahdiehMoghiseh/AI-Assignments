from params import *
import colors

class Agent:
    def __init__(self, board):
        self.position = board.get_agent_pos()
        self.current_state = board.get_current_state()
        self.board = board
        self.bfs_num_iterations = 0
        self.dfs_num_iterations = 0
        self.aStar_num_iterations = 0

    def get_position(self):
        return self.position

    def set_position(self, position, board):
        self.position = position
        board.set_agent_pos(position)
        board.update_board(self.current_state)

    def percept(self, board):
        # perception :
        # sets the current state
        # Use get_current_state function to get the maze matrix. - make your state
        self.current_state = board.get_current_state()

        pass

    def move(self, direction):
        # make your next move based on your perception
        # check if the move destination is not blocked
        # if not blocked:
        # use red color to show visited tiles.
        # something like :
        current_pos = self.get_position()
        x, y = current_pos[0], current_pos[1]
        self.board.colorize(x, y, self.colors.red)
        
        # then move to destination - set new position
        # something like :
        self.set_position(self.get_position() + direction)

        pass

    @staticmethod

    def get_actions(self, position):
        actions = []
        x, y = position.x, position.y
        
        if (x - 1) >= 0 and (x - 1) < rows : 
            help = self.board.boardArray[x - 1][y]
            if not help.is_blocked():
                actions.append(help)
        if (x + 1) >= 0 and (x + 1) < rows : 
            help = self.board.boardArray[x + 1][y]
            if not help.is_blocked():
                actions.append(help)
        if (y - 1) >= 0 and (y - 1) < cols : 
            help = self.board.boardArray[x][y - 1]
            if not help.is_blocked():
                actions.append(help)
        if (y + 1) >= 0 and (y + 1) < cols :
            help = self.board.boardArray[x][y + 1]
            if not help.is_blocked():
                actions.append(help)
        # returns a list of valid actions
        return actions

    def bfs(self, environment, start, end):
        # now go on !
        frontier = []
        # node is a tile object
        node = self.board.boardArray[self.position[0]][self.position[1]]  # tile object
        frontier.append(node)
        reached = {}     # use dictionary to access children of a node 
        while len(frontier) != 0:
            self.bfs_num_iterations += 1
            node = frontier.pop(0)
            if node.isGoal:
                break
            expand = self.get_actions(self, node)
            for child in expand:
                help = child.x, child.y
                list_help = list(reached.keys())
                if help not in list_help:
                    frontier.append(child)
                    reached[(child.x, child.y)] = node.x, node.y

        # colorize the path
        start = start['x'], start['y']
        end = end['x'], end['y']
        node = help      
        while reached.get(node) is not None:
            node = reached.get(node)
            if node == start:
                break
            if node == end:
                continue
            environment.colorize(node[0], node[1], colors.green)

        # use green color and colorize method to show the path. 
        pass

    def dfs(self, environment, start, end):
        frontier = []
        # node is a tile object
        node = self.board.boardArray[self.position[0]][self.position[1]]  # tile object
        frontier.append(node)
        reached = {}     # use dictionary to access children of a node 
        while len(frontier) != 0:
            self.dfs_num_iterations += 1
            node = frontier.pop()
            if node.isGoal:
                break
            expand = self.get_actions(self, node)
            for child in expand:
                help = child.x, child.y
                list_help = list(reached.keys())
                if help not in list_help:
                    frontier.append(child)
                    reached[(child.x, child.y)] = node.x, node.y

        # colorize the path
        start = start['x'], start['y']
        end = end['x'], end['y']
        node = help      
        while reached.get(node) is not None:
            node = reached.get(node)
            if node == start:
                break
            if node == end:
                continue
            environment.colorize(node[0], node[1], colors.red)
        pass

    def heuristic_manhattan(self, start_pos, goal_pos):
        distance = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
        return distance

    def a_star(self, environment, start, end):
        # after every step, g++
        # f = g + h 
        h = []
        g = []
        frontier = []
        start = start['x'], start['y']
        end = end['x'], end['y']
        # node is a tile object
        node = self.board.boardArray[self.position[0]][self.position[1]]  # tile object
        frontier.append(node)
        h.append(self.heuristic_manhattan(start, end))
        gg = 0
        g.append(gg)
        reached = {}     # use dictionary to access children of a node 
        mini = h[0] + g[0]
        mini_index = 0
        while len(frontier) != 0:
            self.aStar_num_iterations += 1
            for i in range(len(frontier)):
                if h[i] + g[i] < mini:
                    mini = h[i] + g[i]
                    mini_index = i
            node = frontier.pop(mini_index)
            h.pop(mini_index)
            g.pop(mini_index)
            if node.isGoal:
                break
            expand = self.get_actions(self, node)
            gg += 1
            for child in expand:
                help = child.x, child.y
                list_help = list(reached.keys())
                if help not in list_help:
                    frontier.append(child)
                    reached[(child.x, child.y)] = node.x, node.y
                    h.append(self.heuristic_manhattan(end, (child.x, child.y)))
                    g.append(gg)

        # colorize the path
        node = help      
        while reached.get(node) is not None:
            node = reached.get(node)
            if node == start:
                break
            if node == end:
                continue
            environment.colorize(node[0], node[1], colors.blue)

        pass
