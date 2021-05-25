from functools import reduce
if __name__ == "__main__":
    k = int(input())
    a = input().split()
    b = input().split()
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    c = [abs(a - b) for (a, b) in zip(a, b)]
    sumFirst = reduce(lambda a, b: a + b, c)
    index = c.index(max(c))
    indexb = b.index(max(b))
    if (index == indexb):
        indexb = a.index(max(a))
    first = b[index]
    second = b[indexb]
    b[index] = second
    b[indexb] = first
    c = [abs(a - b) for (a, b) in zip(a, b)]
    sumSecond = reduce(lambda a, b: a + b, c)
    if(sumFirst > sumSecond):
        print(sumSecond)
    else:
        print(sumFirst)
