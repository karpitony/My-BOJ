import sys
from dataclasses import dataclass

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E = map(int, input().split())

@dataclass
class Edge:
    start: int = None
    end: int = None
    weight: int = None

edges:Edge = list()

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append(Edge(A, B, C))

parent = [-1 for _ in range(V + 1)]

def set_find(a: int):
    if parent[a] == -1:
        return a
    parent[a] = set_find(parent[a])
    return parent[a]

def set_union(a:int, b:int) -> None:
    root1 = set_find(a)
    root2 = set_find(b)
    if root1 != root2:
        parent[root1] = root2

edges.sort(key=lambda x: x.weight)

edge_accepted = 0
uset = 0
vset = 0
total_weight = 0
for e in edges:
    uset = set_find(e.start)
    vset = set_find(e.end)
    if uset != vset:
        edge_accepted += 1
        total_weight += e.weight
        set_union(uset, vset)

print(total_weight)