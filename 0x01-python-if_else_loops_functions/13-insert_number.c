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
	listint_t *add_node = malloc(sizeof(listint_t));
	listint_t *tmp_node = *head;
	add_node->next = NULL;
	add_node->n = number;

	if (!head || !add_node)
		return (NULL);

	if (!*head)
	{
		*head = add_node;
		return (*head);
	}

	while (tmp_node->next)
	{
		if (add_node->n >= tmp_node->n && add_node->n <= tmp_node->next->n)
		{
			add_node->next = tmp_node->next;
			tmp_node->next = add_node;
			return (add_node);
		}

		tmp_node = tmp_node->next;
	}

	return (add_node);
}
