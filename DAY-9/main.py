class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s_list) - 1

        is_vowel = vowels.__contains__

        while left < right:
            l_char, r_char = s_list[left], s_list[right]

            if not is_vowel(l_char):
                left += 1
            elif not is_vowel(r_char):
                right -= 1
            else:
                s_list[left], s_list[right] = r_char, l_char
                left += 1
                right -= 1

        return ''.join(s_list)
