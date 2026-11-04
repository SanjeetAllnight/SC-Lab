def neuron(x1,x2,x3,w1,w2,w3,thres):
    total=(x1*w1+x2*w2+x3*w3)
    if total>=thres:
        return 1
    else:
        return 0
def XOR(x1,x2,x3):
    n1=neuron(x1,x2,x3,1,1,1,1)
    n2=neuron(x1,x2,x3,1,1,1,3)
    if n1==1 and n2==0:
        return 1
    else:
        return 0
while True:
    print("1.AND")
    print("2.OR")
    print("3.NAND")
    print("4.NOR")
    print("5.XOR")
    choice=int(input("Enter your choice: "))
    x1=int(input("Enter input 1 (0 or 1): "))
    x2=int(input("Enter input 2 (0 or 1): "))
    x3=int(input("Enter input 3 (0 or 1): "))
    match choice:
        case 1:
            w1=int(input("Enter weight 1 (1 or -1): "))
            w2=int(input("Enter weight 2 (1 or -1): "))
            w3=int(input("Enter weight 3 (1 or -1): "))
            print("AND Output= ",neuron(x1,x2,x3,w1,w2,w3,3))
        case 2:
            w1=int(input("Enter weight 1 (1 or -1): "))
            w2=int(input("Enter weight 2 (1 or -1): "))
            w3=int(input("Enter weight 3 (1 or -1): "))
            print("OR Output= ",neuron(x1,x2,x3,w1,w2,w3,1))
        case 3:
            w1=int(input("Enter weight 1 (1 or -1): "))
            w2=int(input("Enter weight 2 (1 or -1): "))
            w3=int(input("Enter weight 3 (1 or -1): "))
            print("NAND Output= ",neuron(x1,x2,x3,w1,w2,w3,-2))
        case 4:
            w1=int(input("Enter weight 1 (1 or -1): "))
            w2=int(input("Enter weight 2 (1 or -1): "))
            w3=int(input("Enter weight 3 (1 or -1): "))
            print("NOR Output= ",neuron(x1,x2,x3,w1,w2,w3,0))
        case 5:
            print("XOR Output= ",XOR(x1,x2,x3))
        case _:
            print("Invalid choice")
    c=input("Do you want to continue? (Y/N): ")
    if c!='Y' and c!='y':
        break