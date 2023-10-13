infix = input()
postfix = ""
stack = []

for ch in infix:
    if ch.isalpha(): 
        postfix += ch
    elif ch == '(':  
        stack.append(ch)
    elif ch == ')':  
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()  
    else:  
        while stack and stack[-1] in "*/+-":
            if stack[-1] in "*/" and ch in "*/+-":
                postfix += stack.pop()
            elif stack[-1] in "+-" and ch in "+-":
                postfix += stack.pop()
            else:
                break
        stack.append(ch)

while stack:
    postfix += stack.pop()

print(postfix)
