import svgwrite

class Canvas:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__tris = []

    def add(self, pA, pB, pC):
        self.__tris.append([pA,pB,pC])

    def saveSVG(self,path):
        dwg = svgwrite.Drawing(path, size=(self.__height, self.__width))
        for face in self.__tris:
            try:
                dwg.add(dwg.polygon(face, fill='red', stroke='red'))
            except:
                print(face)
                print(type(face[0][0]))
        
        dwg.save()
