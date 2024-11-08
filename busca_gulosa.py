import heapq

class NodeG:
    visited = set()
    tb_caminho = {'.','L','T'}
    def __init__(self, cord, meta, pai = None):
        self.i, self.j = cord
        NodeG.visited.add(cord)
        self.heuristica = abs(self.i - meta[0]) + abs(self.j - meta[1])
        self.pai = pai
    def __repr__(self):
        return f'{(self.i, self.j)}'
    def __lt__(self, other):
        return self.heuristica < other.heuristica
    def get_cord(self):
        return (self.i, self.j)
    def eh_caminho(chave):
        return chave in NodeG.tb_caminho
    def get_pai(self):
        return self.pai
    def visitado(i, j):
        return (i, j) in NodeG.visited
    
def busca_gulosa(grid, pos_inicial, pos_tesouro):
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
        
        if i > 0 and NodeG.eh_caminho(grid[i-1][j]) and not NodeG.visitado(i-1, j):
            filho = NodeG((i - 1, j), pos_tesouro, no)
            heapq.heappush(fila, filho)
        
        
        if j < guarda_col and NodeG.eh_caminho(grid[i][j+1]) and not NodeG.visitado(i, j+1):
            filho = NodeG((i, j+1), pos_tesouro, no)
            heapq.heappush(fila, filho)
        
        
        if i < guarda_linha and NodeG.eh_caminho(grid[i+1][j]) and not NodeG.visitado(i+1, j):
            filho = NodeG((i+1, j), pos_tesouro, no)
            heapq.heappush(fila, filho)
        
        
        if j > 0 and NodeG.eh_caminho(grid[i][j-1]) and not NodeG.visitado(i, j-1):
            filho = NodeG((i, j-1), pos_tesouro, no)
            heapq.heappush(fila, filho)

mapa = [
    ['I', '.', 'L', 'L', 'L', '.', 'T'],
    ['.', '.', '.', 'L', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
]
pos_inicial = (0, 0)
pos_tesouro = (0, 6)


caminho = busca_gulosa(mapa, pos_inicial, pos_tesouro)
print(*caminho)
##print(mapa)