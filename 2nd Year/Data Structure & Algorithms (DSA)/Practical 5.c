#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

void insert(struct Node** head_ref, int new_data)
{
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));

    new_node -> data = new_data;

    new_node -> next = (*head_ref);
    new_node -> prev = NULL;

    if((*head_ref) != NULL)
        (*head_ref) -> prev = new_node;

    (*head_ref) = new_node;
}

void deleteNode(struct Node **head_ref, int key)
{
	struct Node* temp = *head_ref, *prev;
	if (temp != NULL && temp->data == key)
	{
		*head_ref = temp->next;
		free(temp);
		return;
	}
	while (temp != NULL && temp->data != key)
	{
		prev = temp;
		temp = temp->next;
	}
	if (temp == NULL) return;
	prev->next = temp->next;

	free(temp);
}

void printList(struct Node* node)
{
    struct Node* last;
    while(node != NULL) {
        printf("%d ", node -> data);
        last = node;
        node = node -> next;
    }
}

int main(int argc, char const *argv[]) {
    struct Node* head = NULL;
    int temp, n, i;

    printf("\n Name: Shivam Tawari");
    printf("\nSection: A \t Semester: 3");
    printf("\nRoll Number: 58");

    printf("\n Enter number of elements to be inserted: ");
    scanf("%d", &n);

    for(i=0; i<n; i++)  {
        printf(" Enter element %d: ", i+1);
        scanf("%d", &temp);
        insert(&head, temp);
    }

    printf("\n Created Doubly Linked List: ");
    printList(head);

    printf("\n Enter element to be deleted: ");
    scanf("%d", &temp);
	deleteNode(&head, temp);

    printf("\n Doubly Linked List after deletion of %d: ", temp);
    printList(head);

    return 0;
}
