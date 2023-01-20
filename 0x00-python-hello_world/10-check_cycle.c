#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head node of the singly linked list
 *
 * Return: 1 if there is a cycle, 0 if there is not
 */
int check_cycle(listint_t *list)
{
	listint_t *check;
	listint_t *forward;
	int b;

	if (list == NULL)
		return (0);

	b = 0;
	forward = list;
	while (forward->next != NULL && forward->next != list)
	{
		forward = forward->next;
	}

	check = forward;
	forward = list;
	while (forward != NULL)
	{
		if (forward == check->next)
		{
			b = 1;
			break;
		}
		forward = forward->next;
	}
	return (b);
}
