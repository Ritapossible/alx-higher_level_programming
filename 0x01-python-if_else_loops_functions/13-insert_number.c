#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - This inserts a new node
 * at a given position.
 * @head: The head of a list.
 * @number: The index of the list where the new node is
 * added.
 * Return: The address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h;
	listint_t *head_prev;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		head_prev = h;
		h = h->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			head_prev->next = new;
	}

	return (new);
}
