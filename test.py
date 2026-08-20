def mcp(x1,x2,x3,w1,w2,w3,threshold):
    s=x1*w1+x2*w2+x3*w3
    return 1 if s>=threshold else 0

x1=int(input("Enter x1: "))
x2=int(input("Enter x2: "))
x3=int(input("Enter x3: "))
w1=float(input("Enter w1: "))
w2=float(input("Enter w2: "))
w3=float(input("Enter w3: "))
threshold=float(input("Enter threshold: "))
print("Weighted Sum:",x1*w1+x2*w2+x3*w3)
print("Output:",mcp(x1,x2,x3,w1,w2,w3,threshold))