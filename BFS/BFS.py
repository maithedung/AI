'''
Input: G = (V,E)
- V: Tap dinh
- E: Tap cung
- T0: Dinh dau
- Goal: Tap cac dinh dich
- TG: Dinh dich. TG thuoc Goal
- Bn: Dinh ke voi dinh dang xet

Output: Duong di p tu T0 den 1 dinh TG thuoc Goal

Phuong phap: 2 danh sach mo va dong theo nguyen tac FIFO

Hint: https://www.youtube.com/watch?v=i4fEZlVNwVs
'''


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


def bfs(graph, T0, Goal):
    mo = []  # Chua cac dinh dang xet
    dong = []  # Chua cac dinh da xet
    p = [] # Duong di

    mo.append(T0)
    dong.append(T0)

    while mo:
        m = mo.pop(0)
        p.append(m)
        if m in Goal:
            return p

        for Bn in graph[m]:
            if Bn not in dong:
                dong.append(Bn)
                mo.append(Bn)
    return 'Khong co duong di'


print("Following is the Breadth-First Search")
print(bfs(graph, '5', ['4']))
