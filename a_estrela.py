import heapq

class NodeA:
    visited = set()
    tb_custo = {
    '.' : 1,
    'L' : 5,
    'T' : 0, 
    }
    def __init__(self, cord, meta, matrix = None, pai = None):
        self.i, self.j = cord
        NodeA.visited.add(cord)
        self.pai = pai
        self.dist = abs(self.i - meta[0]) + abs(self.j - meta[1])
        if pai:
            self.custo = pai.custo + NodeA.tb_custo[matrix[self.i][self.j]]
            self.heuristica = max(self.pai.heuristica, self.dist + self.custo)
        else: 
            self.custo = 0
            self.heuristica = self.dist
    def __repr__(self):
        return f'{(self.i, self.j)}'
    def __lt__(self, other):
        return self.heuristica < other.heuristica
    def get_cord(self):
        return (self.i, self.j)
    def get_custo(self, matrix):
        return self.custo
    def eh_caminho(chave):
        return chave in NodeA.tb_custo
    def get_pai(self):
        return self.pai
    def visitado(i, j):
        return (i, j) in NodeA.visited
    
def busca_a_estrela(grid, pos_inicial, pos_tesouro):
    caminho = []
    fila = []
    guarda_linha = len(grid) - 1
    guarda_col = len(grid[0]) - 1
    heapq.heappush(fila, NodeA(pos_inicial, pos_tesouro))

    while (fila):
        no = heapq.heappop(fila)
        i, j = no.get_cord()

        if (i, j) == pos_tesouro:
            while(no):
                caminho.append(no.get_cord())
                no = no.get_pai()
            caminho.reverse()
            return caminho
        
        if i > 0 and NodeA.eh_caminho(grid[i-1][j]) and not NodeA.visitado(i-1, j):
            filho = NodeA((i - 1, j), pos_tesouro, grid, no)
            heapq.heappush(fila, filho)
        
        
        if j < guarda_col and NodeA.eh_caminho(grid[i][j+1]) and not NodeA.visitado(i, j+1):
            filho = NodeA((i, j+1), pos_tesouro, grid, no)
            heapq.heappush(fila, filho)
        
        
        if i < guarda_linha and NodeA.eh_caminho(grid[i+1][j]) and not NodeA.visitado(i+1, j):
            filho = NodeA((i+1, j), pos_tesouro, grid, no)
            heapq.heappush(fila, filho)
        
        
        if j > 0 and NodeA.eh_caminho(grid[i][j-1]) and not NodeA.visitado(i, j-1):
            filho = NodeA((i, j-1), pos_tesouro, grid, no)
            heapq.heappush(fila, filho)

grid = [
    ['I', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '#', 'L', '.'],
    ['.', 'L', '#', 'T', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]
pos_inicial = (0, 0)
pos_tesouro = (3, 3)


caminho = busca_a_estrela(grid, pos_inicial, pos_tesouro)
print(*caminho)
##print(mapa)