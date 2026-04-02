class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stack = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in stack:
                stack[key] = []
            stack[key].append(word)
        return list(stack.values())
            