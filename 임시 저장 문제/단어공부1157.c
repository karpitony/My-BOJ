#include <stdio.h>
#include <string.h>

// 소문자 -> 대문자 함수 
int upper(char str, int len)
{
	
	for(int num2=0; num2<len; num2++)
	{
		if(str[num2] >= 'a'&& str[num2] <= 'z') str[num2]+=32;
	}
	return(str);
}

int main()
{
	char word1[1000000];
	scanf("%s", &word1);
	
	char* word2;
	word2 = strtok(word1,"");
	int len=strlen(word2);
	word2 = upper(word2)
	
	int cnt[26] = {0, };
	
	for(int num=0; num<len; num++)
	{
		for
	}
	

}
