import numpy as np
import unit
import board


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
test_board = board.Board(all_units)
print(test_board.to_int())
print(test_board.to_string())