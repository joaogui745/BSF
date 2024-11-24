import heapq
def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    visitados = set()
    fila = []  
    antecessor = {} 
    caminho = []
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    tb_custo = {
    '.' : 1,
    'L' : 5,
    'T' : 0, 
    }
    root = pos_inicial + (0,)
    heapq.heappush(fila, root)
    antecessor[root] = None  

    linhas = len(grid)
    colunas = len(grid[0])

    while (fila):
        no = heapq.heappop(fila)
        i , j, custo = no
        cord = (i, j)

        if (no[0:2]) == pos_tesouro:
            while(no):
                caminho.append(no[0:2])
                no = antecessor[no]
            caminho.reverse()
            return caminho
        
        if not cord in visitados:
            visitados.add(cord)
            for oi, oj in offsets:
                ni, nj = i + oi, j + oj
                if 0 <= ni < linhas and 0 <= nj < colunas and grid[ni][nj] != '#' and not (ni, nj) in visitados:
                    novocusto = tb_custo[grid[ni][nj]] + custo
                    filho = (ni, nj, novocusto)
                    antecessor[(ni, nj, novocusto)] = no
                    heapq.heappush(fila, filho)
    return []

    

grid = [
    ['I', '#', '.', '#', 'L', 'L', 'T'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.'],
]

pos_inicial = (0, 0)
pos_tesouro = (0, 6)

caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)

print(caminho_bcu)