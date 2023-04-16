from src.MyCanvas import Canvas
from src.ZugztriTemplate import ZugzTri
import numpy as np
import math
canvas = Canvas(900,900)

model = ZugzTri(4)

degree_start = - math.pi / 2
unit_degree = (15 / 180) * math.pi

def centerRadius(center, radius, angle):
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)

    return np.array([center[0] + x, center[1] + y])

def flip(x, point):
    return np.array([2 * x - point[0], point[1]])


center = np.array([450, 450])

def AddZugz(A, B, C):
    temp = model.Transform(A, B, C)
    for i3 in range(0, len(temp), 3):
        canvas.add(temp[i3], temp[i3 + 1], temp[i3 + 2])

for i in range(9):
    angle0 = degree_start + i * unit_degree
    angle1 = degree_start + (i + 1) * unit_degree
    p00 = centerRadius(center, 300, angle0)
    p01 = centerRadius(center, 360, angle0)
    p10 = centerRadius(center, 300, angle1)
    p11 = centerRadius(center, 360, angle1)
    f00 = flip(center[1], p00)
    f01 = flip(center[1], p01)
    f10 = flip(center[1], p10)
    f11 = flip(center[1], p11)

    AddZugz(p00,p01, p10)
    AddZugz(p11,p10, p01)
    AddZugz(f00,f01, f10)
    AddZugz(f11,f10, f01)

canvas.saveSVG(r"Images/Playground.svg")
