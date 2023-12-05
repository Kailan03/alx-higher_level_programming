#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head);
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);  /* An empty list or a list with one element is a palindrome*/
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *second_half;

    /* Move slow_ptr to the middle of the list*/
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}

    /* If the length of the list is odd, move slow_ptr to the next node*/
	if (fast_ptr != NULL)
	{
		slow_ptr = slow_ptr->next;
	}

    /* Reverse the second half of the list*/
	second_half = reverse_list(slow_ptr);

    /* Compare the first half and the reversed second half*/
	return (compare_lists(*head, second_half));
}
/**
 * reverse_list - reverse the first half of the list
 * @head: pointer to the first node
 *
 * Return: 0 for success
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * compare_lists - compares first half and second half of the list
 * @list1: pointer to first half
 * @list2: pointer to second half
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
		{
			return (0);  /* not a palindrome*/
		}
		list1 = list1->next;
		list2 = list2->next;
	}
	return (1);  /* Palindrome*/
}
/**
 * print_listint - prints all elements in a list
 * @h: pointer to head of list
 *
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		fprintf(stderr, "Memory allocation failed\n");
		exit(EXIT_FAILURE);
	}
	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
	}
		else
		{
			listint_t *temp = *head;

			while (temp->next != NULL)
			{
				temp = temp->next;
			}
			temp->next = new_node;
		}
		return (new_node);
}
/**
 * free_listint - frees a listint_t list
 * @head: pointer to the list to be freed
 *
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
