#include "lists.h"
/**
  * insert_node - inserts a node into a sorted linked list
  * @head: head of list
  * @number: integer to insert
  *
  * Return: address of new node
  */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
	return (NULL);
    new->n = number;
    new->next = NULL;

    current = *head;
    if (current == NULL || current->n >= number)
    {
	new->next = current;
	*head = new;
	return (new);
    }
    
    while (current && current->next && current->next->n < number)
	current = current->next;

    new->next = current->next;
    current->next = new;

    return (new);
} 
