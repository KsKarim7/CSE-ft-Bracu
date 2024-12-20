import heapq

# def load_graph(filename):
#     graph = {}
#     with open(filename, 'r') as file:
#         for line in file:
#             parts = line.split()
#             source = parts[0]
#             heuristic[source] = int(parts[1])  
            
#             graph[source] = []
#             for i in range(2, len(parts), 2):
#                 destination = parts[i]
#                 distance = int(parts[i + 1])
#                 graph[source].append((destination, distance))
    
#     return graph

def load_graph(filename):
    graph = {}
    heuristic = {}
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            source = parts[0]
            heuristic[source] = int(parts[1])
            
            graph[source] = [] 
            for i in range(2, len(parts), 2):
                destination = parts[i]
                distance = int(parts[i + 1])
                graph[source].append((destination, distance))
    
    return graph, heuristic

path = []
total_cost = 0
alternatives = {}

def a_star_search(graph, heuristic, start, goal):
    open_set = [(0 + heuristic[start], start)]
    # heapq.heappush(open_set, (0 + heuristic[start], start)) 
    came_from = set()
    # g_cost = {start: 0}

    while open_set:

        total_cost, current = heapq.heappop(open_set)
        path.append(current)

        if current == goal:
            # path = []
            # while current in came_from:
            #     path.append(current)
            #     current = came_from[current]
            # path.append(start)
            # path.reverse()
            return [total_cost, path]
        
        if current in came_from:
            continue

        came_from.add(current)
        total_cost -= heuristic[current]

 
        for neighbor, distance in graph[current]:
            if neighbor in came_from:
                continue
            
            if neighbor == goal:
                alternatives[current] = (neighbor, total_cost + distance)

            f_cost = total_cost + heuristic[neighbor] + distance
            heapq.heappush(open_set, (f_cost, neighbor))
            # came_from[neighbor] = current

    return None, float('inf')  


def main():
    filename = r'K:\\BracU\\CSE422\\Lab_1\\input.txt'
    graph, heuristic = load_graph(filename)

    start = input("Enter the starting city: ")
    goal = input("Enter the destination city: ")

    if start not in graph or goal not in graph:
        print("One of the specified cities does not exist in the graph.")
        return


    final = a_star_search(graph, heuristic, start, goal)


    print(final)
    print(alternatives)

    lower = min(alternatives.values())
    print(lower)

    for k, v in alternatives.items():
        if v != lower:
            final[1].remove(k)
    
    print(final)



if __name__ == "__main__":
    main()