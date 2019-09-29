import numpy as np
import unit
import time

class Board():
    def __init__(self, units) :
        self.units = units
        self.parent = None
    def set_parent(self, parent):
        self.parent = parent
    def get_all_units(self):
        res = []
        for i in self.units:
            res.append(i.copy()) # deep!
        return res 
    def get_unit(self, index):
        for i in self.units:
            if i.index == index:
                return i.copy()
    def to_int(self):
        board = np.zeros((5,4), dtype=int)
        for i in self.units:
            i.place(board)
        return board
    def to_string(self):
        board = np.zeros((5,4), dtype=str)
        for i in self.units:
            x = i.pos[0]
            y = i.pos[1]
            if i.text == "t":
                board[x:x+2, y:y+2] = "t"
            elif i.text == "h":
                board[x, y:y+2] = "h"
            elif i.text == "s":
                board[x:x+2, y] = "s"
            elif i.text == "d":
                board[x, y] = "d"

        return board

def get_board_from_int_board(board):
    units = []
    for i in range(10):
        distribution = np.where(board==i+1)
        points = len(distribution[0])
        position = (distribution[0][0], distribution[1][0])
        if(points==4):
            units.append(unit.Cc(i+1, position))
        if(points==1):
            units.append(unit.Zu(i+1, position))
        elif(points==2):
            # same x, Heng
            if distribution[0][0]==distribution[0][1]:
                units.append(unit.Heng(i+1, position))
            else:
                units.append(unit.Shu(i+1, position))
    return Board(units)

def neighbour_index(board, pos):
    res = []
    x = pos[0]
    y = pos[1]
    if x==0:
        res.append(board[1,y])
    elif x==board.shape[0]-1:
        res.append(board[board.shape[0]-2, y])
    else:
        res.append(board[x-1, y])
        res.append(board[x+1, y])

    if y==0:
        res.append(board[x,1])
    elif y==board.shape[1]-1:
        res.append(board[x, board.shape[1]-2])
    else:
        res.append(board[x, y-1])
        res.append(board[x, y+1])
    return set(res)

def get_movable_units(board):
    res = np.where(board==0)
    empty1 = (res[0][0], res[1][0])
    empty2 = (res[0][1], res[1][1])
    movable1 = neighbour_index(board, empty1)
    movable2 = neighbour_index(board, empty2)
    movable_set = movable1.union(movable2)
    movable_set.discard(0)
    return movable_set

def get_simplified_board(board):
    return

def success(board):
    res = board[3:5, 1:3] == 1
    success = True
    for i in res:
        for j in i:
            success = success and j
    return success

def BFS(queue, visited): 
    # queue store Board
    # visited store Board.to_string
    # do moving on Board.to_int
    while len(queue)>0: 
        # time.sleep(1)
        board = queue.pop(0) #BFS
        # board = queue.pop() #DFS 
        int_board = board.to_int()
        # print(int_board)
        # Get all adjacent vertices of the 
        # dequeued vertex s. If a adjacent 
        # has not been visited, then mark it 
        # visited and enqueue it 
        for movable_unit_index in get_movable_units(int_board):
            for i in ["up", "left", "down", "right"]: 
                temp_int_board = int_board.copy()
                movable_unit = board.get_unit(movable_unit_index) # from the unit.index to index in all_unit list
                # print("moving " + str(movable_unit_index))
                # print(movable_unit.pos)
                if i == "up":
                    if not movable_unit.up(temp_int_board):
                        continue
                if i == "left":
                    if not movable_unit.left(temp_int_board):
                        continue
                if i == "down":
                    if not movable_unit.down(temp_int_board):
                        continue
                if i == "right":
                    if not movable_unit.right(temp_int_board):
                        continue
                new_board = get_board_from_int_board(temp_int_board)
                new_board.set_parent(board)
                if success(temp_int_board):
                    print("Done")
                    return new_board
                # avoid duplicated cases
                if visited.get(new_board.to_string().tobytes()) != True: 
                    # print("new state")
                    # print(current_board)
                    # print("move " + str(movable_unit_index))
                    # print("to " + str(movable_unit.pos))
                    queue.append(new_board)
                    visited[new_board.to_string().tobytes()] = True
                    # print("repeated")
    return None