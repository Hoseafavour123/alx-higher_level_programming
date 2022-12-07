#include "lists.h"

/**
  * check_cycle - checks if a cycle contains a cycle
  * @list: list
  *
  * Return: 1 if there is a cycle, 0 otherwise
  */

int check_cycle(listint_t *list)
{
	listint_t *ptr1;
	listint_t *ptr2;

	ptr1 = list;
	ptr2 = list;

	while (ptr1 != NULL && ptr2 != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
			return (1);
	}

	return (0);
}
