import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMapAO = {}
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        for n in self._nodes:
            self._idMapAO[n.object_id] = n

    def getInfoCompConnessa(self, id_oggetto):
        #cercare la componente connessa che contiene id_oggetto
        #metodo Depth_First

        if not self.hasNode(id_oggetto):
            return None

        source = self._idMapAO[id_oggetto]

        #Strategia 1
        dfsTree = nx.dfs_tree(self._graph, source)
        print("size connessa con dfs_tree", len(dfsTree.nodes()))

        #Strategia 2
        dfsPred = nx.dfs_predecessors(self._graph, source)
        print("size connessa con dfs_predecessors", len(dfsPred.values()))

        #Strategia 3
        conn = nx.node_connected_component(self._graph, source)
        print("size connessa con node_connected_component", len(conn))

        return len(conn)

    def hasNode(self, id_oggetto):
        return id_oggetto in self._idMapAO  #true (c'è) o false


    def buildGraph(self):
        #aggiunge i nodi
        self._graph.add_nodes_from(self._nodes)

        #aggiunge gli archi
        self.addEdgesV2()

    def addEgdes(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getEdgePeso(u, v)
                if peso is not None:
                    self._graph.add_edge(u, v, weight=peso)
                    print(f"Aggiunto arco tra {u} e {v} con peso {peso}.")

    def addEdgesV2(self):
        allEdges = DAO.getAllEdges(self._idMapAO)
        for e in allEdges:
            self._graph.add_edge(e.o1, e.o2, weight = e.peso)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)