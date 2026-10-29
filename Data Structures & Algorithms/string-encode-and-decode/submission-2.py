class Solution:

    def encode(self, strs: List[str]) -> str:
        strs = [f'{len(s)}#{s}' for s in strs]
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        index = 0
        words = []
        while index < len(s):
            delimiter = s.find('#', index)
            length = int(s[index:delimiter])
            stop = delimiter + 1 + length
            words.append(s[delimiter+1:stop])
            
            index = stop
        
        return words