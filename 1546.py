N = int(input())

for i in range(N):
    K = int(input())
    for j in range(K):
        feed = int(input())

        if feed == 1:
            print("Rolien")
        elif feed == 2:
            print("Naej")
        elif feed == 3:
            print("Elehcim")
        else:
            print("Odranoel")