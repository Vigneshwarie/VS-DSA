# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


def longest_common_subsequence(text1: str, text2:str) -> int:
     m = len(text1)
     n = len(text2)

     memo = {}

     def helper(i, j):
          if i == m or j == n:
               return 0

          if (i,j) in memo:
               return memo[(i,j)]

          if text1[i] == text2[j]:
               memo[(i,j)] = 1 + helper(i+1, j+1)
          else:
               memo[(i,j)] = max(helper(i+1,j), helper(i, j+1))
          
          return memo[(i,j)]

     return helper(0,0)


text1 = "horse"
text2 = "hhh"
print(longest_common_subsequence(text1, text2))
