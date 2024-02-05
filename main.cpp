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

Matrix ones(int row , int col)
    {
        vector<vector<float>> elements(row, vector<float>(col, 1));



        return Matrix(elements,row,col);
    }


Matrix zeros(int row , int col)
    {
        vector<vector<float>> elements(row, vector<float>(col, 0));



        return Matrix(elements,row,col);
    }


Matrix eye(int row, int col)
{
    vector<vector<float>> elements(row,vector<float>(col,0));
      for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            if(i==j){elements[i][j]=1 ;}
        }

    }
    return Matrix(elements,row,col) ;
}

/////********************************************************************************************************************






int main()
{
/*
    vector<vector<float>> a = eye(3,3);
    Matrix s(a);
    Matrix b({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3, 3);

    s.show();

    b.dimention();
*/


    Matrix a = ones(4,5);
    a.show();
    a.dimention();
    cout<<endl;
    Matrix b = eye(4,4);
    b.show();
    b.dimention();

    return 0;
}











