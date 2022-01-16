class Pen2D():
    import numpy as np
    def __init__(self):
        self.__Position = [0,0]
        self.__Line = [[0,0]]
        self.__Direction = 0

    def Move(self,Length):
        import numpy as np
        self.__Position[0] += Length * np.cos((self.__Direction/180) * np.pi)
        self.__Position[1] += Length * np.sin((self.__Direction/180) * np.pi)
        #print(self.__Position)
        self.__Line.append(list(self.__Position))

    def Turn(self, Degree):
        self.__Direction += Degree
        if self.__Direction < 0:
            self.__Direction += (int(self.__Direction / -360) + 1) * 360
        else:
            self.__Direction = self.__Direction % 360
            
    def SetDirection(self,Direction):
        self.__Direction = Direction
    
    def Print(self):
        import numpy as np
        return np.array(self.__Line)

    def __str__(self):
        return str(self.__Position) + ';' + str(self.__Direction)

    def Plot(self, Depth, IsLeft, Length):
        if Depth == 1:
            self.Move(10)
            if IsLeft == True:
                self.Turn(120)
            else:
                self.Turn(-120)
            self.Move(10)
        else:
            self.Plot( Depth - 1, (IsLeft + 1) % 2, Length)
            if Depth % 2 == 0:
                if IsLeft == True:
                    self.Turn(60)
                else:
                    self.Turn(-60)
                self.Move(Length)
            else:
                self.Move(Length)
                if IsLeft == True:
                    self.Turn(60)
                else:
                    self.Turn(-60)
            self.Plot( Depth - 1, IsLeft, Length)
            if Depth % 2 == 1:
                if IsLeft == True:
                    self.Turn(60)
                else:
                    self.Turn(-60)
                self.Move(Length)
            else:
                self.Move(Length)
                if IsLeft == True:
                    self.Turn(60)
                else:
                    self.Turn(-60)
            self.Plot( Depth - 1, (IsLeft + 1) % 2, Length)
    
