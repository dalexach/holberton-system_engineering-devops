#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
* infinite_while - infinite loop
* Return: 0 when exit
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
* main - Function to fork 5 PID
* Return: 0
*/
int main(void)
{
	pid_t zombie;
	size_t n = 0;

	while (n < 5)
	{
		zombie = fork();
		if (zombie == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", zombie);
		n++;
	}
	return (infinite_while());
}
