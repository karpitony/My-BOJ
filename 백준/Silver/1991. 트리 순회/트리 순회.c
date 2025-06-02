#include <stdio.h>
#include <stdlib.h>
#define SIZE 26

typedef struct TreeNode {
    char data;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode nodes[SIZE];

TreeNode* getNode(char c) {
    if (c == '.') 
        return NULL;
    return &nodes[c - 'A'];
}

// 전위 순회 출력
void preorder(TreeNode *node) {
    printf("%c", node->data);
    if (node->left != NULL)
        preorder(node->left);
    if (node->right != NULL)
        preorder(node->right);
}

// 중위 순회
void inorder(TreeNode *node) {
    if (node->left != NULL)
        inorder(node->left);
    printf("%c", node->data);
    if (node->right != NULL)
        inorder(node->right);
}

// 후위 순회
void postorder(TreeNode *node) {
    if (node->left != NULL)
        postorder(node->left);
    if (node->right != NULL)
        postorder(node->right);
    printf("%c", node->data);
}

int main(void) {
    int N;
    char value, left, right;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf(" %c %c %c", &value, &left, &right);
        nodes[value - 'A'].data = value;
        nodes[value - 'A'].left = getNode(left);
        nodes[value - 'A'].right = getNode(right);
    }

    preorder(&nodes[0]);
    printf("\n");

    inorder(&nodes[0]);
    printf("\n");

    postorder(&nodes[0]);
    printf("\n");

    return 0;
}