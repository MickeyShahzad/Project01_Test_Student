from collections import deque
import heapq

def bfs(graph, start, goal):
    # if city is not in map, instead of error just return NULL
    if start not in graph or goal not in graph:
        return [], 0, 0
    
    # current city, visisted city
    queue = deque([(start, [start])])
    # adding start in visited so doesnt cause infinit eloop by going back n forth
    visit = {start}
    nodes_expanded = 0

    # as long as there are cities to be explored, keep searching.
    while queue:
        # FIFO structure
        current, path = queue.popleft()
        nodes_expanded += 1

        # Keep track
        if current == goal:
            cost = 0
            for i in range(len(path)-1):
                cost += graph[path[i]][path[i+1]]
            return path, round(cost, 2), nodes_expanded
        
        for neighbor in graph[current]:
            if neighbor not in visit:
                visit.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return [], 0, nodes_expanded


def dfs(graph, start, goal):
    # LIFO Structure
    if start not in graph or goal not in graph:
        return [], 0, 0

    # city, path to city
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            cost = 0
            for i in range(len(path)-1):
                cost += graph[path[i]][path[i+1]]
            return path, round(cost, 2), nodes_expanded

        for neighbors in graph[current]:
            if neighbors not in visited:
                new_path = path + [neighbors]
                stack.append((neighbors, new_path))

    return [], 0, nodes_expanded



def ucs(graph, start, goal):
    if start not in graph or goal not in graph:
        return [], 0, 0

    # Priority queue stores: (total cost, current city, path)
    priority_queue = [(0, start, [start])]

    visited = set()
    nodes_expanded = 0

    while priority_queue:
        # Remove the path with the LOWEST total cost
        cost, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, round(cost, 2), nodes_expanded

        # Explore all neighboring cities
        for neighbor in graph[current]:
            if neighbor not in visited:

                # Total cost = cost so far + distance to neighbor
                new_cost = cost + graph[current][neighbor]

                # Save the path used to reach the neighbor
                new_path = path + [neighbor]

                # Add it to the priority queue
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, new_path)
                )

    # No path exists
    return [], 0, nodes_expanded



def depth_limited_search(graph, current, goal, limit, path, visited):
    # Count the current node as expanded
    nodes_expanded = 1

    # Goal found
    if current == goal:
        return path, nodes_expanded

    # Reached maximum allowed depth
    if limit == 0:
        return None, nodes_expanded

    # Explore neighbors using DFS
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)

            result, child_expanded = depth_limited_search(
                graph,
                neighbor,
                goal,
                limit - 1,
                path + [neighbor],
                visited
            )

            nodes_expanded += child_expanded

            # If the goal was found, return the path
            if result is not None:
                return result, nodes_expanded

            # Backtrack so this city can be used in another path
            visited.remove(neighbor)

    return None, nodes_expanded


def ids(graph, start, goal):
    if start not in graph or goal not in graph:
        return [], 0, 0

    total_nodes_expanded = 0

    # Try increasing depth limits: 0, 1, 2, 3, ...
    for depth in range(len(graph)):
        visited = {start}

        path, nodes_expanded = depth_limited_search(
            graph,
            start,
            goal,
            depth,
            [start],
            visited
        )

        # IDS repeats earlier searches, so add expansions
        # from every depth iteration
        total_nodes_expanded += nodes_expanded

        # Goal found
        if path is not None:
            cost = 0

            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return path, round(cost, 2), total_nodes_expanded

    # No path found
    return [], 0, total_nodes_expanded