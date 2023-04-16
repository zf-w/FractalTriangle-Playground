from LogoModel import LogoModel2D
import numpy as np


def LogoShape_4_0_10():
    model = LogoModel2D(4, 0, 10)
    line = model.getLine()
    # line = line[:20]

    import matplotlib.pyplot as plt

    half_pi = np.pi / 2
    sqrt3 = np.sqrt(3) / 2

    w = 2

    def angle(p):
        return np.arctan2(p[1], p[0])

    def degree(r):
        return 180 * r / np.pi

    def BuildLine(prev, curr, next):
        a = np.array(prev)
        b = np.array(curr)
        c = np.array(next)

        def dis(v):
            return np.power(np.dot(v, v),0.5)

        def norm(v):
            return v / dis(v)

        ba = a - b
        bc = c - b

        d = ba + bc

        l = dis(d)
        if (l <= 0.005):
            return []

        d /= l

        angle_ba = angle(ba)
        angle_bc = angle(bc)

        angle_babc = abs(angle_ba - angle_bc)
        # print(degree(angle_ba), degree(angle_bc), degree(angle_babc))

        if (angle_babc > np.pi / 3 + 0.01):
            return [b + w * sqrt3 * d, b - w * sqrt3 * d]
        else:
            return [b + w * 2 * d, b - w * d]

    # print(BuildLine([0,0], [0,1], [1,1]))
    # line = np.array([[0,0], [0,1], [1,1]])

    # plt.plot(line[:,0], line[:,1])

    line1 = [(line[0] + [0,  w])]
    line2 = [(line[0] - [w * sqrt3, w / 2])]
    angles = []
    for i in range(1, len(line) - 1):
        seg = BuildLine(line[i - 1], line[i], line[i + 1])
        if (len(seg) == 0):
            continue
        line1.append(seg[0])
        line2.append(seg[1])

    line1.append((line[-1] + [0,  w]))
    line2.append((line[-1] + [w * sqrt3, - w / 2]))

    line1 = np.array(line1)
    line2 = np.array(line2)


    def intersect(a, b, c, d):
        
        ab = b - a
        ac = c - a
        ad = d - a
        angle_ac = angle(ac) / 2
        angle_ab = angle(ab) / 2
        angle_ad = angle(ad) / 2
        abac = angle_ab - angle_ac
        if (abac > half_pi):
            abac -= np.pi
        elif (abac < -half_pi):
            abac += np.pi
        adac = angle_ad - angle_ac
        if (adac > half_pi):
            adac -= np.pi
        elif (adac < -half_pi):
            adac += np.pi
        # print(angle_ab, angle_ac, angle_ad, end=' ')
        
        # plt.plot([a[0], c[0]],[a[1], c[1]] , color="green")
        # plt.plot([b[0], d[0]],[b[1], d[1]] , color="red")
        return (abac >= 0) != (adac >= 0)

    # print(intersect(np.array([0,0]), np.array([0,1]), np.array([1,1]), np.array([1,0])))
    # print(type(intersect(np.array([0,0]), np.array([0,1]), np.array([1,1]), np.array([1,0]))))

    for i in range(1, len(line1)):
        swap = intersect(line1[i - 1], line2[i - 1], line1[i], line2[i])
        if (swap):
        
            temp = list(line1[i])
            line1[i] = line2[i]
            line2[i] = temp

    return line1, line2
    # plt.plot(line1[:, 0], line1[:, 1], color="r")
    # plt.plot(line2[:, 0], line2[:, 1], color="r")

    # plt.show()

