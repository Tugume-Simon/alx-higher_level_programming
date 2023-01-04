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
	listint_t *check;
	
	if (list == NULL)
		return (0);

	b = 0;
	forward = list->next;
	while (forward != NULL)
	{
		check = list;
		while (check != NULL && check != forward)
		{
			if (forward->next == check)
			{
				b = 1;
				break;
			}
			check = check->next;
		}
		if (b == 1)
			break;
		forward = forward->next;
	}

	return (b);
}
