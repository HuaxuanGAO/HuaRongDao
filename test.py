import numpy as np
import unit

board = np.zeros((5,4), dtype=int)
test = unit.Zu(1, (1,1))
# test = unit.Cc(1, (1,1))
# test = unit.Heng(1, (1,1))
# test = unit.Shu(1, (1,1))
test.place(board)
print(board)
print(unit.movable_unit(board))

test.up(board)
test.up(board)
test.up(board)
test.up(board)
test.down(board)
test.down(board)
test.down(board)
test.down(board)
test.down(board)
test.down(board)
test.left(board)
test.left(board)
test.right(board)
test.right(board)
test.right(board)
test.right(board)

