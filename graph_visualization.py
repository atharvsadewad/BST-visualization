import matplotlib.pyplot as plt
import networkx as nx
import time

# Create a sample graph
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)  # fixed layout

def draw_graph(highlight_nodes=[]):
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=800, font_size=12)
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color="yellow", node_size=800)
    plt.pause(1)  # pause for animation

def bfs(start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            draw_graph(visited)
            queue.extend([n for n in G.neighbors(node) if n not in visited])
    return visited

def dfs(start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            draw_graph(visited)
            stack.extend([n for n in G.neighbors(node) if n not in visited])
    return visited

if __name__ == "__main__":
    plt.ion()  # interactive mode on
    print("BFS Traversal Order:")
    bfs_order = bfs(1)
    print(bfs_order)

    time.sleep(2)

    print("DFS Traversal Order:")
    dfs_order = dfs(1)
    print(dfs_order)

    plt.ioff()
    plt.show()
