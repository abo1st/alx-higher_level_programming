#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 *  struct listint_s - The singly linked list.
 *  @n: The integer.
 *  @next: This is the points to the next node.
 *  Description: This is the singly linked list node structure.
 **/

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *insert_node(listint_t **head, int number);

#endif

