# 🗺️ Busca Gulosa pela Melhor Escolha — Problema das Cidades da Romênia

> Implementação do algoritmo **Greedy Best-First Search** aplicado ao mapa rodoviário da Romênia, conforme apresentado em **Russell & Norvig — Inteligência Artificial: Uma Abordagem Moderna** (Figuras 3.2 e 3.22).

---

## 📖 O que é a Busca Gulosa?

A **Busca Gulosa pela Melhor Escolha** (*Greedy Best-First Search*) é um algoritmo de busca informada que utiliza uma **função heurística `h(n)`** para guiar a exploração do espaço de estados. A ideia central é sempre expandir o nó que parece estar **mais próximo do objetivo**, segundo a estimativa da heurística — daí o nome "gulosa": ela toma a melhor decisão *local* a cada passo, sem olhar para trás.

### Função de avaliação

```
f(n) = h(n)
```

Onde `h(n)` é a **distância em linha reta** (em km) entre a cidade `n` e o destino — Bucareste. Esse valor é retirado diretamente da **Figura 3.22** do livro.

### Características principais

| Propriedade       | Busca Gulosa                         |
|-------------------|--------------------------------------|
| **Completa?**     | Não (pode entrar em ciclos)          |
| **Ótima?**        | Não (não garante o menor custo)      |
| **Complexidade**  | O(b^m) no pior caso                  |
| **Guiada por**    | Apenas `h(n)` — ignora o custo real  |

> ⚠️ A busca gulosa **não considera o custo acumulado do caminho** (`g(n)`). Isso significa que ela pode encontrar uma rota rapidamente, mas não necessariamente a mais curta ou eficiente.

---

## 🗺️ O Problema: Romênia de Arad até Bucareste

O problema clássico do livro consiste em encontrar um caminho entre as cidades romenas **Arad** (ponto de partida) e **Bucareste** (destino). O mapa utilizado é o da **Figura 3.2** do livro, com as conexões entre cidades.

### Heurística utilizada (Figura 3.22)

A heurística `h(n)` representa a distância em linha reta de cada cidade até Bucareste:

| Cidade           | h(n) — dist. até Bucareste (km) |
|------------------|----------------------------------|
| Arad             | 366                              |
| Sibiu            | 253                              |
| Rimnicu Vilcea   | 193                              |
| Fagaras          | 176                              |
| Bucareste        | 0                                |
| *(demais cidades)* | *(ver código)*                 |

---

## 🐍 Código Python — Explicação Passo a Passo

### Estruturas de dados

```python
heuristica_bucareste = {
    'Arad': 366,
    'Bucareste': 0,
    ...
}
```

Dicionário que armazena o valor `h(n)` de cada cidade. Os valores são fixos e representam a distância em linha reta até Bucareste, conforme a **Figura 3.22** do livro. Note que `h('Bucareste') = 0`, pois já estamos no destino.

```python
grafo_romenia = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    ...
}
```

Dicionário que representa o **grafo não ponderado** do mapa rodoviário (Figura 3.2). Cada chave é uma cidade, e o valor é a lista de cidades vizinhas diretamente conectadas por estrada. Note que, na busca gulosa, **os custos das estradas não são utilizados** — apenas a heurística importa.

---

### A função `busca_gulosa`

#### 1. Inicialização da fronteira

```python
fronteira = []
heapq.heappush(fronteira, (heuristica[inicio], inicio, [inicio]))
```

A **fronteira** é uma **fila de prioridade mínima** (*min-heap*), implementada com o módulo `heapq`. Cada elemento é uma tupla com três componentes:

- `heuristica[inicio]` → o valor `h(n)` da cidade inicial (prioridade)
- `inicio` → o nome da cidade atual
- `[inicio]` → o caminho percorrido até aqui (começa com a cidade de origem)

O nó com **menor `h(n)`** sempre será extraído primeiro — este é o princípio guloso.

#### 2. Controle de visitados

```python
visitados = set()
```

Um conjunto que registra as cidades já expandidas. Isso evita que o algoritmo processe a mesma cidade duas vezes e entre em ciclos infinitos.

#### 3. Loop principal

```python
while fronteira:
    valor_h, atual, caminho = heapq.heappop(fronteira)
```

Enquanto houver cidades na fronteira, o algoritmo extrai a cidade com o **menor valor heurístico `h(n)`**. As três variáveis recebem:

- `valor_h` → o valor `h(n)` da cidade (usado apenas para a prioridade)
- `atual` → o nome da cidade sendo expandida
- `caminho` → a lista de cidades percorridas até aqui

#### 4. Teste de objetivo

```python
if atual == objetivo:
    return caminho
```

Se a cidade extraída for Bucareste, o caminho foi encontrado e é retornado imediatamente.

#### 5. Expansão dos vizinhos

```python
visitados.add(atual)

for vizinho in grafo[atual]:
    if vizinho not in visitados:
        novo_caminho = list(caminho)
        novo_caminho.append(vizinho)
        heapq.heappush(fronteira, (heuristica[vizinho], vizinho, novo_caminho))
```

A cidade atual é marcada como visitada. Em seguida, para cada vizinho ainda não visitado:

1. Cria-se uma cópia do caminho atual com o vizinho adicionado ao final
2. O vizinho é inserido na fronteira com sua prioridade sendo **apenas `h(vizinho)`**

> 💡 Observe que o **custo real do caminho é completamente ignorado** nesta etapa. Não há soma de distâncias de estrada — a decisão é tomada exclusivamente pela proximidade estimada ao destino.

---

### Bloco principal

```python
if __name__ == "__main__":
    origem = 'Arad'
    destino = 'Bucareste'

    caminho_encontrado = busca_gulosa(grafo_romenia, heuristica_bucareste, origem, destino)
    print(" -> ".join(caminho_encontrado))
```

Define origem e destino, executa o algoritmo e exibe o caminho encontrado no formato `Cidade1 -> Cidade2 -> ... -> Bucareste`.

---

## 🔍 Caminho Encontrado

A execução da busca gulosa a partir de Arad produz o seguinte trajeto:

```
Arad → Sibiu → Fagaras → Bucareste
```

Este caminho é encontrado rapidamente porque a heurística guia o algoritmo de forma direta. Contudo, **não é o caminho de menor custo real** — para isso, seria necessário usar o A\*.

---

## 📚 Referência

> Russell, S., & Norvig, P. (2022). *Inteligência Artificial: Uma Abordagem Moderna* (4ª ed.). Capítulo 3 — Solução de Problemas por Busca. Figuras 3.2 e 3.22.
