from typing import List, Dict, Tuple

class MinPriorityQueue:
    """
    MinPriorityQueue stores nodes ordered by lowest priority
    """
    
    def append(self, node: str, priority: int) -> None:
        pass
    
    def dequeue(self) -> str:
        # FIXME: add implementation
        return ""

def dejsktra(graph: Dict[str, List[Tuple[str, int]]], start_point: str):

    # init dist_to with infinities
    dist_to = {
        start_point: 0
    }

    for vertex in graph.items:
        dist_to[vertex] = float("inf")

    # add start point to the priority queue
    queue = MinPriorityQueue()
    queue.append(start_point, 0)
    visited = set()
    
    while queue:
        current = queue.dequeue()
        # get from list all possible available vortexes
        # from current one
        neighbour_vortexes = graph[current]
        
        for vertex, weight in neighbour_vortexes:

            # FIXME: potential issue
            if vertex in visited:
                continue
            visited.add(vertex)      
            
            # relax edge
            if (dist_to[current] + weight) < dist_to[vertex]:
                dist_to[vertex] = dist_to[current] + weight
            
            # add vortex into the queue
            queue.append(vertex, weight)


def min_path(graph, start_p, destination = None):
    """_summary_

    Args:
        graph (_type_): graph as adjastency list: [A: (B, 10), (C, 20), (F, 23) ]
        start_p (_type_): start point
        destination (_type_, optional): Destination point to search shortest path. Defaults to None.
    """
    pass