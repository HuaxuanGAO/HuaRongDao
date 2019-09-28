import numpy as np
import unit

def init_board():
    board = np.zeros((5,4), dtype=int)
    cc = unit.Cc(1, (0,1))
    z1 = unit.Zu(2, (0,0))
    z2 = unit.Zu(3, (1,0))
    z3 = unit.Zu(4, (0,3))
    z4 = unit.Zu(5, (1,3))
    heng1 = unit.Heng(6, (2,0))
    heng2 = unit.Heng(7, (2,2))
    heng3 = unit.Heng(8, (3,0))
    heng4 = unit.Heng(9, (3,2))
    heng5 = unit.Heng(10, (4,1))

    all_units = [cc, z1, z2, z3, z4, heng1, heng2, heng3, heng4, heng5]
    for i in all_units:
        i.place(board)
    return board

def get_current_units(board):
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
    return units

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

def success(board):
    res = board[3:5, 1:3] == 1
    success = True
    for i in res:
        for j in i:
            success = success and j
    return success

def BFS(queue, visited): 
    while len(queue)>0: 
        # Dequeue a vertex from  
        # queue and print it 
        board = queue.pop(0) 
        print(board) 
        # Get all adjacent vertices of the 
        # dequeued vertex s. If a adjacent 
        # has not been visited, then mark it 
        # visited and enqueue it 
        for movable_unit_index in get_movable_units(board):
            current_units = get_current_units(board)
            movable_unit = current_units[movable_unit_index-1] # from the unit.index to index in all_unit list
            print("moving " + str(movable_unit_index))
            print(movable_unit.pos)
            for i in ["up", "left", "down", "right"]: 
                current_board = board.copy()
                if i == "up":
                    if not movable_unit.up(current_board):
                        continue
                if i == "left":
                    if not movable_unit.left(current_board):
                        continue
                if i == "down":
                    if not movable_unit.down(current_board):
                        continue
                if i == "right":
                    if not movable_unit.right(current_board):
                        continue
                if success(current_board):
                    print("Done")
                    break
                if visited.get(current_board.tobytes()) != True: 
                    print("new state")
                    print(current_board)
                    print("move " + str(movable_unit_index))
                    print("to " + str(movable_unit.pos))
                    queue.append(current_board)
                    visited[current_board.tobytes()] = True
                else:
                    print("repeated")

board = init_board()
visited = {}
# Create a queue for BFS 
queue = []
# Mark the source node as  
# visited and enqueue it 
visited[board.tobytes()] = True
queue.append(board) 
print(board)
all_units = get_current_units(board)
BFS(queue, visited)
# print(len(all_units))
# for i in all_units:
#     print(i.index)
#     print(i.pos)