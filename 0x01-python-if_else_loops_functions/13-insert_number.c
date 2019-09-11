#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node in a sorted list
 * @head: pointer to head
 * @number: number
 *
 * Return: list *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *add_node = NULL;
	listint_t *tmp = *head;

	if (!head)
		return (NULL);

	add_node = malloc(sizeof(listint_t));

	if (!add_node)
		return (NULL);

	add_node->n = number;
	add_node->next = NULL;

	if (!*head)
	{
		*head = add_node;
		return (add_node);
	}

	while (tmp->next)
	{
		if (add_node->n >= tmp->n && add_node->n <= tmp->next->n)
		{
			add_node->next = tmp->next;
			tmp->next = add_node;
			return (add_node);
		}

		tmp = tmp->next;
	}

	return (add_node);
}
