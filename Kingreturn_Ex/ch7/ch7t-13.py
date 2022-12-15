flag = 2
prime_number = []
while len(prime_number) < 20:
    if flag == 2: # 2是質數
        prime_number.append(flag)
    for i in range(2, flag):
        if flag % i == 0:
            break
        elif i == flag - 1:
            print('i=%d,flag=%d' % (i,flag))
            prime_number.append(flag)
    flag += 1
print(prime_number)
