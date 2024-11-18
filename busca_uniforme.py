import heapq

class NodeU:
    tb_custo = {
    '.' : 1,
    'L' : 5,
    'T' : 0, 
    }
    def __init__(self, cord, matrix = None, pai = None):
        self.i, self.j = cord
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
    
def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    visited = set()
    caminho = []
    fila = []
    guarda_linha = len(grid) - 1
    guarda_col = len(grid[0]) - 1
    heapq.heappush(fila, NodeU(pos_inicial))
    visited.add(pos_inicial)

    while (fila):
        no = heapq.heappop(fila)
        i, j = no.get_cord()

        if (i, j) == pos_tesouro:
            while(no):
                caminho.append(no.get_cord())
                no = no.get_pai()
            caminho.reverse()
            return caminho
        
        if i > 0 and NodeU.eh_caminho(grid[i-1][j]) and not (i-1, j) in visited:
            filho = NodeU((i - 1, j), grid, no)
            visited.add(filho.get_cord)
            heapq.heappush(fila, filho)
        
        
        if j < guarda_col and NodeU.eh_caminho(grid[i][j+1]) and not (i, j+1) in visited:
            filho = NodeU((i, j+1), grid, no)
            visited.add(filho.get_cord)
            heapq.heappush(fila, filho)
        
        
        if i < guarda_linha and NodeU.eh_caminho(grid[i+1][j]) and not (i+1, j) in visited:
            filho = NodeU((i+1, j), grid, no)
            visited.add(filho.get_cord)
            heapq.heappush(fila, filho)
        
        
        if j > 0 and NodeU.eh_caminho(grid[i][j-1]) and not (i, j-1) in visited:
            filho = NodeU((i, j-1), grid, no)
            visited.add(filho.get_cord)
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