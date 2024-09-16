#include <iostream>
#include <list>
#include <string>
#include <vector>
#include <cmath>
using namespace std;


class point
{


public :
	// attributes//////////////////////////////////////////////////

	string name ; float x; float y; float z;

	// functions //////////////////////////////////////////////////

	void show_coordinates()
	{
		cout << "point "<<name <<" : "<<"[ " << x << " , " << y <<" , " <<z<<" ]\n";
	}



	// constructors ///////////////////////////////////////////////

	point(string Name  , float X, float Y ,float Z = 0) :name(Name), x(X), y(Y) , z(Z) {};

};

// euclidian distance ---------------------------------------------------------------------------------------

float EU_distance(point a, point b)
{
	float dist;
	dist = sqrt(pow((b.x - a.x) ,2) + pow((b.y - a.y) , 2)  + pow((b.z - a.z),2));
	return dist;
}

int main()
{

	point one("A", 4.5,5.26);
	point two("B", 12.2, 53.12);
	one.show_coordinates();
	two.show_coordinates();


	float d;

	d = EU_distance(one, two);

	cout << d;


	return 0; 
}

