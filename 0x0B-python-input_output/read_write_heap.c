#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
	int i = 0;
	char *str = NULL;
	
	str = strdup("Holberton");

	for (i = 0; i <= 200; i++)
	{
		printf("[%03d] %s\n", i, str);
		sleep(1);
	}

	return (0);
}