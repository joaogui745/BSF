import heapq

class NodeU:
    visited = set()
    tb_custo = {
    '.' : 1,
    'L' : 5,
    'T' : 0, 
    }
    def __init__(self, cord, matrix = None, pai = None):
        self.i, self.j = cord
        NodeU.visited.add(cord)
        self.pai = pai
        if pai:
            self.custo = pai.custo + NodeU.tb_custo[matrix[self.i][self.j]]
        else: 
            self.custo = 0
    def __repr__(self):
        return f'{(self.i, self.j)}'
    def __lt__(self, other):
        return self.custo < other.custo
    def get_cord(self):
        return (self.i, self.j)
    def get_custo(self, matrix):
        return self.custo
    def eh_caminho(chave):
        return chave in NodeU.tb_custo
    def get_pai(self):
        return self.pai
    def visitado(i, j):
        return (i, j) in NodeU.visited
    
def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    caminho = []
    fila = []
    guarda_linha = len(grid) - 1
    guarda_col = len(grid[0]) - 1
    heapq.heappush(fila, NodeU(pos_inicial))

    while (fila):
        no = heapq.heappop(fila)
        i, j = no.get_cord()

        if (i, j) == pos_tesouro:
            while(no):
                caminho.append(no.get_cord())
                no = no.get_pai()
            caminho.reverse()
            return caminho
        
        if i > 0 and NodeU.eh_caminho(grid[i-1][j]) and not NodeU.visitado(i-1, j):
            filho = NodeU((i - 1, j), grid, no)
            heapq.heappush(fila, filho)
        
        
        if j < guarda_col and NodeU.eh_caminho(grid[i][j+1]) and not NodeU.visitado(i, j+1):
            filho = NodeU((i, j+1), grid, no)
            heapq.heappush(fila, filho)
        
        
        if i < guarda_linha and NodeU.eh_caminho(grid[i+1][j]) and not NodeU.visitado(i+1, j):
            filho = NodeU((i+1, j), grid, no)
            heapq.heappush(fila, filho)
        
        
        if j > 0 and NodeU.eh_caminho(grid[i][j-1]) and not NodeU.visitado(i, j-1):
            filho = NodeU((i, j-1), grid, no)
            heapq.heappush(fila, filho)

grid = [
    ['I', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '#', '#', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '#', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '#', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '#', 'T'],
    ['.', '#', '#', '.', '#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '#', '.', '#', '.', '.', '.'],
]
pos_inicial = (0, 0)
pos_tesouro = (6, 9)


caminho = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)
print(*caminho)
#print(mapa)