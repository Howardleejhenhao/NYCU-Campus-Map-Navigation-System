import copy
INF=1e9
 
def ObjMin(obj1, obj2):
    if obj1.distance == obj2.distance:
        if len(obj1.route) < len(obj2.route):
            return obj1
        return obj2
    if obj1.distance < obj2.distance:
        return obj1
    return obj2
 
class Obj:
    def __init__(self, distance, route: list):
        self.distance = distance
        self.route = route
    def caculate(self, Obj2, midNode:int):
        return Obj(self.distance + Obj2.distance, self.route + midNode + Obj2.route)
 
class Matrix:
    def __init__(self, length):
        self.length = length
        self.matrix = [[Obj(0, []) if  i==j else Obj(1e9,[]) for i in range(length)] for j in range(length)]
    def add_edge(self, start, end, distance):
        if start == end:
            return
        self.matrix[start][end] = ObjMin(self.matrix[start][end], Obj(distance, []))
        self.matrix[end][start] = ObjMin(self.matrix[end][start], Obj(distance, []))
    def get_distance(self, start, end):
        return self.matrix[start][end].distance
    def get_route(self, start, end):
        return self.matrix[start][end].route
 
    def output(self):
        for i in range(self.length):
            for j in range(self.length):
                print(self.matrix[i][j].distance, end=" ")
            print()
        for i in range(self.length):
            for j in range(self.length):
                print(self.matrix[i][j].route, end=" ")
            print()
    def copy(self):
        return copy.deepcopy(self)
    def multiply(self, matrix):
        result = self.copy()
        for i in range(self.length):
            for j in range(self.length):
                for k in range(self.length):
                    result.matrix[i][j] = ObjMin(result.matrix[i][j], self.matrix[i][k].caculate(matrix.matrix[k][j],[k+1]))
        return result
 
 
def readInput(): 
    #return len, matrix
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        length = int(lines[0])
        matrix = Matrix(length)
        for i in range(1, len(lines)):
            line = lines[i].split()
            for j in range(len(line)):
                if line[j] == INF: 
                    matrix.add_edge(i-1, j, 1e9)
                else:
                    matrix.add_edge(i-1, j, int(line[j]))
 
        return length, matrix
 
def outputMatrix(matrix):
    #output as the format of json
    dic = {}
    for i in range(matrix.length):
        dic[i+1] = {}
        for j in range(matrix.length):
            dic[i+1][j+1] = { "dis": matrix.get_distance(i, j), "route": [i+1] + matrix.get_route(i, j) + [j+1] }
 
    import json
    with open('output.json', 'w') as f:
        f.write(json.dumps(dic, indent=4))
        
if __name__ == "__main__":
    length, matrix = readInput() 
    result = matrix.copy()
    for i in range(10) :
        print(i)
        result = result.multiply(matrix)
        matrix = result.copy()
    outputMatrix(result)
