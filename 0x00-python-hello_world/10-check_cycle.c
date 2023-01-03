#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head node of the singly linked list
 *
 * Return: 1 if there is a cycle, 0 if there is not
 */
int check_cycle(listint_t *list)
{
	int b; /* boolean, 0-false, 1-true */
	listint_t *forward;
	
	if (list == NULL)
		return (0);

	b = 0;
	forward = list->next;
	while (forward != NULL)
	{
		if (forward->next == list)
		{
			b = 1;
			break;
		}
		forward = forward->next;
	}

	return (b);
}
