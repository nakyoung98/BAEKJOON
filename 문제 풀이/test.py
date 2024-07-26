import math
from typing import List, Tuple


def calculate_distances(
    points: List[Tuple[int, int]]
) -> List[Tuple[Tuple[int, int], float]]:
    n = len(points)
    distance_sums = []
    for i, point in enumerate(points):
        distance_sum = 0
        for j, other_point in enumerate(points):
            if i != j:
                dx = point[0] - other_point[0]
                dy = point[1] - other_point[1]
                distance_sum += math.sqrt(dx**2 + dy**2)
        distance_sums.append((point, distance_sum))
    return distance_sums


def sort_points_by_proximity(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    distance_sums = calculate_distances(points)
    sorted_points = sorted(distance_sums, key=lambda x: x[1])
    return [point for point, _ in sorted_points]


# 테스트
test_points = [(1, 1), (5, 4), (3, 3)]
result = sort_points_by_proximity(test_points)
print(result)
