from map import cities
import heapq

def get_neighbors(city):
    return cities[city]['neighbors'].keys()

def get_geo_coordinates(city):
    info = cities[city]
    return info['x'], info['y']

def get_real_distance(city1, city2):
    return cities[city1]['neighbors'][city2]

def heuristic(city, end):
    x1, y1 = get_geo_coordinates(city)
    x2, y2 = get_geo_coordinates(end)
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance


def find(start, end):
    visited = set()
    distances = {city: float('inf') for city in cities}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_city == end:
            path = []
            while current_city != start:
                path.append(current_city)
                current_city = distances[current_city][1]
            path.append(start)
            return path[::-1]

        visited.add(current_city)

        neighbors = get_neighbors(current_city)

        for neighbor in neighbors:
            if neighbor not in visited:
                distance = get_real_distance(current_city, neighbor)
                new_distance = current_distance + distance

                if new_distance < distances[neighbor]:
                    distances[neighbor] = (new_distance, current_city)
                    priority = new_distance + heuristic(neighbor, end)
                    heapq.heappush(priority_queue, (priority, neighbor))

    return []

