import json
import networkx as nx
import matplotlib.pyplot as plt

# Завантаження даних з файлу cities.json
with open('cities.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cities = data["cities"]
neighbors = data["neighbors"]

# Створення графа
G = nx.Graph()

# Додавання вершин (міст)
for city in cities:
    G.add_node(city)

# Додавання ребер (сусідніх міст)
for city, neighbor_list in neighbors.items():
    for neighbor in neighbor_list:
        G.add_edge(city, neighbor)

# Візуалізація графа
plt.figure(figsize=(15, 10))
nx.draw_networkx(G, with_labels=True, node_color='skyblue', node_size=700, font_size=10, font_weight='bold')
plt.title("Граф міст України", fontsize=15)
plt.show()

# Аналіз основних характеристик графа
print(f"Кількість вершин (міст): {G.number_of_nodes()}")
print(f"Кількість ребер (зв'язків): {G.number_of_edges()}")

# Ступінь кожної вершини
degrees = dict(G.degree())
print("\nСтупінь вершин (міст):")
for city, degree in degrees.items():
    print(f"{city}: {degree}")
