package test

import "core:fmt"
print :: fmt.println

main :: proc() {
    print(longestCommonSubsequence("abcde", "ace")) // 3
    print(longestCommonSubsequence("abcde", "acb")) // 2
    print(longestCommonSubsequence("abcde", "cat")) // 1
    print(longestCommonSubsequence("bl", "yby"))    // 1

    free_all(context.temp_allocator)
    // Output:
    // 3
    // 2
    // 1
    // 1
}

longestCommonSubsequence :: proc(text1: string, text2: string) -> int {
    m := len(text1)
    n := len(text2)

    // Create a 2D array initialized to 0
    dp := make([][]int, m+1, context.temp_allocator)
    for i in 0 ..< m + 1 {
        dp[i] = make([]int, n+1, context.temp_allocator)
    }

    // Fill the DP table
    for i in 1 ..< m + 1 {
        for j in 1 ..< n + 1 {
            if text1[i-1] == text2[j-1] {
                dp[i][j] = dp[i-1][j-1] + 1 // Match found, increase count
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) // Take max of previous results
            }
        }
    }

    return dp[m][n] // The bottom-right cell contains the LCS length
}