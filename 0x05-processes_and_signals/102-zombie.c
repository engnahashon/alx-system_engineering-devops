#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - causes an infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	infinite_while();
	return (0);
}
