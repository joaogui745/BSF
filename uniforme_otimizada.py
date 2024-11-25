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
    root = (0,) + pos_inicial
    heapq.heappush(fila, root)
    antecessor[root] = None  

    linhas = len(grid)
    colunas = len(grid[0])

    while (fila):
        no = heapq.heappop(fila)
        custo, i , j = no
        cord = (i, j)

        if (no[1:]) == pos_tesouro:
            while(no):
                caminho.append(no[1:])
                no = antecessor[no]
            caminho.reverse()
            return caminho
        
        if not cord in visitados:
            visitados.add(cord)
            for oi, oj in offsets:
                ni, nj = i + oi, j + oj
                if 0 <= ni < linhas and 0 <= nj < colunas and grid[ni][nj] != '#' and not (ni, nj) in visitados:
                    novocusto = tb_custo[grid[ni][nj]] + custo
                    filho = (novocusto, ni, nj)
                    antecessor[(novocusto, ni, nj,)] = no
                    heapq.heappush(fila, filho)
    return []

    

grid = [
    ['I', '#', '.', '#', 'T'],
    ['.', 'L', 'L', 'L', '.'],
    ['.', '#', '#', '#', '.'],
    ['L', '.', 'L', '.', 'L']]

pos_inicial = (0, 0)
pos_tesouro = (0, 4)

caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)

print(caminho_bcu)