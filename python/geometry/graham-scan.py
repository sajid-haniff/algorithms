from math import atan2
import random


# Given three points {s_k-1, s_k, s_k+1}, return whether the connection s_k-1->s_k->s_k+1 counter clockwise.
def counter_clockwise(p1, p2, p3):
    """Is the turn counter-clockwise?"""
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])


def polar_angle(ref, point):
    """Find the polar angle of a point relative to a reference point"""
    return atan2(point[1] - ref[1], point[0] - ref[0])


# Given a 'gift' S (list of points (x,y)), return all the points that construct a convex hull for the gift.
# The convex hull will be a subset of the gift.
def graham_scan(gift):
    gift = list(set(gift))  # remove duplicates
    start = min(gift, key=lambda p: (p[1], p[0]))
    gift.remove(start)

    s = sorted(gift, key=lambda point: polar_angle(start, point))  # soft based on increasing polar angle
    hull = [start, s[0], s[1]]

    # Remove points from hull that make the hull concave
    # NOTE: In this implementation, we treat 'pt' as s_k+1.
    for pt in s[2:]:
        while not counter_clockwise(hull[-2], hull[-1], pt):
            hull.pop()  # if the three points form a clockwise rotation, delete the middle point from the hull (s_k).
        hull.append(pt)

    return hull


# Helper method. Given an integer n, return a list of points containing random points (x,y), where
# x = random integer (0-n), y = random integer (0-n).
def create_random_points(n):
    point_list = []

    for i in range(n):
        point_list.append((int(random.uniform(0, n)), int(random.uniform(0, n))))

    return point_list


def main():
    points = create_random_points(100)
    hull = graham_scan(points)
    print(hull)


if __name__ == "__main__":
    main()
