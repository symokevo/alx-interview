
# 2D Matrix Rotation

This is a Python function that allows you to rotate a given n x n 2D matrix 90 degrees clockwise in-place. The rotation is achieved by transposing the matrix and then reversing each row.

## How to Use

1. Import the function:
   ```python
   from matrix_rotation import rotate_2d_matrix
   ```

2. Prepare your matrix as a list of lists, where each inner list represents a row in the matrix:
   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   ```

3. Call the `rotate_2d_matrix` function with your matrix as an argument:
   ```python
   rotate_2d_matrix(matrix)
   ```

4. The matrix will be rotated 90 degrees clockwise in-place.

## Example

### Input:
```
1  2  3
4  5  6
7  8  9
```

### Output:
```
7  4  1
8  5  2
9  6  3
```

## Notes
- The matrix should have 2 dimensions and should not be empty.
- The function does not return anything, as it modifies the matrix in-place.

## Implementation Details

The rotation is performed using two main steps:
1. Transpose: Swap the elements at matrix[i][j] and matrix[j][i].
2. Reverse each row to achieve the final rotated matrix.

The function combines these two steps to effectively rotate the matrix.
