import unittest

def build_matrix(str1, str2):
    matrix = []
    for _ in range(len(str2)+1):
        row = []
        for _ in range(len(str1)+1):
            row.append(0)
        matrix.append(row)
    return matrix


def lcs(str1, str2):
    matrix = build_matrix(str1, str2)
    for j, char_row in enumerate(str2):
        for i, char_col in enumerate(str1):
            top_left = matrix[j][i]
            prev_col = matrix[j+1][i]
            prev_row = matrix[j][i+1]
            if char_row == char_col:
                matrix[j+1][i+1] = top_left + 1
            else:
                matrix[j+1][i+1] = max(prev_col, prev_row)
    return matrix[len(str2)][len(str1)]

class Tests(unittest.TestCase):

    def test_1(self):
        test_A1 = "WHOWEEKLY"
        test_B1 = "HOWONLY"
        lcs_val1 = lcs(test_A1, test_B1)
        self.assertEqual(lcs_val1,5)



    def test_2(self):
        test_A2 = "CATSINSPACETWO"
        test_B2 = "DOGSPACEWHO"
        lcs_val2 = lcs(test_A2, test_B2)
        self.assertEqual(lcs_val2,7)

if __name__ == '__main__':
    unittest.main()