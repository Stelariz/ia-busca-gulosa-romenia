import heapq

# Valores da heurística de distância em linha reta até Bucareste (Figura 3.22 do livro).
heuristica_bucareste = {
    'Arad': 366,
    'Bucareste': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# Mapa rodoviário simplificado da Romênia (Figura 3.2 do livro).
grafo_romenia = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Bucareste': ['Fagaras', 'Giurgiu', 'Pitesti', 'Urziceni'],
    'Craiova': ['Drobeta', 'Pitesti', 'Rimnicu Vilcea'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Eforie': ['Hirsova'],
    'Fagaras': ['Bucareste', 'Sibiu'],
    'Giurgiu': ['Bucareste'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Neamt': ['Iasi'],
    'Oradea': ['Sibiu', 'Zerind'],
    'Pitesti': ['Bucareste', 'Craiova', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Craiova', 'Pitesti', 'Sibiu'],
    'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Urziceni': ['Bucareste', 'Hirsova', 'Vaslui'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Zerind': ['Arad', 'Oradea']
}

def busca_gulosa(grafo, heuristica, inicio, objetivo):
    """
    Algoritmo de Busca Gulosa pela Melhor Escolha.
    A seleção do próximo nó a ser expandido baseia-se exclusivamente no menor valor da heurística h(n).
    """
    # A fronteira é uma fila de prioridade (min-heap) 
    # Ela armazena tuplas no formato: (valor_da_heuristica, nó_atual, caminho_percorrido)
    fronteira = []
    heapq.heappush(fronteira, (heuristica[inicio], inicio, [inicio]))
    
    visitados = set()
    
    while fronteira:
        # Retira da fronteira o nó com o menor valor heurístico
        valor_h, atual, caminho = heapq.heappop(fronteira)
        
        # Verifica se o nó atual é o objetivo (Bucareste)
        if atual == objetivo:
            return caminho
            
        visitados.add(atual)
        
        # Expande para os vizinhos do nó atual
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                # O custo real do passo (g(n)) é ignorado na busca gulosa.
                # Apenas a distância estimada até o destino (h(n)) dita a prioridade.
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                heapq.heappush(fronteira, (heuristica[vizinho], vizinho, novo_caminho))
                
    return None

if __name__ == "__main__":
    origem = 'Arad'
    destino = 'Bucareste'
    
    print(f"Iniciando a Busca Gulosa de {origem} para {destino}...\n")
    caminho_encontrado = busca_gulosa(grafo_romenia, heuristica_bucareste, origem, destino)
    
    if caminho_encontrado:
        print("Caminho encontrado:")
        print(" -> ".join(caminho_encontrado))
    else:
        print("Nenhum caminho foi encontrado.")