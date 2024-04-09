def string_reverse(s):

    str=""
    
    for i in s:
        str = i + str
    
    return str

s=str(input("Input any string: "))

print("Your string is: ",s)

print("Your string reversed is: ",string_reverse(s))