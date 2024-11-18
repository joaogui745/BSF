import heapq

class NodeG:
    def __init__(self, cord, meta, pai = None):
        self.i, self.j = cord
        self.heuristica = abs(self.i - meta[0]) + abs(self.j - meta[1])
        self.pai = pai
    def __repr__(self):
        return f'{(self.i, self.j)}'
    def __lt__(self, other):
        return self.heuristica < other.heuristica
    def get_cord(self):
        return (self.i, self.j)
    def get_pai(self):
        return self.pai
    
def busca_gulosa(grid, pos_inicial, pos_tesouro):
    visitado = set()
    tb_caminho = {'.','L','T'}
    caminho = []
    fila = []
    guarda_linha = len(grid) - 1
    guarda_col = len(grid[0]) - 1
    heapq.heappush(fila, NodeG(pos_inicial, pos_tesouro))

    while (fila):
        no = heapq.heappop(fila)
        i, j = no.get_cord()

        if (i, j) == pos_tesouro:
            while(no):
                caminho.append(no.get_cord())
                no = no.get_pai()
            caminho.reverse()
            return caminho
        
        if i > 0 and grid[i-1][j] in tb_caminho and not (i-1, j) in visitado:
            filho = NodeG((i - 1, j), pos_tesouro, no)
            heapq.heappush(fila, filho)
        
        
        if j < guarda_col and grid[i][j+1] in tb_caminho and not (i, j+1) in visitado:
            filho = NodeG((i, j+1), pos_tesouro, no)
            heapq.heappush(fila, filho)
        
        
        if i < guarda_linha and grid[i+1][j] in tb_caminho and not (i+1, j) in visitado:
            filho = NodeG((i+1, j), pos_tesouro, no)
            heapq.heappush(fila, filho)
        
        
        if j > 0 and grid[i][j-1] in tb_caminho and not (i, j-1) in visitado:
            filho = NodeG((i, j-1), pos_tesouro, no)
            heapq.heappush(fila, filho)
        
        visitado.add((i, j))
    
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


caminho = busca_gulosa(grid, pos_inicial, pos_tesouro)
print(*caminho)
##print(mapa)