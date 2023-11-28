#include "lists.h"

/**
 * insert_node - Inserts a number into singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Basliel Tegegn
 * Return: If the function fails - NULL.
 *         or a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *fresh;

	fresh = malloc(sizeof(listint_t));
	if (fresh == NULL)
		return (NULL);
	fresh->n = number;

	if (nd == NULL || nd->n >= number)
	{
		fresh->next = nd;
		*head = fresh;
		return (fresh);
	}

	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;

	fresh->next = nd->next;
	nd->next = fresh;

	return (fresh);
}
