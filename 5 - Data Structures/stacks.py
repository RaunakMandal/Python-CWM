stk = []
stk.append(1)
stk.append(2)
stk.append(3)
print(stk)

print(stk.pop())
print("Redirect", stk[-1])

if not stk:
    print(stk[-1])
