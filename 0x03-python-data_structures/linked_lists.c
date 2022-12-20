#include "lists.h"


/**
  * print_listint - prints the elements of a listint
  * @h: head of lists
  *
  * Return: number of nodes
  */
size_t print_listint(const listint_t *h)
{
    size_t nodes = 0;
    const listint_t *ptr;

    ptr = h;

    while (ptr != NULL)
    {
	printf("%d\n", ptr->n);
	nodes += 1;
	ptr = ptr->next;
    }
    return (nodes);
}

/**
  * add_nodeint_end - adds a node to the end of singly linked list
  * @head: head of list
  * @n: integer
  *
  * Return: pointer to new list
  */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new, *ptr;

    ptr = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
	return (NULL);
    new->n = n;
    new->next = NULL;

    if (*head == NULL)
	*head = new;
    else
    {
	while (ptr->next != NULL)
	    ptr = ptr->next;
	ptr->next = new;
    }

    return (new);
}

/**
  * free_listint - frees a listint list
  * @head: head of list
  *
  * Return: void
  */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
	current = head;
	head = head->next;
	free(current);
    }
}

