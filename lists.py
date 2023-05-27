if __name__ == '__main__':
    N = int(input())
    operand = []
    for i in range(N):
        operation = input()
        operation = operation.split()
        if operation[0] == 'insert':
            ind = int(operation[1])
            n = int(operation[2])
            operand.insert(ind,n)
        elif operation[0] == "print":
            print(operand)
        elif operation[0] == "remove":
            n = int(operation[1])
            operand.remove(n)
        elif operation[0] == "append":
            n = int(operation[1])
            operand.append(n)
        elif operation[0] == "sort":
            operand.sort()
        elif operation[0] == "pop":
            operand.pop()
        elif operation[0] == "reverse":
            operand.reverse()
            