class Solution:

    def encode(self, strs: List[str]) -> str:
        strs = [f'{len(s)}{s}' for s in strs]
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        index = 0
        words = []
        while index < len(s) - 1:
            length = int(s[index])
            end = index + 1 + length
            words.append(s[index+1:end])
            index = end
        
        return words