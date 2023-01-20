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

	if (list == NULL)
		return (0);

	check = list;
	if (check->next == check)
		return (1);
	while (check != NULL)
	{
		check = check->next;
		if (check == list)
			return (1);
	}
	return (0);
}
