#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head node of the singly linked list
 *
 * Return: 1 if there is a cycle, 0 if there is not
 */
int check_cycle(listint_t *list)
{
	int b; /* boolean */
	listint_t *current;
	
	if (list == NULL)
		return (0);

	b = 0;
	current = list;
	do {
		current = current->next;
		if (current == list)
		{
			b = 1;
			break;
		}
	} while (current != NULL);

	return (b);
}
