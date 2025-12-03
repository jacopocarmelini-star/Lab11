import networkx as nx
from database import dao
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._id_map = {}
        self._lista_rifugi = []


    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        self.G.clear()
        self._id_map.clear()
        self._lista_rifugi.clear()

        self._lista_rifugi = DAO.get_rifugio()
        for rifugio in self._lista_rifugi:
            self._id_map[rifugio.id] = rifugio

        #self.G.add_nodes_from(self._lista_rifugi)

        connessioni = DAO.get_connessione()
        for c in connessioni:
            if c.anno <= year:
                if c.id_rifugio1 in self._id_map and c.id_rifugio2 in self._id_map:
                    r1 = self._id_map[c.id_rifugio1]
                    r2 = self._id_map[c.id_rifugio2]
                    self.G.add_edge(r1, r2)


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO
        return list(self.G.nodes())

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO
        return self.G.degree(node)

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return nx.number_connected_components(self.G)

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO
        albero = nx.bfs_tree(self.G, start)
        lista_nodi = list(albero.nodes())

        if start in lista_nodi:
            lista_nodi.remove(start)
        return lista_nodi




