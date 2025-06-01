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

int is_first_small_then_second(const int a, const int b) {
    if (abs(a) < abs(b)) {
        return 1;
    } else if (abs(a) > abs(b)) {
        return 0;
    } else {
        if (a < b) return 1;
        else if (a == b) return 0;
        else return 0;
    }
}

void insert_min_abs_heap(HeapType *h, element item) {
    int i = ++(h->heap_size);
    while ((i != 1) && is_first_small_then_second(item.key, h->heap[i / 2].key)) {
        h->heap[i] = h->heap[i / 2];
        i /= 2;
    }
    h->heap[i] = item;
}

element delete_min_abs_heap(HeapType *h) {
    int parent, child;
    element item, temp;

    parent = 1;
    child = 2;
    item = h->heap[1];
    temp = h->heap[(h->heap_size)--];

    while(child <= h->heap_size) {
        if ((child < h->heap_size) && is_first_small_then_second(h->heap[child + 1].key, h->heap[child].key))
            child++;
        if (is_first_small_then_second(temp.key, h->heap[child].key)) {
            break;
        }
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
                item = delete_min_abs_heap(h);
                printf("%d\n", item.key);
            }
        } else {
            item.key = input;
            insert_min_abs_heap(h, item);
        }
    }
    free(h);
    return 0;
}