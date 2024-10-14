import json
import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Завантаження даних з файлу cities.json
with open('cities.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cities = data['cities']
distances = data['distances']
neighbors = data['neighbors']

# Створення графа
graph = {}
for city in cities:
    graph[city] = {}
    for i, neighbor in enumerate(neighbors[city]):
        graph[city][neighbor] = distances[city][i]

def dijkstra(graph, start):
    # Ініціалізація
    queue = []
    heapq.heappush(queue, (0, start))  # (вага, місто)
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    shortest_path = {city: [] for city in graph}

    while queue:
        current_distance, current_city = heapq.heappop(queue)

        # Відзначення найкоротшого шляху
        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = shortest_path[current_city] + [current_city]
                heapq.heappush(queue, (distance, neighbor))

    return distances, shortest_path

# Знайдемо найкоротші шляхи з кожного міста
all_shortest_paths = {}
for city in cities:
    distances, paths = dijkstra(graph, city)
    all_shortest_paths[city] = {
        'distances': distances,
        'paths': {target: paths[target] + [target] for target in distances if distances[target] != float('inf') and target != city}
    }

# Виведемо результати
for city, data in all_shortest_paths.items():
    print(f"Найкоротші відстані та шляхи з {city}:")
    for target, path in data['paths'].items():
        print(f"  до {target}: відстань {data['distances'][target]}, шлях: {' -> '.join(path)}")
    print()

# Візуалізація графа
G = nx.Graph()

# Додавання ребер з вагами
for city in cities:
    for neighbor in neighbors[city]:
        weight = graph[city][neighbor]
        G.add_edge(city, neighbor, weight=weight)

# Налаштування позицій вершин
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title('Граф міст України з вагами до ребер (відстанями)')
plt.show()