class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        cnt = Counter(s)

        # Check whether a palindrome can be formed
        odd = [c for c in cnt if cnt[c] % 2]

        if len(odd) > 1:
            return ""

        mid = odd[0] if n % 2 else ""

        # Count characters available for the left half
        half_cnt = [0] * 26

        for c, v in cnt.items():
            half_cnt[ord(c) - 97] = v // 2

        m = n // 2
        target_half = target[:m]

        # Try to match target's left half
        rem = half_cnt[:]
        prefix = []

        i = 0

        while i < m:
            x = ord(target_half[i]) - 97

            if rem[x] == 0:
                break

            prefix.append(target_half[i])
            rem[x] -= 1
            i += 1

        # ------------------------------------------------
        # Case 1: target's entire left half is possible
        # ------------------------------------------------
        if i == m:
            left = ''.join(prefix)

            candidate = left + mid + left[::-1]

            # It is already strictly greater
            if candidate > target:
                return candidate

        # ------------------------------------------------
        # Find the rightmost position where we can increase
        # ------------------------------------------------

        # If matching failed at i, we can try increasing
        # target_half[i].
        #
        # If matching succeeded completely, start from m-1.

        pos = i if i < m else m - 1

        while pos >= 0:

            # For the first iteration after a failed match,
            # nothing needs to be restored.
            #
            # Afterwards, restore prefix[pos].
            if pos < i:
                rem[ord(prefix[pos]) - 97] += 1

            # Prefix before pos remains unchanged
            base = prefix[:pos]

            # Character we need to beat
            cur = ord(target_half[pos]) - 97

            # Find the smallest available character > target[pos]
            for c in range(cur + 1, 26):

                if rem[c] == 0:
                    continue

                new_left = base + [chr(c + 97)]

                rem[c] -= 1

                # Fill remaining positions with smallest chars
                for x in range(26):
                    if rem[x]:
                        new_left.extend(
                            [chr(x + 97)] * rem[x]
                        )

                left = ''.join(new_left)

                return left + mid + left[::-1]

            pos -= 1

        return ""
