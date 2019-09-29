import unit
import game_board
import visualize
import time

cc = unit.Cc(1, (0,1))
z1 = unit.Zu(2, (4,0))
z2 = unit.Zu(3, (4,3))
z3 = unit.Zu(4, (3,1))
z4 = unit.Zu(5, (3,2))
mc = unit.Shu(6, (0,0))
zy = unit.Shu(7, (0,3))
zf = unit.Shu(8, (2,3))
hz = unit.Shu(9, (2,0))
gy = unit.Heng(10, (2,1))


all_units = [cc, z1, z2, z3, z4, mc, zy, zf, hz, gy]
new_board = game_board.Board(all_units)

visited = {}
queue = []
visited[new_board.to_string().tobytes()] = True
queue.append(new_board) 
print("start: ")
print(new_board.to_int())
start = time.time()
final_board = game_board.BFS(queue, visited)
end = time.time()
print("finished in " + str(end-start))
if final_board is None:
    print("Unsolvable")
else:
    trace = []
    temp = final_board
    while temp.parent is not None:
        trace.append(temp)
        temp = temp.parent

trace = trace[::-1]
visualize.to_image(trace, "./solutions/hengdaolima/")
visualize.to_video("./solutions/hengdaolima/", "hengdao.mp4")