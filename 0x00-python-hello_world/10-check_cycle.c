#include "lists.h"

/**
 * check_cycle - finds a loop in a linked list
 *
 * @head: pointer to head node
 *
 * Return: a pointer to the head node of the reversed list
 */

int check_cycle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	if (head && head->next)
	{
		while (slow && fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;

			if (slow == fast)
			{
				slow = head;
				while (slow != fast)
				{
					slow = slow->next;
					fast = fast->next;
				}
				return (1);
			}
		}
	}

	return (0);
}
