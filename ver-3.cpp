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
// printing matrix ---------------------------------------------------------------
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

// getting MATRIXs'  DIMENTIONS (EITHER ROW OR COLUMN )
    void dimention() const
    {
        cout<<Row<<'x'<<Column;
    }

        int row()
    {
        return Row ;
    }

        int col()
    {
        return Column ;
    }



    vector<vector<float>> getElements() {
        return Elements;
    }

    float& operator()(int i, int j)
    {
        return Elements[i][j];
    }

    };

//  functions for specific matrixes (a member of Matrix class) *************************************************************************************

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


Matrix diag(vector<float> elements , int row , int col)
{
     vector<vector<float>> elements1(row, vector<float>(col, 0));
     for (int i = 0 ; i<row ;++i)
     {
         for (int j =0 ; j<col ; ++j)
            {
                 if (i==j)
                    {
                        elements1[i][j]= elements[i] ;
                    }
            }
     }
     return Matrix(elements1,row,col) ;
}


/////********************************************************************************************************************

// MATRIX OPERATIONS
 // #1 MATRIX MULTIPICATION
Matrix multiply( Matrix& A,  Matrix& B) {
    if (A.col() != B.row()) {
        throw invalid_argument("Matrix dimensions are incompatible for multiplication");
    }

    int m = A.row();
    int n = A.col();
    int p = B.col();

    vector<vector<float>> result(m, vector<float>(p, 0));

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            for (int k = 0; k < n; ++k) {
                result[i][j] += A(i,k) * B(k,j);
            }
        }
    }

    return Matrix(result, m, p);
}

// TRANSPOSE OF A MATRIX
Matrix T(Matrix& A)
{
     vector<vector<float>> result(A.row(), vector<float>(A.col(), 0));
        for (int i = 0; i <A.row() ; ++i)
    {
          for (int j = 0; j < A.col(); ++j)
            {
            result[i][j] = A(j,i) ;
            }
    }


     return Matrix(result,A.row(),A.col());
}


int main()
{

    Matrix b({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3, 3);
    Matrix a = eye(3,3);

    /*
    Matrix a = ones(4,5);
    a.show();
    a.dimention();
    cout<<endl;
    Matrix b = eye(4,4);
    b.show();
    b.dimention();
    int x ;
    x = b.Col();
    cout<<endl<<x;

    Matrix d = diag({0.222,0.25,3.12},3,3) ;
    d.show();
    cout<<endl;
    int a = d.row();
    cout<<a;
    */



    Matrix xcap = multiply(a,b) ;
    Matrix xcap_transpose = T(xcap);





    return 0;

}











