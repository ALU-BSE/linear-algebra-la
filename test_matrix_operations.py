import unittest

class TestMatrixOperations(unittest.TestCase):
    def test_matrix_calculation(self):
        # Test case 1: Given example in the original code
        Prices = [[300, 500],
                  [1000, 120.85]]
        Array2 = [200, 100]
        Ans = []
        for i in range(len(Prices)):
            row_sum = 0
            for j in range(len(Prices[0])):
                row_sum += Prices[i][j] * Array2[j]
            Ans.append(row_sum)
        self.assertEqual(Ans, [110000, 212085.0])

    def test_different_matrix(self):
        # Test case 2: Different matrix and quantities
        Prices = [[1, 2], [3, 4]]
        Array2 = [5, 6]
        Ans = []
        for i in range(len(Prices)):
            row_sum = 0
            for j in range(len(Prices[0])):
                row_sum += Prices[i][j] * Array2[j]
            Ans.append(row_sum)
        self.assertEqual(Ans, [17, 39])

    def test_empty_matrix(self):
        # Test case 3: Edge case with an empty matrix
        Prices = []
        Array2 = [5, 6]
        Ans = []
        for i in range(len(Prices)):
            row_sum = 0
            for j in range(len(Prices[0])):
                row_sum += Prices[i][j] * Array2[j]
            Ans.append(row_sum)
        self.assertEqual(Ans, [])

    def test_single_row_matrix(self):
        # Test case 4: Single row in the matrix
        Prices = [[10, 20]]
        Array2 = [3, 4]
        Ans = []
        for i in range(len(Prices)):
            row_sum = 0
            for j in range(len(Prices[0])):
                row_sum += Prices[i][j] * Array2[j]
            Ans.append(row_sum)
        self.assertEqual(Ans, [110])

    def test_single_column_matrix(self):
        # Test case 5: Single column in the matrix
        Prices = [[10], [20], [30]]
        Array2 = [2]
        Ans = []
        for i in range(len(Prices)):
            row_sum = 0
            for j in range(len(Prices[0])):
                row_sum += Prices[i][j] * Array2[j]
            Ans.append(row_sum)
        self.assertEqual(Ans, [20, 40, 60])

if __name__ == "__main__":
    unittest.main()
