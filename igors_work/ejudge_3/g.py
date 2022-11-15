def heap_add(heap, el):
    heap.append(el)
    i = len(heap) - 1
    while i > 1 and heap[i // 2] > el:
        heap[i] = heap[i // 2]
        i //= 2
        heap[i] = el

input()
a = list(map(int, input().split()))

heap = [] 
heap.append(0)
    
for el in a:
    heap_add(heap, el)
print(*heap[1:])