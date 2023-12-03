#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node
 * Return: pointer to the first node
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *tmp = *head, *dupp = NULL;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			dupp = s->next;
			break;
		}
		if (!f->next)
		{
			dupp = s->next->next;
			break;
		}
		s = s->next;
	}
	reverse_listint(&dupp);
	while (dupp && tmp)
	{
		if (tmp->n == dupp->n)
		{
			dupp = dupp->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}
	if (!dupp)
		return (1);
	return (0);
}
