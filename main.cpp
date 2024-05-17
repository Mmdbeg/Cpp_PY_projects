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


// Function to interchange two rows of a matrix
void swaprow(Matrix& A , int row1 , int row2)
{

    for (int i = 0 ; i < A.col();++i)
    {
        swap(A(row1,i),A(row2,i)) ;
    }





}

Matrix inv(Matrix& A)
{
    int n = A.row(); // Declare 'n' before using it

    // Create augmented matrix [A | I]
    Matrix B = zeros(n, 2 * n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            B(i, j) = A(i, j);
        }
        B(i, i + n) = 1;
    }



    // Gaussian elimination
    for (int i = 0; i < n; ++i) {
        // Find pivot row
        int pivot_row = i;
        for (int k = i + 1; k < n; ++k)
        {
            if (abs(B(k, i)) > abs(B(pivot_row, i)))
                {
                    pivot_row = k;
                }
        }
            if (pivot_row != i)
                {
                   swaprow(B, i, pivot_row); // Assuming you have a function to swap rows
                }

        // Make the diagonal element 1
        double pivot = B(i, i); // Correctly reference the pivot element
        for (int j = i; j < 2 * n; ++j) {
            B(i, j) /= pivot;
        }

        // Make other elements in the column 0
        for (int k = 0; k < n; ++k) {
            if (k != i) {
                double factor = B(k, i);
                for (int j = i; j < 2 * n; ++j) {
                    B(k, j) -= factor * B(i, j);
                }
            }
        }
    }

    // Extract the inverse matrix from the right side of the augmented matrix
    Matrix invA = zeros(n, n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            invA(i, j) = B(i, j + n);
        }
    }

    return invA ;
}




int main()
{




    Matrix A ({{1, 2, 3},
                {0, 1, 4},
                {5, 6, 0}},3,3);

    Matrix A_inv = inv(A);
    cout << "Original Matrix A:" << endl;
    A.show();
    cout << endl;

    cout << "Inverse of Matrix A:" << endl;
    A_inv.show();
    cout << endl;

    Matrix s = multiply(A, A_inv);
    cout << "Multiplication of A and its inverse:" << endl;
    s.show();

    return 0;
}


