class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        list_s = list(s)
        list_t = list(t)


        for letter in list_s:
            if letter not in hash_s:
                hash_s[letter] = 1
            else:
                hash_s[letter] += 1

        for letter in list_t:
            if letter not in hash_t:
                hash_t[letter] = 1
            else:
                hash_t[letter] += 1

        if hash_s == hash_t:
            return True
        return False
        