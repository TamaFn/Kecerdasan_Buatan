

heuristik = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


d = {
         'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
         'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
         'Timisoara': [('Arad', 118), ('Lugoj', 111)],
         'Zerind': [('Arad', 75), ('Oradea', 71)],
         'Oradea': [('Zerind', 71), ('Sibiu', 151)],
         'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
         'Rimnicu': [('Sibiu', 80), ('Craivo', 146), ('Pitesti', 97)],
         'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
         'Bucharest': [('Giurgiu', 90), ('Urziceni', 85), ('Pitesti', 101), ('Fagaras', 211)],
         'Craivo': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu', 146)],
         'Pitesti': [('Rimnicu', 97), ('Craivo', 138), ('Bucharest', 101)],
         'Mehadia': [('Dobreta', 75), ('Lugoj', 70)],
         'Giurgiu': [('Bucharest', 90)],
         'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
         'Dobreta': [('Mehadia', 75), ('Craivo', 120)],
         'Hirsova' : [('Eforie', 86), ('Urziceni', 98)],
         'Vaslui' : [('Urziceni', 142), ('Lasi', 92)],
         'Eforie' : [('Hirsova', 86)],
         'Lasi': [('Neamt', 87), ('Vaslui', 92)],
         'Neamt': [('Lasi', 87)],
}


def second_index(x):
    return x[1]

def build_dict(li):
    di  = {}

    for i in li:
        name = i[0]
        cost = i[1]
        di[name] = cost
    return di

def GBFS(start, goal):
    q = []
    start_val = heuristik[start]
    q.append((start, start_val))
    explored = []
    expanded = []
    while len(q) > 0:
        node = q.pop(0)
        if node[0] not in explored:
            explored.append(node[0])
            
        if node[0] == goal:
            print('results: ', explored, ' ', expanded, ' ', len(expanded))
            return
        
        child = d[node[0]]
        for i in child:
            n_key = i[0]
            n_val = heuristik[n_key]
            n_tuple = n_key, n_val 
            if i[0] not in explored and i[0] not in build_dict(q):
                q.append(n_tuple)
        expanded.append(node[0])
        q = sorted(q, key = second_index)
    return explored, expanded,  len(expanded)


start = input("Masukkan Kota Awal : ")
goal = input("Masukkan Kota Akhir : ")
GBFS(start,goal)





















