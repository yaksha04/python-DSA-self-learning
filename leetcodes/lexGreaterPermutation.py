class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Store how much of target we can match
        prefix_len = 0

        while prefix_len < n:
            idx = ord(target[prefix_len]) - ord('a')

            if freq[idx] == 0:
                break

            freq[idx] -= 1
            prefix_len += 1

        # Backtrack from the rightmost matched position
        for i in range(prefix_len, -1, -1):

            # If this position was matched before,
            # put that character back.
            if i < prefix_len:
                idx = ord(target[i]) - ord('a')
                freq[idx] += 1

            # We need a character strictly greater than target[i]
            if i == n:
                continue

            target_idx = ord(target[i]) - ord('a')

            for c in range(target_idx + 1, 26):

                if freq[c] > 0:
                    freq[c] -= 1

                    # Prefix remains same as target
                    ans = target[:i]

                    # Put the bigger character
                    ans += chr(c + ord('a'))

                    # Put all remaining characters in sorted order
                    for x in range(26):
                        ans += chr(x + ord('a')) * freq[x]

                    return ans

        return ""
