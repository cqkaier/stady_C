#include <stdio.h>
#include <stdlib.h>

// 定义二叉树节点结构体
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

// 创建一个新的节点
struct Node* newNode(int data) {
    struct Node* node = (struct Node*) malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

// 先序遍历
void preorderTraversal(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

// 中序遍历
void inorderTraversal(struct Node* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->data);
        inorderTraversal(root->right);
    }
}

// 后序遍历
void postorderTraversal(struct Node* root) {
    if (root != NULL) {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        printf("%d ", root->data);
    }
}

int main() {
    // 创建一个二叉树
    struct Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);

    // 打印各种遍历结果
    printf("先序遍历: ");
    preorderTraversal(root);
    printf("\n");

    printf("中序遍历: ");
    inorderTraversal(root);
    printf("\n");

    printf("后序遍历: ");
    postorderTraversal(root);
    printf("\n");

    return 0;
}

