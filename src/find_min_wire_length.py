import csv
from typing import Dict
from src.binary_tree_priority_queue import PriorityQueue


def read_data(file_path: str) -> Dict[str, Dict[str, int]]:
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
        int: The total distance of the minimum spanning tree, or -1 if the graph is not connected.
    """
    priority_queue = PriorityQueue()
    visited = set()
    total_distance = 0

    start_vertex = next(iter(graph.keys())) if graph else None

    if start_vertex:
        priority_queue.insert(start_vertex, 0)

    while priority_queue.root:
        node = priority_queue.remove()
        distance, current_node = node.priority, node.value
        if current_node not in visited:
            visited.add(current_node)
            total_distance += distance
            for neighbor, neighbor_distance in graph[current_node].items():
                if neighbor not in visited:
                    priority_queue.insert(neighbor, neighbor_distance)

    if total_distance == 0:
        return -1
    return total_distance
