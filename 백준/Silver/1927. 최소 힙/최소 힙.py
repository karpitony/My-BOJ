import sys
input = sys.stdin.readline

N = int(input())
heap = list()

# 힙속성 체크
def heap_top_down(n, idx):
    # 0-indexed
    left_idx = idx * 2 + 1
    right_idx = idx * 2 + 2
    smallest = idx
    
    if left_idx < n and heap[left_idx] < heap[idx]:
        smallest = left_idx
    if right_idx < n and heap[right_idx] < heap[smallest]:
        smallest = right_idx
    # top and down swap
    if smallest != idx:
        heap[idx], heap[smallest] = heap[smallest],  heap[idx]
        heap_top_down(n, smallest)

def heap_bottom_up(idx):
    while idx > 0:
        up = (idx - 1)//2
        if heap[idx] < heap[up]:
            heap[idx], heap[up] = heap[up], heap[idx]
            idx = up #heap_bottom_up(up)도 좋지만 반복문이 깔끔
        else:
            break; 

for _ in range(N):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
            print(heap.pop()) 
            heap_top_down(len(heap), 0)
    else:
        heap.append(num)
        heap_bottom_up(len(heap)-1)
        