points =[(1,2),(3,4),(5,6),(7,8),(-5,2),(20,4)]
distances =[]
def euclideanDistance(konum_1,konum_2):
    res =int(abs(((konum_1[0] - konum_2[0]) ** 2 + (konum_2[1] - konum_2[1]) ** 2) ** 0.5))
    if res == 0:
        return float('inf')
    return res
def Liste_Duzenleme(a):
    s_2 = set(a)
    a= list(s_2)
    a.sort()
    a.remove(float('inf'))
    return a   
distances = [euclideanDistance(a, b) for a in points for b in points]
distances= Liste_Duzenleme(distances)
print("Bu listedeki minimum mesafe :",distances[0])
print(distances)

'''
points =[(1,2),(3,4),(5,6),(7,8),(-5,2),(20,4)]
distances =[]
for a in range(len(points)):
    x = points[a][0]
    y = points[a][1]
    for b in range(len(points)):
        x1 = points[b][0]
        y1 = points[b][1]
        euclideanDistance =int(abs(((x - x1) ** 2 + (y - y1) ** 2) ** 0.5))
        if euclideanDistance == 0 :
            continue
        distances.append(euclideanDistance)
s = set(distances)
yeni = list(s)
yeni.sort()
print("Bu listedeki minimum mesafe :",yeni[0])
print(yeni)
'''
