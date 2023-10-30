#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct listint_t - singly linked list
 * @n: int
 * @next: pointer to next node
 */

typedef struct listint_t
{
	int n;
	struct listint_t *next;
}listint_t;

size_t print_listint(count listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
