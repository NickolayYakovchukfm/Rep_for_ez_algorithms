class Solution:
    def isReflected(self, points):
        if len(points) == 0:
            return True
        coordinates_of_symmetry_point = max(points, key=lambda x: x[0])[0] + min(points, key=lambda x: x[0])[0]
        symmetry_point = coordinates_of_symmetry_point / 2
        list_of_points = list()
        list_of_reflected_points = list()
        for a, b in points:
            if a > symmetry_point:
                list_of_points.append((a, b))
            elif a < symmetry_point:
                list_of_reflected_points.append((coordinates_of_symmetry_point - a, b))
        if list_of_reflected_points == list_of_points:
            return True
        else:
            return False
