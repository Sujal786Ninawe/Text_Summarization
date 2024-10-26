def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        
        s = int(data[index], 2)
        index += 1
        
        a = []
        for _ in range(n):
            a.append(int(data[index], 2))
            index += 1
            
        total_sum = sum(a)
        
        target = total_sum ^ s
        
        if target % n == 0:
            x = target // n
            x_binary = bin(x)[2:]
            if len(x_binary) > k:
                results.append('-1')
            else:
                x_binary = x_binary.zfill(k)
                results.append(x_binary)
        else:
            results.append('-1')
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()
