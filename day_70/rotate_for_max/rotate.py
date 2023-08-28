def max_rot(n: int) -> int:
    n = str(n)
    max_num = int(n)

    for i in range(len(n)):
        n = n[:i] + n[i+1:] + n[i]
        if int(n) > max_num:
            max_num = int(n)
    
    return max_num