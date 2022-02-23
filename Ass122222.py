n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=' ')
    for k in range(1,j+1):
        print("*",end=" ")
    print('\n')
for i in range(1,n):
    for j in range(0,i):
        print(end=' ')
    for k in range(0,n-i):
        print("*",end=" ")
    print('\n')
