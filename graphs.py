import networkx as nx

from algorithm import Result
from consts import NODE_COLORS


def plot_group_route(group_num, list_of_address_in_short_path, ax):
    G = nx.Graph()

    length = len(list_of_address_in_short_path)
    for i in range(length):
        G.add_node(i, pos=list_of_address_in_short_path[i])
    for i in range(length - 1):
        G.add_edge(i, i + 1)

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, node_color=NODE_COLORS[group_num], with_labels=True, ax=ax)

    return G


def plot_combined_route(result: Result, graphs_list, ax):
    for i in range(len(graphs_list)):
        pos = nx.get_node_attributes(graphs_list[i], 'pos')
        nx.draw(graphs_list[i], pos, node_color=NODE_COLORS[i], with_labels=True, ax=ax)

    G = nx.Graph()
    G.add_node(i, pos=result.school_point)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, node_color="y", with_labels=True, ax=ax)


def plot_group_scatter(result: Result, ax):
    x_1, y_1 = result.school_point
    ax.scatter(x_1, y_1, color='yellow', s=150)
    for i in range(len(result.clusters)):
        ax.scatter(*zip(*result.clusters[i]), color=NODE_COLORS[i])
    # ax.scatter(*zip(*result.clusters[0]), color=NODE_COLORS[0])
    # ax.scatter(*zip(*result.clusters[1]), color=NODE_COLORS[1])
    # ax.scatter(*zip(*result.clusters[2]), color=NODE_COLORS[2])
    # Add means to the image
    # center points
    ax.scatter(*zip(*result.means), color='black', s=150)
