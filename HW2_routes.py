import json

# Завантаження даних з файлу cities.json
with open('cities.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

cities = data['cities']
distances = data['distances']

# Функція для знаходження сусідів (neighbors) для певного міста
def get_neighbors(city):
    city_index = cities.index(city)
    neighbors = []
    for i in range(len(cities)):
        if i != city_index and distances[city][i] > 0:  # якщо є відстань більше нуля
            neighbors.append(cities[i])
    return neighbors

# Алгоритм BFS
def bfs(start, goal):
    visited = set()
    queue = [(start, [start])]  # Кожен елемент у черзі - кортеж (місто, шлях)

    while queue:
        current_city, path = queue.pop(0)
        if current_city == goal:
            return path

        visited.add(current_city)

        for neighbor in get_neighbors(current_city):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # Якщо шлях не знайдено

# Алгоритм DFS
def dfs(start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor in get_neighbors(start):
        if neighbor not in visited:
            result = dfs(neighbor, goal, visited, path.copy())  # використовуємо copy, щоб не змінювати поточний шлях
            if result is not None:
                return result

    return None  # Якщо шлях не знайдено

# Функція для підрахунку відстані між містами за знайденим шляхом
def calculate_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        city1_index = cities.index(path[i])
        city2_index = cities.index(path[i + 1])
        total_distance += distances[path[i]][city2_index]
    return total_distance

# Визначення міст для перевірки
cities_to_check = ['Львів', 'Харків', 'Донецьк', 'Симферопіль', 'Ужгород']

# Виведення результатів
for city in cities_to_check:
    print(f"\nШлях з Києва до {city}:")
    bfs_path = bfs('Київ', city)
    dfs_path = dfs('Київ', city)

    bfs_distance = calculate_distance(bfs_path) if bfs_path else None
    dfs_distance = calculate_distance(dfs_path) if dfs_path else None

    print(f"BFS шлях: {bfs_path}, відстань: {bfs_distance}")
    print(f"DFS шлях: {dfs_path}, відстань: {dfs_distance}")

# Порівняння результатів
print("\nПорівняння результатів:")
for city in cities_to_check:
    bfs_path = bfs('Київ', city)
    dfs_path = dfs('Київ', city)

    print(f"{city}:")
    print(f"  BFS шлях: {bfs_path}, відстань: {calculate_distance(bfs_path) if bfs_path else None}")
    print(f"  DFS шлях: {dfs_path}, відстань: {calculate_distance(dfs_path) if dfs_path else None}")

# Пояснення різниці в шляхах
print("\nВисновок:")
print("BFS (ширина) завжди знаходить найкоротший шлях у неваженому графі, тоді як DFS (глибина) може знайти більш довгі шляхи, оскільки він не обирає найкоротші маршрути спочатку, а йде в глибину до кінця.")
