#include <iostream>
#include <string>

using namespace std;


int a, b, c;


void result1(char Sign)
{
	cout << a << Sign << b << "=" << c << endl;
}

void result2(char Sign)
{
	cout << a << "=" << b << Sign << c << endl;
}


int main()
{
	
	cin >> a >> b >> c;

	if(a+b == c) result1('+');
	else if(a-b == c) result1('-');
	else if(a*b == c) result1('*');
	else if(a/b == c) result1('/');

	else if(b+c == a) result2('+');
	else if(b-c == a) result2('-');
	else if(b*c == a) result2('*');
	else if(b/c == a) result2('/');
	return 0;
}