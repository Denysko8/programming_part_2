import csv
from typing import Dict


def read_data(file_path:str)->Dict[str, Dict[str, int]]:
    """
    This function reads data about connections between wells from a CSV file.

    Returns:
        dict: A data structure of the graph, where each vertex is represented as a key,
        and the value is a dictionary containing neighboring vertices and distances to them.
    """
    graph = {}
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                well1, well2, distance = row[0].split(", ")
                if well1 not in graph:
                    graph[well1] = {}
                if well2 not in graph:
                    graph[well2] = {}
                graph[well1][well2] = int(distance)
                graph[well2][well1] = int(distance)
    return graph


def minimum_spanning_tree(graph):
    """
    This function finds the minimum spanning tree in the graph using a greedy algorithm.
    Args:
        graph (dict): The graph represented as a dictionary, where the keys are vertices,
        and the values are their neighbors and distances to them.
    Returns:
        int: The total distance of the minimum spanning tree.
    """
    min_heap = [(0, "K1")] if "K1" in graph else []
    visited = set()
    total_distance = 0

    while min_heap:
        distance, node = min_heap.pop(0)
        if node not in visited:
            visited.add(node)
            total_distance += distance
            for neighbor, neighbor_distance in graph[node].items():
                if neighbor not in visited:
                    min_heap.append((neighbor_distance, neighbor))
            min_heap.sort()
    if total_distance == 0:
        return -1
    return total_distance
