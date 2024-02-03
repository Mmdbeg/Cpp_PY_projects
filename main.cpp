#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;


class Matrix // matrix class for general matrixes
{
public:
    vector<vector<float>> Elements ;
    int Row ;
    int Column ;

    //constructer
    Matrix(vector<vector<float>> elements, int row=1 , int columns=0):Elements(elements),Row(row),Column(columns){}


public:

    void show() const
    {
     for(int i=0;i<Row;++i)
        {
        for(int j=0;j<Column;++j)
            {
         cout<<Elements[i][j]<<" ";
            }
            cout<<endl;
        }
    }

    void dimention() const
    {
        cout<<Row<<'x'<<Column;
    }









    };

//  functions for specific matrixes *************************************************************************************
vector<vector<float>> zeros(int row, int col)
{
    vector<vector<float>> elements(row, vector<float>(col, 0)); // Resize the vector

    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            cout << elements[i][j] << " ";
        }
        cout << endl;
    }
    return elements ;
}

vector<vector<float>> ones(int row, int col)
{
    vector<vector<float>> elements(row, vector<float>(col, 1)); // Resize the vector

    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            cout << elements[i][j] << " ";
        }
        cout << endl;
    }
    return elements ;
}

vector<vector<float>> eye(int row, int col)
{
    vector<vector<float>> elements(row,vector<float>(col,0));
      for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            if(i==j){elements[i][j]=1 ;}
            cout << elements[i][j] << " ";
        }
        cout << endl;
    }
    return elements ;
}

/////********************************************************************************************************************


int main()
{

    vector<vector<float>> a = zeros(4,4);

    Matrix s(a);
    Matrix b({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3, 3);
    s.show();
    s.dimention();


    return 0;
}











