class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = [[None] * (len(s) + 1) for _ in range(len(s) + 1)]
        longest = [""]

        def dfs(i, j):
            if i >= j:
                return True

            if cache[i][j] is not None:
                return cache[i][j]

            cache[i][j] = (
                s[i] == s[j - 1]
                and dfs(i + 1, j - 1)
            )

            if cache[i][j] and j - i > len(longest[0]):
                longest[0] = s[i:j]

            return cache[i][j]

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                dfs(i, j)

        return longest[0]