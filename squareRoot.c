/*
 * =====================================================================================
 *
 *       Filename:  squareRoot.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/01/16 10:51:54
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

float absoluteValue(float x);
float squareRoot(float epsilon, float userNum);

int main(void)
{
	while(true)
	{
		float userNum;
		float epsilon;

		printf("Enter the number U want to square: ");
		scanf("%f", &userNum);
		printf("Enter the acceptable error margin: ");
		scanf("%f", &epsilon);
		printf("square root of %i is %0.2f\n", (int)userNum, squareRoot(epsilon, userNum));
	}
	return 0;
}

float absoluteValue(float x)
{
		if(x < 0)
			x = -x;
		return x;
}

float squareRoot(float epsilon, float userNum)
{
		float guess = 1.0;
		while(absoluteValue((guess * guess) - userNum) >= epsilon)
		{
				guess = (userNum/guess + guess)/2.0;
		}
		return guess;
}
