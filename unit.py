import numpy as np

class Cc():
    def __init__(self, index, pos) :
        self.index = index
        self.pos = pos
    def place(self, board):
        pos = self.pos
        board[pos[0]: pos[0]+2, pos[1]: pos[1]+2]=self.index
    def up(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==0 or board[x-1, y]!=0 or board[x-1, y+1]!=0):
            print("up fail")
            return False
        board[x-1, y:y+2] = self.index
        board[x+1, y:y+2] = 0
        self.pos = (x-1, y)
        print("up")
        return True
    def down(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==board.shape[0]-2 or board[x+2, y]!=0 or board[x+2, y+1]!=0):
            print("down fail")
            return False
        board[x+2, y:y+2] = self.index
        board[x, y:y+2] = 0
        self.pos = (x+1, y)
        print("down")
        return True
    def left(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==0 or board[x, y-1]!=0 or board[x+1, y-1]!=0):
            print("left fail")
            return False
        board[x:x+2, y-1] = self.index
        board[x:x+2, y+1] = 0
        self.pos = (x, y-1)
        print("left")
        return True
    def right(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==board.shape[1]-2 or board[x, y+2]!=0 or board[x+1, y+2]!=0):
            print("right fail")
            return False
        board[x:x+2, y+2] = self.index
        board[x:x+2, y] = 0
        self.pos = (x, y+1)
        print("right")
        return True

class Shu():
    def __init__(self, index, pos) :
        self.index = index
        self.pos = pos
    def place(self, board):
        pos = self.pos
        board[pos[0]: pos[0]+2, pos[1]]=self.index
    def up(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==0 or board[x-1, y]!=0):
            print("up fail")
            return False
        board[x-1, y] = self.index
        board[x+1, y] = 0
        self.pos = (x-1, y)
        print("up")
        return True
    def down(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==board.shape[0]-2 or board[x+2, y]!=0):
            print("down fail")
            return False
        board[x+2, y] = self.index
        board[x, y] = 0
        self.pos = (x+1, y)
        print("down")
        return True
    def left(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==0 or board[x, y-1]!=0 or board[x+1, y-1]!=0):
            print("left fail")
            return False
        board[x:x+2, y-1] = self.index
        board[x:x+2, y] = 0
        self.pos = (x, y-1)
        print("left")
        return True
    def right(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==board.shape[1]-1 or board[x, y+1]!=0 or board[x+1, y+1]!=0):
            print("right fail")
            return False
        board[x:x+2, y+1] = self.index
        board[x:x+2, y] = 0
        self.pos = (x, y+1)
        print("right")
        return True

class Heng():
    def __init__(self, index, pos) :
        self.index = index
        self.pos = pos
    def place(self, board):
        pos = self.pos
        board[pos[0], pos[1]:pos[1]+2]=self.index
    def up(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==0 or board[x-1, y]!=0 or board[x-1, y+1]!=0):
            print("up fail")
            return False
        board[x-1, y:y+2] = self.index
        board[x, y:y+2] = 0
        self.pos = (x-1, y)
        print("up")
        return True
    def down(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==board.shape[0]-1 or board[x+1, y]!=0 or board[x+1, y+1]!=0):
            print("down fail")
            return False
        board[x+1, y:y+2] = self.index
        board[x, y:y+2] = 0
        self.pos = (x+1, y)
        print("down")
        return True
    def left(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==0 or board[x, y-1]!=0):
            print("left fail")
            return False
        board[x, y-1] = self.index
        board[x, y+1] = 0
        self.pos = (x, y-1)
        print("left")
        return True
    def right(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==board.shape[1]-2 or board[x, y+2]!=0):
            print("right fail")
            return False
        board[x, y+2] = self.index
        board[x, y] = 0
        self.pos = (x, y+1)
        print("right")
        return True

class Zu():
    def __init__(self, index, pos) :
        self.index = index
        self.pos = pos
    def place(self, board):
        pos = self.pos
        board[pos[0], pos[1]]=self.index
    def up(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==0 or board[x-1, y]!=0):
            print("up fail")
            return False
        board[x-1, y] = self.index
        board[x, y] = 0
        self.pos = (x-1, y)
        print("up")
        return True
    def down(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(x==board.shape[0]-1 or board[x+1, y]!=0):
            print("down fail")
            return False
        board[x+1, y] = self.index
        board[x, y] = 0
        self.pos = (x+1, y)
        print("down")
        return True
    def left(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==0 or board[x, y-1]!=0):
            print("left fail")
            return False
        board[x, y-1] = self.index
        board[x, y] = 0
        self.pos = (x, y-1)
        print("left")
        return True
    def right(self, board):
        x = self.pos[0]
        y = self.pos[1]
        if(y==board.shape[1]-1 or board[x, y+1]!=0):
            print("right fail")
            return False
        board[x, y+1] = self.index
        board[x, y] = 0
        self.pos = (x, y+1)
        print("right")
        return True