#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - This is the singly linked list.
 * @n: This is the integer.
 * @next: This points to the next node.
 * Description: This is the singly linked list node structure.
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);

#endif
