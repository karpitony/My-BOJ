#include <stdio.h>

main()
{
	int rock, turn = 1;
	scanf( "%d", &rock);
	while (1)
	{
		if(rock >= 3)
		{
			rock -= 3;
			turn += 1;
		}
		else if(rock >= 1)
		{
			rock -= 1;	
			turn += 1;
		}
		else
		{
			if(turn%2 == 1)
			{
				printf( "SK");
				break;
			}
			else
			{
				printf( "CY");
				break;
			}
		}
	}
}