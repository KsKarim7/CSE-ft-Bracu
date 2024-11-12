# import heapq

# # Define the heuristic values for each city to Bucharest
# heuristic = {
#     "Arad": 366,
#     "Mehadia": 241,
#     "Bucharest": 0,
#     "Neamt": 234,
#     "Craiova": 160,
#     "Oradea": 380,
#     "Eforie": 161,
#     "Pitesti": 100,
#     "Fagaras": 176,
#     "Rimnicu Vilcea": 193,
#     "Dobreta": 242,
#     "Timisoara": 329,
#     "Hirsova": 151,
#     "Urziceni": 80,
#     "Iasi": 226,
#     "Vaslui": 199,
#     "Lugoj": 244,
#     "Zerind": 374
# }

# heuristic = {'Arad': 366, 'Craiova': 160, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Mehadia': 241, 'Neamt': 234, 'Sibiu': 253, 'Oradea': 380, 'Pitesti': 100, 'RimnicuVilcea': 193, 'Dobreta': 242, 'Hirsova': 151, 'lasi': 226, 'Lugoj': 244, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374, 'Bucharest': 0}
    # graph = {'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)], 'Craiova': [('Dobreta', 120), ('RimnicuVilcea', 146), ('Pitesti', 138)], 'Eforie': [('Hirsova', 86)], 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)], 'Giurgiu': [('Bucharest', 90)], 'Mehadia': [('Lugoj', 70), ('Dobreta', 75)], 'Neamt': [('lasi', 87)], 'Sibiu': [('Oradea', 151), ('Arad', 140), ('RimnicuVilcea', 80), ('Fagaras', 99)], 'Oradea': [('Zerind', 71), ('Sibiu', 151)], 'Pitesti': [('RimnicuVilcea', 97), ('Craiova', 138), ('Bucharest', 101)], 'RimnicuVilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)], 'Dobreta': [('Mehadia', 75), ('Craiova', 120)], 'Hirsova': [('Urziceni', 98), ('Eforie', 86)], 'lasi': [('Vaslui', 92), ('Neamt', 87)], 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)], 'Timisoara': [('Arad', 118), ('Lugoj', 111)], 'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)], 'Vaslui': [('Urziceni', 142), ('lasi', 92)], 'Zerind': [('Oradea', 71), ('Arad', 75)], 'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)]}

# # def load_graph(filename):
# #     graph = {}
# #     with open(filename, 'r') as file:
# #         for line in file:
# #             parts = line.split()
# #             source, destination = parts[0], parts[1]
# #             distance = int(parts[2])

# #             if source not in graph:
# #                 graph[source] = []
# #             if destination not in graph:
# #                 graph[destination] = []
# #             graph[source].append((destination, distance))
# #             graph[destination].append((source, distance))

# #     return graph


# def a_star_search(graph, heuristic, start, goal):
#     open_set = []
#     heapq.heappush(open_set, (0 + heuristic[start], start)) 
#     came_from = {}
#     g_cost = {start: 0}

#     while open_set:

#         _, current = heapq.heappop(open_set)


#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             path.reverse()
#             return path, g_cost[goal]

 
#         for neighbor, distance in graph[current]:
#             tentative_g_cost = g_cost[current] + distance

#             if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
#                 g_cost[neighbor] = tentative_g_cost
#                 f_cost = tentative_g_cost + heuristic[neighbor]
#                 heapq.heappush(open_set, (f_cost, neighbor))
#                 came_from[neighbor] = current

#     return None, float('inf')  


# def main():
#     filename = r'K:\\BracU\\CSE422\\Lab_1\\input.txt'
#     # graph = load_graph(filename)
#     graph = {'A': [('C', 118), ('E', 140), ('B', 75)], 'B': [('A', 75)], 'C': [('D', 11), ('A', 118)], 'D': [('C', 11)], 'E': [('G', 80), ('F', 99), ('A', 140)], 'F': [('I', 211), ('E', 99)], 'G': [('H', 97), ('E', 80)], 'H': [('I', 101), ('G', 97)], 'I': [('H', 101), ('F', 211)]}
#     # print(graph)
    

#     start = input("Enter the starting city: ")
#     goal = input("Enter the destination city: ")


#     if start not in graph or goal not in graph:
#         print("One of the specified cities does not exist in the graph.")
#         return


#     path, cost = a_star_search(graph, heuristic, start, goal)


#     if path:
#         print("Optimal path:", " -> ".join(path))
#         print("Total cost:", cost)
#     else:
#         print("No path found between the cities.")


# if __name__ == "__main__":
#     main()



import heapq

# Define the heuristic values for each city to Bucharest
heuristic = {
    "Arad": 366,
    "Mehadia": 241,
    "Bucharest": 0,
    "Neamt": 234,
    "Craiova": 160,
    "Oradea": 380,
    "Eforie": 161,
    "Pitesti": 100,
    "Fagaras": 176,
    "Rimnicu Vilcea": 193,
    "Dobreta": 242,
    "Timisoara": 329,
    "Hirsova": 151,
    "Urziceni": 80,
    "Iasi": 226,
    "Vaslui": 199,
    "Lugoj": 244,
    "Zerind": 374
}

# Load graph data from a file
def load_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            source, destination = parts[0], parts[1]
            distance = int(parts[2])

            if source not in graph:
                graph[source] = []
            if destination not in graph:
                graph[destination] = []

            # Add the edges in both directions since it's an undirected graph
            graph[source].append((destination, distance))
            graph[destination].append((source, distance))

    return graph

# A* Search Algorithm
def a_star_search(graph, heuristic, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], start))  # (f(n), city)
    came_from = {}
    g_cost = {start: 0}

    while open_set:
        # Get the node with the lowest f(n) = g(n) + h(n)
        _, current = heapq.heappop(open_set)

        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]

        # Check each neighbor of the current node
        for neighbor, distance in graph[current]:
            tentative_g_cost = g_cost[current] + distance

            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_set, (f_cost, neighbor))
                came_from[neighbor] = current

    return None, float('inf')  # Return None if there's no path

# Main function to execute the A* search
def main():
    filename = 'input.txt'
    graph = load_graph(filename)
    
    # User input for start and goal cities
    start = input("Enter the starting city: ")
    goal = input("Enter the destination city: ")

    # Check if start and goal are in the graph
    if start not in graph or goal not in graph:
        print("One of the specified cities does not exist in the graph.")
        return

    # Run A* search
    path, cost = a_star_search(graph, heuristic, start, goal)

    # Output result
    if path:
        print("Optimal path:", " -> ".join(path))
        print("Total cost:", cost)
    else:
        print("No path found between the cities.")

# Run the main function
if __name__ == "__main__":
    main()
