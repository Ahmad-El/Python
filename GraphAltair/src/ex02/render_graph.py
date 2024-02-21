import os
import networkx as nx
import nx_altair as nxa
import matplotlib.pyplot as plt
import json
from pyvis.network import Network
from dotenv import load_dotenv

load_dotenv()

FILE = os.environ.get("WIKI_FILE")
G = nx.Graph()


def read(data: dict, key=None):
    for url in data:
        link = url.split("/")[-1]
        if link is not None and key is not None:
            G.add_edge(key.split("/")[-1], link)
        read(data[url], url)


def show_simple_graph():
    for n in G.nodes():
        G.nodes[n]["name"] = str(n)

    plot = nxa.draw_networkx(G, node_tooltip="name")

    plot.save("wiki_graph.png")
    plot.save("wiki_graph.html", inline=True)


def show_advenced_graph():
    pos = nx.spring_layout(G)
    node_sizes = [10 * len(list(G.neighbors(node))) for node in G.nodes]
    labels = {node: node for node in G.nodes}
    plt.figure(figsize=(16, 12))

    nx.draw_networkx(
        G,
        pos=pos,
        node_size=node_sizes,
        cmap=plt.cm.Blues,
        node_color="blue",
        font_color="red",
        with_labels=False,
    )

    nx.draw_networkx_labels(G, pos, font_color="red", font_size=4)

    plt.savefig("wiki_graph.png")
    nt = Network(notebook=True, height="800px", width="100%")
    nt.from_nx(G)
    nt.show("wiki_graph.html")
    # plt.show()


def main():
    if os.path.exists(FILE):
        json_data = {}
        with open(FILE, "r") as file:
            json_data = json.load(file)
        read(json_data)
        show_simple_graph()
        # show_advenced_graph()
    else:
        print(f"The file {FILE} does not exist.")


if __name__ == "__main__":
    main()
