class LogoModel2D():
    import numpy as np

    def _Move(self,Length):
        import numpy as np
        self.__Position[0] += Length * np.cos((self.__Direction/180) * np.pi)
        self.__Position[1] += Length * np.sin((self.__Direction/180) * np.pi)
        #print(self.__Position)
        self.__Line.append(list(self.__Position))

    def _Turn(self, Degree):
        self.__Direction += Degree
        if self.__Direction < 0:
            self.__Direction += (int(self.__Direction / -360) + 1) * 360
        else:
            self.__Direction = self.__Direction % 360
            
    def SetDirection(self,Direction):
        self.__Direction = Direction

    def _Plot(self, Depth, IsLeft, Length):
        if Depth == 1:
            self._Move(10)
            if IsLeft == True:
                self._Turn(120)
            else:
                self._Turn(-120)
            self._Move(10)
        else:
            self._Plot( Depth - 1, (IsLeft + 1) % 2, Length)
            if Depth % 2 == 0:
                if IsLeft == True:
                    self._Turn(60)
                else:
                    self._Turn(-60)
                self._Move(Length)
            else:
                self._Move(Length)
                if IsLeft == True:
                    self._Turn(60)
                else:
                    self._Turn(-60)
            self._Plot( Depth - 1, IsLeft, Length)
            if Depth % 2 == 1:
                if IsLeft == True:
                    self._Turn(60)
                else:
                    self._Turn(-60)
                self._Move(Length)
            else:
                self._Move(Length)
                if IsLeft == True:
                    self._Turn(60)
                else:
                    self._Turn(-60)
            self._Plot( Depth - 1, (IsLeft + 1) % 2, Length)

    def __init__(self, Depth, IsLeft, Length):
        self.__Position = [0,0]
        self.__Line = [[0,0]]
        self.__Direction = 0
        self._Plot(Depth, IsLeft, Length)

    def __str__(self):
        return str(self.__Position) + ';' + str(self.__Direction)

    def getLineString(self):
        to_return = ""
        for i in self.__Line:
            to_return += f"{i[0]:.3f},0.0,{i[1]:.3f}\\n"
        return to_return

    def getLine(self):
        import numpy as np
        return np.array(self.__Line)

# Pen = LogoModel2D(4,0,10)
# line = Pen.getLine()

# import matplotlib.pyplot as plt

# plt.plot(line[:,0], line[:,1])

# plt.show()