"""
You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

Input Format
There are 1 lines in the input. First 2 integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the row-wise numbers in the 2D array A.
Output Format
Return an integer denoting the sum of main diagonal elements.
"""
class Solution:
    @staticmethod
    def MainDiagonalSum(x):
        row,col=x[0],x[1]
        array,j=[],2
        for _ in range(col):
            array.append(x[j:(j+row)])
            j+=row
        Sum,i=0,0
        while i<row and i<col:
            Sum+=array[i][i]
            i+=1
        return Sum

if __name__ == '__main__':
    x=list(map(int,input().split()))
    print(Solution().MainDiagonalSum(x))
