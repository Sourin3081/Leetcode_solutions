class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();

        int[] dp = new int[n + 1];
        boolean[][] pal = new boolean[n][n];

        // Find all palindrome substrings
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) &&
                    (j - i <= 2 || pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                }
            }
        }

        // DP to find maximum number of non-overlapping palindromes
        for (int i = 1; i <= n; i++) {

            // Don't select a palindrome ending at i-1
            dp[i] = dp[i - 1];

            // Check substrings ending at i-1
            for (int j = 0; j <= i - k; j++) {

                if (pal[j][i - 1]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        return dp[n];
    }
}