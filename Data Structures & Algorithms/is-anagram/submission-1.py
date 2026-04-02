class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = sorted(set(s))
        set_t = sorted(set(t))
        if set_t != set_s:
            return False
        
        for c in set_s:
            if s.count(c) != t.count(c):
                return False
        
        return True
