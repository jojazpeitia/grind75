class Solution:
    def isValid(self, s: str) -> bool:
        # create dictionary to help us find pairs fast
        dict1 = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []
        # cannot start with right bracket
        # right bracket must be next to another right bracket or matching
        # if matching bracket pop from the stack

        for i in s:
            # if non empty and i matches the top
            if stack and stack[-1] == dict1.get(i):
                stack.pop()
                continue

            # if unmatching right brace
            if stack and i in dict1.keys() and stack[-1] != dict1.get(i):
                return False

            # if left bracket append
            if i in dict1.values():
                stack.append(i)

            # if right brace and we put on empty stack
            if i in dict1.keys() and len(stack) == 0:
                return False

        if len(stack) == 0:
            return True 
            