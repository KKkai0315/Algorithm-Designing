import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def sort_by_x(points):
    return sorted(points, key=lambda x: x[0])

def closest_pair_strip(strip, d):
    min_dist = d
    strip.sort(key=lambda x: x[1])
    n = len(strip)
    min_pair = None
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_dist:
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                min_pair = (strip[i], strip[j])
            j += 1
    return min_dist, min_pair

def closest_pair(points):
    n = len(points)
    if n <= 3:
        min_dist = float('inf')
        min_pair = None
        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    min_pair = (points[i], points[j])
        return min_dist, min_pair

    points_x = sort_by_x(points)
    mid = n // 2
    mid_point = points_x[mid]

    left_points = points[:mid]
    right_points = points[mid:]

    dl, min_pair_l = closest_pair(left_points)
    dr, min_pair_r = closest_pair(right_points)

    d = min(dl, dr)
    min_pair = min_pair_l if dl <= dr else min_pair_r

    strip = [point for point in points_x if abs(point[0] - mid_point[0]) < d]

    d_strip, min_pair_strip = closest_pair_strip(strip, d)

    if d_strip < d:
        return d_strip, min_pair_strip
    else:
        return d, min_pair

n=int(input())
points = []
for i in range(n):
    points.append((tuple(map(int,input().split()))))
closest_distance, closest_pair = closest_pair(points)
print("{:.2f}".format(closest_distance))
for (i,j) in closest_pair:
    print(i,j)
