import heapq
import math


def haversine(lat1, lon1, lat2, lon2):
    # Earth's radius in miles
    R = 3958.8

    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def greedy_best_first(graph, locations, start, goal):
    # Check that start and goal exist
    if start not in graph or goal not in graph:
        return [], 0, 0

    # Get goal coordinates
    goal_lat = locations[goal]["lat"]
    goal_lon = locations[goal]["lon"]

    # Calculate heuristic for starting city
    start_h = haversine(
        locations[start]["lat"],
        locations[start]["lon"],
        goal_lat,
        goal_lon
    )

    # Priority queue stores:
    # (heuristic, current city, path)
    priority_queue = [(start_h, start, [start])]

    visited = set()
    nodes_expanded = 0

    while priority_queue:
        # Remove city with smallest heuristic
        heuristic, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        # Goal found
        if current == goal:
            # Calculate actual path cost
            cost = 0

            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return path, round(cost, 2), nodes_expanded

        # Explore neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:

                # Calculate straight-line distance
                # from neighbor to goal
                h = haversine(
                    locations[neighbor]["lat"],
                    locations[neighbor]["lon"],
                    goal_lat,
                    goal_lon
                )

                new_path = path + [neighbor]

                heapq.heappush(
                    priority_queue,
                    (h, neighbor, new_path)
                )

    # No route found
    return [], 0, nodes_expanded


def a_star(graph, locations, start, goal):
    # Check that start and goal exist
    if start not in graph or goal not in graph:
        return [], 0, 0

    # Get goal coordinates
    goal_lat = locations[goal]["lat"]
    goal_lon = locations[goal]["lon"]

    # Calculate heuristic for starting city
    start_h = haversine(
        locations[start]["lat"],
        locations[start]["lon"],
        goal_lat,
        goal_lon
    )

    # Priority queue stores:
    # (f = g + h, g = actual cost, current city, path)
    priority_queue = [(start_h, 0, start, [start])]

    # Best known actual cost to each city
    best_cost = {start: 0}

    nodes_expanded = 0

    while priority_queue:
        # Remove city with smallest f(n)
        f, cost, current, path = heapq.heappop(priority_queue)

        # Skip this entry if we already found
        # a cheaper way to reach this city
        if cost > best_cost.get(current, float("inf")):
            continue

        nodes_expanded += 1

        # Goal found
        if current == goal:
            return path, round(cost, 2), nodes_expanded

        # Explore neighbors
        for neighbor in graph[current]:

            # g(n): actual cost from start to neighbor
            new_cost = cost + graph[current][neighbor]

            # Only continue if this is the cheapest
            # route we've found to this neighbor
            if new_cost < best_cost.get(neighbor, float("inf")):

                best_cost[neighbor] = new_cost

                # h(n): straight-line distance
                # from neighbor to goal
                h = haversine(
                    locations[neighbor]["lat"],
                    locations[neighbor]["lon"],
                    goal_lat,
                    goal_lon
                )

                # f(n) = g(n) + h(n)
                new_f = new_cost + h

                new_path = path + [neighbor]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_cost, neighbor, new_path)
                )

    # No route found
    return [], 0, nodes_expanded