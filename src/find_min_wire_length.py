import csv


def read_data():
    file_path = "../materials/communication_wells.csv"
    graph = {}
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            well1, well2, distance = row[0].split(", ")
            if well1 not in graph:
                graph[well1] = {}
            if well2 not in graph:
                graph[well2] = {}
            graph[well1][well2] = int(distance)
            graph[well2][well1] = int(distance)
    return graph


def minimum_spanning_tree(graph):
    min_heap = [(0, "K1")]
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
    return total_distance


# def main():
#     file_path = "../materials/communication_wells.csv"
#     graph = read_data(file_path)
#     total_distance = minimum_spanning_tree(graph)
#     print("Мінімальна довжина оптоволоконного кабелю:", total_distance)
#
#
# if __name__ == "__main__":
#     main()
