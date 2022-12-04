#include "lists.h"

/**
 * check_cycle - check for circle in a linked list
 *
 * @list: Pointer to the head node
 *
 * Return: 0 for success else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);
	current = list;
	while (current->next != NULL)
	{
		current = current->next;
		if (current->next == list)
			return (1);
	}
	return (0);
}
