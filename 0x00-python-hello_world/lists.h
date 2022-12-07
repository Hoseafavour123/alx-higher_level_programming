#ifndef LIST_H
#define LIST_H

/**
  * struct listint_s - singly linked list
  * @n: integer
  * @next: pointer to next node
  *
  * Description: singly linked list node structure
  *
  */
typedef struct listint_s
{
	int n;
	struct listint_s *next;

} listint_t;

int check_cycle(listint_t *list);

#endif /*LIST_H*/
