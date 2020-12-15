#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: head of the list
 *
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int arr[2048], i, j = 0;

	if (*head)
	{
		for (i = 0; cur; i++)
		{
			arr[i] = cur->n;
			cur = cur->next;
		}

		for (j = 0; j < i / 2; j++)
		{
			if (arr[j] != arr[i - j - 1])
				return (0);
		}
	}
	return (1);
}
