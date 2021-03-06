import numpy as np
import pandas as pd


# PYTHON SECTION

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.
    '''
    new_d = dict()
    
    for char in string:
        if char not in new_d:
            new_d[char]=string.count(char)
    return new_d


#print(count_characters("abafdcggfaabe"))


def invert_dictionary(d):
    '''
    INPUT: DICT
    OUTPUT: DICT (of sets of input keys indexing the same input values
                  indexed by the input values)

    Given a dictionary d, return a new dictionary with d's values
    as keys and the value for a given key being
    the set of d's keys which shared the same value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    d1= dict()

    for key, val in d.items():
        if val in d1:
            d1[val].update(key)
        else:
            d1[val]=set(key)
    return d1

#print(invert_dictionary({"a": 4, "b": 2, "c": 1, "d": 1, "e": 1, "f": 2, "g": 2}))

def word_count(filename):
    '''
    INPUT: STRING
    OUTPUT: INT, INT, INT (a tuple with line, word,
                           and character count of named INPUT file)

    The INPUT filename is the name of a text file.
    The OUTPUT is a tuple containting (in order)
    the following stats for the text file:
      1. number of lines
      2. number of words (broken by whitespace)
      3. number of characters
    '''
    with open(filename,'r') as f:
        read_data = f.read()
        lst = []
        chars = len(read_data)
        lines =len(read_data.split('\n'))
        words = len(read_data.split())
       
    f.closed
    return tuple([lines, words, chars])

#print(word_count('alice.txt'))

def matrix_multiplication(A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS,
            LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
            (storing the product of a matrix multiplication operation)

    Return the matrix which is the product of matrix A and matrix B
    where A and B will be (a) integer valued (b) square matrices
    (c) of size n-by-n (d) encoded as lists of lists.

    For example:
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix

        | 2  3  4 |
        | 6  4  2 |
        |-1  2  0 |

    Please do not use numpy. Write your solution in straight python.
    '''
    results,interm=[], []
    val=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                val+=A[i][k] * B[k][j]
            interm.append(val)
            val=0
        results.append(interm)
        interm=[]
        
    return results

'''
A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]]
B = [[8, -3, 1], [-7, 3, 2], [0, 3, 3]]
print(matrix_multiplication(A, B))
'''

# NumPy SECTION


def array_work(rows, cols, scalar, matrixA):
    '''
    INPUT: INT, INT, INT, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY
    (of matrix product of r-by-c matrix of "scalar"'s time matrixA)

    Create matrix of size (rows, cols) with elements initialized to the scalar
    value. Right multiply that matrix with the passed matrixA (i.e. AB, not
    BA).  Return the result of the multiplication.  You needn't check for
    matrix compatibililty, but you accomplish this in a single line.

    E.g., array_work(2, 3, 5, [[3, 4], [5, 6], [7, 8]])
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
    '''

    return(matrixA.dot(np.full((rows,cols),scalar)))

'''    
matrixA = np.array([[-4, -2],
                    [0, -3],
                    [-4, -1],
                    [-1, 1],
                    [-3, 0]])
print(array_work(2, 3, 4, matrixA))
print(array_work(2, 2, 6, matrixA))
'''

def boolean_indexing(arr, minimum):
    '''
    INPUT: NUMPY ARRAY, INT
    OUTPUT: NUMPY ARRAY
    (of just elements in "arr" greater or equal to "minimum")

    Return an array of only the elements of "arr" that are greater than or
    equal to "minimum"

    Ex:
    In [1]: boolean_indexing([[3, 4, 5], [6, 7, 8]], 7)
    Out[1]: array([7, 8])
    '''
    return arr[arr >= minimum]

""" arr = np.array([[-4, -4, -3],
                    [-1, 16, -4],
                    [-3, 6, 4]])
print(boolean_indexing(arr, 0))
print(boolean_indexing(arr, 10))
"""

# Pandas SECTION

def make_series(start, length, idx):
    '''
    INPUTS: INT, INT, LIST (of length "length")
    OUTPUT: PANDAS SERIES (of "length" sequential integers
             beginning with "start" and with index "index")

    Create a pandas Series of length "length" with index "index"
    and with elements that are sequential integers starting from "start".
    You may assume the length of index will be "length".

    E.g.,
    In [1]: make_series(5, 3, ['a', 'b', 'c'])
    Out[1]:
    a    5
    b    6
    c    7
    dtype: int64
    '''
    return pd.Series(range(start, start+length), index = idx)


#print(make_series(7, 4, ['a', 'b', 'c', 'd']))
#print(make_series(22, 5, ['a', 'b', 'c', 'd', 'hi']))

def data_frame_work(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    Assume that df contains columns colA and colB and that these are numeric.
    '''
    df[colC] = df[colA] + df[colB]
    return df

'''
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
colA, colB, colC = ('a', 'b', 'c')
df2=data_frame_work(df, colA, colB, colC)
print(df2)
print(df2.columns.tolist())
print(df2[colC].tolist())
'''