t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    

    blacks = (n + 1) // 2  
    whites = (n - 1) // 2  
    
    if x >= blacks and y >= whites:
        print("YES")
    else:
        print("NO")
