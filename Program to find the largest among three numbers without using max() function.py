def maximum(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
result=maximum(25,40,19)
print("Largest number is ",result)