from itertools import permutations

class Solution(object):
    def countGoodIntegers(self, n, k):
        def is_valid_palindrome(s):
            return s == s[::-1]
        
        def generate_palindromes(n):
            half_len = (n + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            palindromes = []
            for i in range(start, end):
                half = str(i)
                full = half + half[:-1][::-1] if n % 2 else half + half[::-1]
                if full[0] != '0':
                    palindromes.append(int(full))
            return palindromes
        
        from collections import Counter
        from math import factorial

        def count_valid_permutations(digits):
            cnt = Counter(digits)
            total = factorial(len(digits))
            for c in cnt.values():
                total //= factorial(c)
            invalid = 0
            for d in set(digits):
                if d == '0':
                    cnt[d] -= 1
                    temp_total = factorial(len(digits) - 1)
                    for c in cnt.values():
                        temp_total //= factorial(c)
                    invalid += temp_total
                    cnt[d] += 1
            return total - invalid

        palindromes = generate_palindromes(n)
        seen = set()
        count = 0

        for p in palindromes:
            if p % k != 0:
                continue
            key = tuple(sorted(str(p)))
            if key in seen:
                continue
            seen.add(key)
            count += count_valid_permutations(str(p))

        return count
