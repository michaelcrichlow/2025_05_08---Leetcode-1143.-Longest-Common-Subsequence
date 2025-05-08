# My first attemt to solve it. Can't repeat letters since it uses a dictionary.
# Have to use a difference approach.
def longestCommonSubsequence_00(s1: str, s2: str) -> int:
    shorter_word, longer_word = sorted([s1, s2], key=len)
    
    local_dict = dict()
    for i, val in enumerate(longer_word):
        local_dict[val] = i
    
    count = 1
    max_count = 0
    for i in range(len(shorter_word) - 1):
        if local_dict.get(shorter_word[i + 1], -1) > local_dict.get(shorter_word[i], -1):
            count += 1
            max_count = max(max_count, count)

    return max_count


# Solution accepted. Beats 72.99%
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # Create a 2D DP table initialized to 0
    dp = [[0] * (n + 1) for val in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:  # If characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Otherwise, take the max of previous results
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]  # The bottom-right cell contains the LCS length

def main() -> None:
    print(longestCommonSubsequence('abcde', 'ace')) # 3
    print(longestCommonSubsequence('abcde', 'acb')) # 2
    print(longestCommonSubsequence('abcde', 'cat')) # 1
    print(longestCommonSubsequence('bl', 'yby'))    # 1


if __name__ == '__main__':
    main()

# longestCommonSubsequence('abcde', 'ace') => 3