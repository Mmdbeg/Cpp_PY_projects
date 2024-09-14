#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;



// celsius to fahrenheit  +
// celsius to kelvin +
// fahrenheit to celsius + 
// fahrenheit to kelvin +
// kelvin to fahrenheit 
// kelvin to celsius 

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void C2F(float t)
{
	t = t * 9 / 5 + 32 ; 
	cout << t << "' " << " Fahrenheit \n";

	t = 273.15 + t;
	cout << t << "' " << " kelvin\n";
}

void F2C(float t)
{
	t = (t - 32) * 5 / 9;
	cout << t << "' " << " celsius\n";

	t = (t - 32) * 5 / 9 + 273.15; 
	cout << t << "' " << " kelvin\n";
}

void k2F(float t)
{
	t = (t - 273.15) * 9 / 5 + 32;
	cout << t << "' " << " fahrenheit\n";

	t = t - 273.15 ; 
	
	cout << t << "' " << " celsius\n";
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main()
{
	char temp_char; 
	float temp_nu; 
	while (true)
	{
		cout << "enter temperture  :\n";
		cin >> temp_nu;
		cout << "enter temperture unit (c/f/k) :\n";
		cin >> temp_char;

		if (temp_char == 'c' || temp_char == 'C')
		{
			C2F(temp_nu);
		}
		else if ((temp_char == 'k' || temp_char == 'K'))
		{
			k2F(temp_nu);
		}
		else if (temp_char == 'f' || temp_char == 'F')
		{
			F2C(temp_nu);
		}
		else
		{
			cout << "please enter correct format :\n";
			continue;
		}
	}



	return 0; 
}
