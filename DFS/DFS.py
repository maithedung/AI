'''
Input: G = (V,E)
- V: Tap dinh
- E: Tap cung
- T0: Dinh dau
- Goal: Tap cac dinh dich
- TG: Dinh dich. TG thuoc Goal
- Bn: Dinh ke voi dinh dang xet

Output: Danh sach cac dinh da duyet tu T0 den 1 dinh TG thuoc Goal

Phuong phap: 2 danh sach mo va dong theo nguyen tac LIFO

Hint: https://www.youtube.com/watch?v=MteYIDMBXnY
'''


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': ['9'],
    '4': ['8', '10'],
    '8': [],
    '9': [],
    '10': []
}


def dfs(graph, T0, Goal):
    mo = []  # Chua cac dinh dang xet
    dong = []  # Chua cac dinh da xet

    mo.append(T0)

    while mo:
        print(f'{mo}, {dong}')
        m = mo.pop(0)
        if m in Goal:
            dong.append(m)
            print(f'{mo}, {dong}')
            return True
        for Bn in graph[m]:
            if Bn not in dong and Bn not in mo:
                mo.insert(0, Bn)
        dong.append(m)
    return False


print("Following is the Breadth-First Search")
print(dfs(graph, '5', ['9']))
