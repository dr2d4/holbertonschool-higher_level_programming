#include "lists.h"

/**
 * get_last - return last node of the list
 * @head: head of the list
 *
 * Return: last node
 */
listint_t *get_last(listint_t *head)
{
	listint_t *tmp = head;
	void *prev = NULL;

	while (tmp)
	{
		tmp->prev = prev;
		prev = tmp;

		tmp = tmp->next;
	}

	tmp = head;

	while (tmp->next)
		tmp = tmp->next;

	return (tmp);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head && *head)
	{
		listint_t *last = get_last(*head);
		listint_t *tmp = *head;

		while (tmp && last)
		{
			/* if (last->prev == tmp->next->prev) */
			/*	break; */

			if (last->n != tmp->n)
				return (0);

			/* printf("%d %d\n", last->n, tmp->n); */
			last = last->prev;
			tmp = tmp->next;
		}
	}

	return (1);
}