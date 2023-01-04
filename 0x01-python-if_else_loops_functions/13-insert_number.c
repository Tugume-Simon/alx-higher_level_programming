#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: address of pointer to singly linked list
 * @number: number to be inserted
 *
 * Return: On success address of new node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert;
	listint_t *current;
	listint_t *tmp;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
	{
		free(insert);
		return (NULL);
	}
	insert->n = number;
	insert->next = NULL;
	tmp = NULL;

	current = *head;
	if (current == NULL)
	{
		*head = insert;
	}
	else
	{
		while (current != NULL && current->n < number)
		{
			tmp = current;
			current = current->next;
		}
		insert->next = current;
		if (tmp == NULL)
			*head = insert;
		else
			tmp->next = insert;
	}

	return (insert);
}
