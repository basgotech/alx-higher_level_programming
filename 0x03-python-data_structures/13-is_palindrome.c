#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node
 * Return: pointer to the first node
 */
void reverse_listint(listint_t **head)
{
	listint_t *pre = NULL;
	listint_t *cu = *head;
	listint_t *nx = NULL;

	while (cu)
	{
		nx = cu->nx;
		cu->nx = pre;
		pre = cu;
		cu = nx;
	}

	*head = pre;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *temp = *head, *dupp = NULL;

	if (*head == NULL || (*head)->nx == NULL)
		return (1);

	while (1)
	{
		f = f->nx->nx;
		if (!f)
		{
			dupp = s->nx;
			break;
		}
		if (!f->nx)
		{
			dupp = s->nx->nx;
			break;
		}
		s = s->nx;
	}

	reverse_listint(&dupp);

	while (dupp && temp)
	{
		if (temp->n == dupp->n)
		{
			dupp = dupp->nx;
			temp = temp->nx;
		}
		else
			return (0);
	}
	if (!dupp)
		return (1);

	return (0);
}
