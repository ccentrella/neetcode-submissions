class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Create score stack
        # While iterating over operations, add/remove from stack:
        # - Integer: Append to stack
        # - +: Easiest way is to pop last item, then peek second last. Add back last. Also add back sum. Alternatively, we could hold two variables, but prefer usig stack only.
        # D: Inspect last item from stack then push double
        # C: Pop last item from stack

        # Pop each item in score stack and save in running counter

        score = []
        for item in operations:
            # Required to convert to int, otherwise python will use string overload for operators
            if item.lstrip("-").isdigit():
                score.append(int(item))
            elif item == "+":
                last = score.pop()
                second_last = score[-1]
                score.append(last)
                score.append(last + second_last)
            elif item == "D":
                last = score[-1]
                score.append(2*last)
            elif item == "C":
                score.pop()

        # Now add them up
        counter = 0
        print(score)
        for item in score:
            counter += item

        return counter



        # Start right to left
        # Add operator to pending stack until 