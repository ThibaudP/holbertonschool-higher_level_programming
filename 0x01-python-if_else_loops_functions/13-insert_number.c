#include "lists.h"

/**
 * insert_node - inserts node in a sorted linked list
 *
 * @head: head node to list
 * @number: number to add in new node
 *
 * Return: address to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	if (*head == NULL)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}


	if (number < cur->n)
	{
		new->next = cur;
		new->n = number;
		*head = new;
	}
	else
	{
		while (cur->next && number > cur->next->n)
			cur = cur->next;

		new->n = number;
		new->next = cur->next;
		cur->next = new;
	}

	return (new);

}
