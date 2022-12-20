#include "lists.h"

/**
  * node_count - counts the number of node in a linked list
  * @head: head of list
  *
  * Return: number of nodes
  */
int node_count(listint_t **head)
{
    listint_t *ptr;
    int nodes = 0;
    
    ptr = *head;
    while (ptr != NULL)
    {
	nodes += 1;
	ptr = ptr->next;
    }

    return (nodes);
}


/**
  * is_palindrome - checks if a linked list is a palindrome
  * @head: head of list
  *
  * Return: 1 if it is a palindrome, 0 otherwise
  */
int is_palindrome(listint_t **head)
{
    listint_t *ptr;
    int *arr;
    int i, j, end;

    ptr = *head;
    if (ptr == NULL)
	return (1);

    end = node_count(head);
    j = end - 1;

    arr = malloc(sizeof(int) * (end + 1));
    if (arr == NULL)
	return (0);

    arr[end] = '\0';

    for (i = 0; ptr != NULL; i++)
    {
	arr[i] = ptr->n;
	ptr = ptr->next;
    }
    
    for (i = 0; i < j; i++, j--)
    {
	if (arr[i] != arr[j])
	    return (0);
    }
    
    return (1);

}
