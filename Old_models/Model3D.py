class Pen2D():
    import numpy as np
    def __init__(self):
        self.__Position = [0,0,0]
        self.__Line = [[0,0,0]]
        self.__DirectionH = 0
        self.__DirectionV = 0
    def Move(self,Length):
        import numpy as np
        self.__Position[0] += Length * np.cos((self.__DirectionH/180) * np.pi) * np.cos((self.__DirectionV/180) * np.pi)
        self.__Position[1] += Length * np.sin((self.__DirectionH/180) * np.pi) * np.cos((self.__DirectionV/180) * np.pi)
        self.__Position[2] += Length * np.sin((self.__DirectionV/180) * np.pi)
        #print(self.__Position)
        self.__Line.append(list(self.__Position))

    def Turn(self, DegreeH, DegreeV = 0):
        self.__DirectionH += DegreeH
        if self.__DirectionH < 0:
            self.__DirectionH += (int(self.__DirectionH / -360) + 1) * 360
        else:
            self.__DirectionH = self.__DirectionH % 360
        self.__DirectionV += DegreeV
        if self.__DirectionV < 0:
            self.__DirectionV += (int(self.__DirectionV / -360) + 1) * 360
        else:
            self.__DirectionV = self.__DirectionV % 360
            
    def SetDirection(self,DirectionH, DirectionV):
        self.__DirectionH = DirectionH
        self.__DirectionV = DirectionV
    
    def Print(self):
        import numpy as np
        return np.array(self.__Line)

    def __str__(self):
        return str(self.__Position) + ';' + str(self.__Direction)

    def Moves(self,Num, dir = True):
        for num in Num:
            if dir == True:
                if num == 1:
                    self.SetDirection(-150,-54.735610317245346)
                    self.Move(10)
                elif num == 2:
                    self.SetDirection(-30,-54.735610317245346)
                    self.Move(10)
                elif num == 3:
                    self.SetDirection(90,-54.735610317245346)
                    self.Move(10)
                elif num == 4:
                    self.SetDirection(0,0)
                    self.Move(10)
                elif num == 5:
                    self.SetDirection(120,0)
                    self.Move(10)
                elif num == 6:
                    self.SetDirection(-120,0)
                    self.Move(10)
                elif num == -1:
                    self.SetDirection(30,54.735610317245346)
                    self.Move(10)
                elif num == -2:
                    self.SetDirection(-30,-54.735610317245346)
                    self.Move(-10)
                elif num == -3:
                    self.SetDirection(90,-54.735610317245346)
                    self.Move(-10)
                elif num == -4:
                    self.SetDirection(0,0)
                    self.Move(-10)
                elif num == -5:
                    self.SetDirection(120,0)
                    self.Move(-10)
                elif num == -6:
                    self.SetDirection(-120,0)
                    self.Move(-10)
                else:
                    print("!")
    def Plot(self, Depth, Type):
        if Depth == 1:
            if Type == 1:
                self.Moves([3,-5,-4])
            elif Type == 2:
                self.Moves([1,-6,-5])
            elif Type == 3:
                self.Moves([1,4,5])
            elif Type == 4:
                self.Moves([-1,3,-5])
            elif Type == 5:
                self.Moves([-4,-1,3])
            elif Type == 6:
                self.Moves([-5,-2,1])
            elif Type == -1:
                self.Moves([4,5,-3])
            elif Type == -2:
                self.Moves([5,6,-1])
            elif Type == -3:
                self.Moves([-5,-4,-1])
            elif Type == -4:
                self.Moves([5,-3,1])
            elif Type == -5:
                self.Moves([-3,1,4])
            elif Type == -6:
                self.Moves([-1,2,5])
            else:
                print("!")
        else:
            if Type == 1:
                self.Plot(Depth-1, 3)
                self.Moves([3])
                self.Plot(Depth-1, 2)
                self.Moves([-5])
                self.Plot(Depth-1, 6)
                self.Moves([-4])
                self.Plot(Depth-1, -4)
            elif Type == -1:
                self.Plot(Depth-1, 4)
                self.Moves([4])
                self.Plot(Depth-1, -6)
                self.Moves([5])
                self.Plot(Depth-1, -2)
                self.Moves([-3])
                self.Plot(Depth-1, -3)
            elif Type == 2:
                self.Plot(Depth-1, 1)
                self.Moves([1])
                self.Plot(Depth-1, 3)
                self.Moves([-6])
                self.Plot(Depth-1, 4)
                self.Moves([-5])
                self.Plot(Depth-1, -5)
            elif Type == -2:
                self.Plot(Depth-1, 5)
                self.Moves([5])
                self.Plot(Depth-1, -4)
                self.Moves([6])
                self.Plot(Depth-1, -3)
                self.Moves([-1])
                self.Plot(Depth-1, -1)
            elif Type == 3:
                self.Plot(Depth-1, 2)
                self.Moves([2])
                self.Plot(Depth-1, 1)
                self.Moves([-4])
                self.Plot(Depth-1, 5)
                self.Moves([-6])
                self.Plot(Depth-1, -6)
            elif Type == -3:
                self.Plot(Depth-1, 6)
                self.Moves([6])
                self.Plot(Depth-1, -5)
                self.Moves([4])
                self.Plot(Depth-1, -1)
                self.Moves([-2])
                self.Plot(Depth-1, -2)
            elif Type == 4:
                self.Plot(Depth-1, -6)
                self.Moves([-6])
                self.Plot(Depth-1, -1)
                self.Moves([-3])
                self.Plot(Depth-1, -5)
                self.Moves([2])
                self.Plot(Depth-1, 2)
            elif Type == -4:
                self.Plot(Depth-1, -2)
                self.Moves([-2])
                self.Plot(Depth-1, 5)
                self.Moves([3])
                self.Plot(Depth-1, 1)
                self.Moves([6])
                self.Plot(Depth-1, 6)    
            elif Type == 5:
                self.Plot(Depth-1, -4)
                self.Moves([-4])
                self.Plot(Depth-1, -2)
                self.Moves([-1])
                self.Plot(Depth-1, -6)
                self.Moves([3])
                self.Plot(Depth-1, 3)
            elif Type == -5:
                self.Plot(Depth-1, -3)
                self.Moves([-3])
                self.Plot(Depth-1, 6)
                self.Moves([1])
                self.Plot(Depth-1, 2)
                self.Moves([4])
                self.Plot(Depth-1, 4)
            elif Type == 6:
                self.Plot(Depth-1, -5)
                self.Moves([-5])
                self.Plot(Depth-1, -3)
                self.Moves([-2])
                self.Plot(Depth-1, -4)
                self.Moves([1])
                self.Plot(Depth-1, 1)
            elif Type == -6:
                self.Plot(Depth-1, -1)
                self.Moves([-1])
                self.Plot(Depth-1, 4)
                self.Moves([2])
                self.Plot(Depth-1, 3)
                self.Moves([5])
                self.Plot(Depth-1, 5)
            else:
                print("!")