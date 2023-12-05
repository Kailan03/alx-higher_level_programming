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
