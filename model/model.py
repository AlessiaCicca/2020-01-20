import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.getRuoli=DAO.getRuoli()
        self.grafo = nx.Graph()
        self._idMap = {}

    def creaGrafo(self, ruolo):
        self.nodi = DAO.getNodi(ruolo)
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[v.artist_id] = v
        self.addEdges(ruolo)
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self, ruolo):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni(ruolo)
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)
    def analisi(self):
        lista=[]
        for arco in self.grafo.edges:
            lista.append((arco[0],arco[1],self.grafo[arco[0]][arco[1]]["weight"]))
        return sorted(lista, key=lambda x:x[2],reverse=True)
