#include "lists.h"

/**
 * check_cycle - checks the cycle in the linked list
 * @list: the linked list to be checked
 * Return: 1 if cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
