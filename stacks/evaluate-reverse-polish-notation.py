class Solution:
    def evalRPN(self, tokens) -> int:

        operate = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a/b) # don't ask it was a havoc
        }
        
        stack = []
        for token in tokens:
            if token not in operate:
                stack.append(int(token))
            else:
                b = stack.pop()  # Correctly pop the last two elements
                a = stack.pop()
                res = operate[token](a, b)
                stack.append(res)
        
        return stack[0]
                
print(
    Solution().evalRPN(
        tokens = 
        ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
    )
)