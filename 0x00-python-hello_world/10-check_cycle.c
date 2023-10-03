#include "lists.h"

/**
 * check_cycle - This checks if a singly linked list has
 * a cycle in it.
 * @list: The pointer to the list.
 * Return: Always 0 if there is no cycle,
 * or 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr2;
	listint_t *prev;

	ptr2 = list;
	prev = list;
	while (list && ptr2 && ptr2->next)
	{
		list = list->next;
		ptr2 = ptr2->next->next;

		if (list == ptr2)
		{
			list = prev;
			prev =  ptr2;
			while (1)
			{
				ptr2 = prev;
				while (ptr2->next != list && ptr2->next != prev)
				{
					ptr2 = ptr2->next;
				}
				if (ptr2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
