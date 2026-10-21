
"""
Performs element-wise addition, subtraction,
multiplication, and division on two NumPy arrays.
"""

import numpy as np


def perform_operations(array_a, array_b):
    """Perform mathematical operations on compatible arrays."""

    if array_a.shape != array_b.shape:
        raise ValueError(
            "Both arrays must have the same shape for this project."
        )

    if not np.all(np.isfinite(array_a)) or not np.all(
        np.isfinite(array_b)
    ):
        raise ValueError("Arrays must contain finite numeric values.")

    if np.any(array_b == 0):
        raise ValueError(
            "Division cannot be performed because array B contains zero."
        )

    results = {
        "Addition": array_a + array_b,
        "Subtraction": array_a - array_b,
        "Multiplication": array_a * array_b,
        "Division": array_a / array_b,
    }

    return results


def display_results(array_a, array_b, results):
    """Display the arrays and their operation results."""

    print("=" * 58)
    print("             NUMPY ARRAY OPERATIONS")
    print("=" * 58)

    print("\nArray A:", array_a)
    print("Array B:", array_b)

    print("\nArray Information")
    print("-" * 58)
    print("Shape of Array A:", array_a.shape)
    print("Shape of Array B:", array_b.shape)
    print("Data type of Array A:", array_a.dtype)
    print("Data type of Array B:", array_b.dtype)

    print("\nMATHEMATICAL OPERATIONS")
    print("-" * 58)

    for operation, result in results.items():
        print(f"{operation:<18}: {result}")

    print("-" * 58)
    print("\nEXPLANATION")
    print(
        "NumPy performs these operations element by element "
        "without requiring explicit loops."
    )
    print(
        "This approach is called vectorization and is useful "
        "for efficient numerical computation."
    )
    print("\nAnalysis completed successfully.")


def main():
    # Create two manually defined NumPy arrays.
    array_a = np.array([10, 20, 30, 40, 50], dtype=float)
    array_b = np.array([2, 4, 5, 8, 10], dtype=float)

    # Check array shapes before performing operations.
    if array_a.shape != array_b.shape:
        print("Error: Arrays must have the same shape.")
        return

    results = perform_operations(array_a, array_b)
    display_results(array_a, array_b, results)


if __name__ == "__main__":
    main()
