from GenerateShapePath import LogoShape_4_0_10

line1, line2 = LogoShape_4_0_10()

def BoundingBox(points, box = [0,0,0,0]):
    for p in points:
        if p[0] < box[0]:
            box[0] = p[0]
        if p[0] > box[1]:
            box[1] = p[0]
        if p[1] < box[2]:
            box[2] = p[1]
        if p[1] > box[3]:
            box[3] = p[1]
    return list(box)

box = BoundingBox(line1)
box = BoundingBox(line2, box)

print(box)
def Flip1(points, center):
    for i in range(len(points)):
        # points[i][0] = center[0] - (points[i][0] - center[0])
        points[i][1] = center[1] - (points[i][1] - center[1])

def BoxToCenter(box):
    center = []
    for i in range(0, len(box), 2):
        center.append((box[i] + box[i + 1]) / 2)
    return center

center = BoxToCenter(box)
# Flip1(line1, center)
# Flip1(line2, center) 

def ApplyBoundingBox(points, box0, box1):
    ndim = int(len(box0) / 2)

    f = []
    for i in range(0, len(box0), 2):
        f.append((box1[i + 1] - box1[i]) / (box0[i + 1] - box0[i]))

    for i in range(len(points)):
        for dim in range(ndim):

            points[i][dim] = (points[i][dim] - box0[dim * 2]) * f[dim] + box1[dim * 2]
        # points[i][1] = (points[i][1] - box[2])
sqrt3_225 = pow(3, 0.5) * 225
sqrt3 = pow(3, 0.5)

graph_box = [0, 1000, 0, 1000]
tri_box = [500 - sqrt3_225, 500 + sqrt3_225, 50, 725]
geo_box = [-sqrt3, sqrt3, -1, 2]

ApplyBoundingBox(line1, box, geo_box)
ApplyBoundingBox(line2, box, geo_box)


# import svgwrite

# dwg = svgwrite.Drawing(r'Images/testsvg.svg', size=(1000, 1000))

# dwg.add(dwg.circle(center=(500, 500 ), r=490, fill='red', stroke='red'))
# dwg.add(dwg.circle(center=(500, 500 ), r=450, fill='white', stroke='white'))
# for i in range(1, len(line1)):
    
#     dwg.add(dwg.polygon([line1[i - 1], line2[i - 1], line1[i]], fill='red',  stroke='red'))
#     dwg.add(dwg.polygon([line1[i], line2[i], line2[i - 1]], fill='red',  stroke='red'))

# dwg.save()

verticeArray = []
for i in range(len(line1)):
    verticeArray += ([line1[i][0], line1[i][1], 0])
    verticeArray += ([line2[i][0], line2[i][1], 0])

indices = []
for i in range(1, len(line1)):
    j = i * 2
    indices += ([j - 2, j - 1, j])
    indices += ([j, j + 1, j - 1])

import json
file = open('Files/LogoShape.json', 'w')

json.dump({"position": verticeArray, "indices": indices}, file)

file.close()