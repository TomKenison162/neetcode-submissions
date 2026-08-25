class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dicts = {"+": lambda x, y : x + y, "*": lambda x, y : x * y, "/": lambda x, y : int(x / y), "-": lambda x, y : x - y }
        
    
        for i in range(0, len(tokens)):

           
            if dicts.get(tokens[i], -1) != -1:
                prev = stack.pop()
                stack.append(dicts[tokens[i]](stack.pop(), prev))
            else:
                stack.append(int(tokens[i]))
        print(stack)
        return round(stack[0])

                

        