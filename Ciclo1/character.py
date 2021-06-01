""" import sys
line = sys.stdin.readline().strip().split(" ") """

if __name__ == "__main__":
    line = input()
    while (line != "0"):
        line = line.split()
        chain = line[1]
        g = len(chain) // int(line[0])
        nchain = chain[0: g]
        reverse = nchain[::-1]
        for n in range(g, len(chain), g):
            nchain = chain[n: n+g]
            nchain = nchain[::-1]
            reverse = reverse + nchain
        print(reverse)
        line = input()
