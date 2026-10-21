# NumPy Array Operations — Analysis Report

## 1. Project Overview

This project demonstrates element-wise mathematical operations using NumPy arrays in Python. Two numerical arrays are created, and addition, subtraction, multiplication, and division are performed.

## 2. Objective

- Create two NumPy arrays.
- Perform four mathematical operations.
- Check the shape and data type of both arrays.
- Understand vectorized operations in NumPy.

## 3. Dataset

Array A: [10, 20, 30, 40, 50]

Array B: [2, 4, 5, 8, 10]

Both arrays contain five numerical elements and have the same shape.

## 4. Methodology

The program creates two arrays using `numpy.array()`. It checks whether their shapes match and verifies that the values are finite and that the divisor array does not contain zero.

The program then performs four element-wise operations:

- Addition using `array_a + array_b`
- Subtraction using `array_a - array_b`
- Multiplication using `array_a * array_b`
- Division using `array_a / array_b`

The results and array information are displayed in the terminal.

## 5. Results

| Operation | Result |
|---|---|
| Addition | [12, 24, 35, 48, 60] |
| Subtraction | [8, 16, 25, 32, 40] |
| Multiplication | [20, 80, 150, 320, 500] |
| Division | [5, 5, 6, 5, 5] |

Array A shape: (5,)

Array B shape: (5,)

## 6. Vectorization

Vectorization allows NumPy to apply mathematical operations to entire arrays without writing an explicit Python loop for every element. This makes numerical code concise and can improve performance for large arrays.

## 7. Conclusion

The project demonstrates how NumPy simplifies mathematical operations on numerical arrays. It also shows the importance of checking array shapes and handling invalid division inputs.

The same approach can be applied to numerical calculations in data analysis, scientific computing, and machine learning.
