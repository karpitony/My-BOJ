#include <stdio.h>
#include <stdlib.h>
#define SIZE 100001

typedef struct {
    int key;
} element;
typedef struct {
    element heap[SIZE];
    int heap_size;
} HeapType;

HeapType* create() { return (HeapType *)malloc(sizeof(HeapType)); }
void init(HeapType *h) { h->heap_size = 0; }

void insert_max_heap(HeapType *h, element item) {
    int i;
    i = ++(h->heap_size);

    while ((i != 1) && (item.key > h->heap[i / 2].key)) {
        h->heap[i] = h->heap[i / 2];
        i /= 2;
    }
    h->heap[i] = item;
}

element delete_max_heap(HeapType *h) {
    int parent, child;
    element item, temp;

    item = h->heap[1];
    temp = h->heap[(h->heap_size)--];
    parent = 1;
    child = 2;
  
    while (child <= h->heap_size) {
        if((child < h->heap_size) && (h->heap[child].key < h->heap[child + 1].key)) {
            child++;
        }
        if(temp.key >= h->heap[child].key)
            break;
        h->heap[parent] = h->heap[child];
        parent = child;
        child *= 2;
    }
    h->heap[parent] = temp;
    return item;
}

int main(void) {
    int i, n, input;
    element item;
    HeapType* h;

    scanf("%d", &n);

    h = create();
    init(h);

    for (int i = 0; i < n; i++) {
        scanf("%d", &input);
        if (input == 0) {
            if (h->heap_size == 0)
                printf("0\n");
            else {
                item = delete_max_heap(h);
                printf("%d\n", item.key);
            }
        } else {
            item.key = input;
            insert_max_heap(h, item);
        }
    }
    free(h);
    return 0;
}