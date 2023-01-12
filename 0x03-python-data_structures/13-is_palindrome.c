#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to address of head of linked list
 *
 * Return: 1 if singly linked list is a palindrome,
 * 0 if singly linked list is not a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr; /* current */
	listint_t *check;

	if (*head == NULL)
		return (1);

	curr = *head;
	while (curr != NULL)
	{
		check = curr;
		if (!check->next)
			break;
		while (check->next->next != NULL)
		{
			check = check->next;
		}
		if (curr->n != check->next->n)
			return (0);
		check->next = NULL;
		curr = curr->next;
	}
	return (1);
}
