import numpy as np
import matplotlib.pyplot as plt
def ZugzTriTemplate(N = 3):

    templateList = []

    def AddFace(A, B, C):
        nonlocal templateList
        templateList += [A[0], A[1], B[0], B[1], C[0], C[1]]

    def Vect2DirectRatioPoint(A, B, r = 1 / 3):
        A = np.array(A)
        B = np.array(B)
        AB = B - A

        return AB * r + A

    def Vect2MidPoint(A, B):
        A = np.array(A)
        B = np.array(B)
        
        return (A + B) / 2

    def helper(n, A, B, C):
        
        A = np.array(A)
        B = np.array(B)
        C = np.array(C)


        unitHalfRatio = 0.5 / (pow(2, n) - 1)

        ABcenter = Vect2MidPoint(A, B)
        BCcenter = Vect2MidPoint(B, C)
        CAcenter = Vect2MidPoint(C, A)

        ab = (B - A) * unitHalfRatio
        bc = (C - B) * unitHalfRatio
        ca = (A - C) * unitHalfRatio

        AB0 = ABcenter - ab
        AB1 = ABcenter + ab
        BC0 = BCcenter - bc
        BC1 = BCcenter + bc
        CA0 = CAcenter - ca
        CA1 = CAcenter + ca

        linkRatio = unitHalfRatio

        ab0 = Vect2DirectRatioPoint(AB0, CA1, linkRatio)
        ab1 = Vect2DirectRatioPoint(AB1, BC0, linkRatio)
        bc0 = Vect2DirectRatioPoint(BC0, AB1, linkRatio)
        bc1 = Vect2DirectRatioPoint(BC1, CA0, linkRatio)

        if (n == 1):
            AddFace(A, B, C)
            return
        
        helper(n - 1, A, CA1, AB0)
        AddFace(AB1, ab0, AB0)
        AddFace(ab1, AB1, ab0)
        helper(n - 1, AB1, B, BC0)
        AddFace(bc0, BC0, BC1)
        AddFace(bc1, BC1, bc0)
        helper(n - 1, BC1, CA0, C)
    
    A = np.array([1,0])
    B = np.array([0,0])
    C = np.array([0,1])

    helper(N, A, B, C)

    return templateList


class ZugzTri:

    def CaluculateNormal(A, B, C):
        AB = B - A
        AC = C - A

        n = np.cross(AB, AC)
        n /= pow(np.dot(n, n), 0.5)
        return n

    def IsCounterClockwise(A, B, C, n):
        AB = B - A
        AC = C - A
        cross = np.cross(AB, AC)

        return np.dot(n, cross) < 0

    def __init__(self, N):
        self.__template = ZugzTriTemplate(N)

    def Transform(self, A, B, C):
        BA = A - B
        BC = C - B

        to_return = []

        for i6 in range(0, len(self.__template), 6):
            A1 = B + BA * self.__template[i6 + 0] + BC * self.__template[i6 + 1]
            B1 = B + BA * self.__template[i6 + 2] + BC * self.__template[i6 + 3]
            C1 = B + BA * self.__template[i6 + 4] + BC * self.__template[i6 + 5]

            to_return.append(A1)
            to_return.append(B1)
            to_return.append(C1)
        
        return to_return

# a = ZugzTri(3)

# sqrt3 = pow(3, 0.5)

# A = np.array([0,2])
# B = np.array([-sqrt3, 0])
# C = np.array([sqrt3, 0])
# temp = a.Transform(A, B, C)

# for i3 in range(0,len(temp), 3):
#     plt.plot([temp[i3][0], temp[i3 + 1][0], temp[i3 + 2][0], temp[i3][0]], [temp[i3][1], temp[i3 + 1][1], temp[i3 + 2][1], temp[i3][1]])
# plt.show()