class Solution:
    def isValid(self, s: str) -> bool:
        # Create stack data structure
        # For open brackets, add to the stack
        # For closed bracket, confirm it matches the last open bracket
        # If it does not, then return False
        # Otherwise we will pop it
        # If stack is empty, return True. Else, false.

        stack = []
        mapping = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for char in s:
            if char in ('[', '{', '('):
                stack.append(char)
            elif len(stack) == 0 or stack.pop() != mapping[char]:
                return False

        return len(stack) == 0
                