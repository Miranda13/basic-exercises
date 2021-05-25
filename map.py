if __name__ == "__main__":
    k = int(input())
    while (k != 0):
        reference = input().split()
        N = int(reference[0])
        M = int(reference[1])
        for n in range(0, k):
            coordinate = input().split()
            X = int(coordinate[0])
            Y = int(coordinate[1])
            if (X == N or Y == M):
                print('divisa')
            elif (X > N):
                if (Y > M):
                    print('NE')
                else:
                    print('SE')
            else:
                if (Y > M):
                    print('NO')
                else:
                    print('SO')
        k = int(input())