def find_prime(num) :
    elem = [2]
    tmp = 2
    while True :
        count = 0
        for i in elem :
            if tmp % i == 0 :
                count += 1
                break
        if count == 0 :
            elem.append(tmp)


        if len(elem) >= num :
            break
        tmp += 1

    return elem[num-1]



num = 600851475143
elem = []
tmp_list = []
tmp = 2
while True :
    count = 0
    for i in elem:
        if tmp % i == 0:
            count += 1
            break
    if count == 0:
        elem.append(tmp)
        if num % tmp == 0 :
            num /= tmp
            tmp_list.append(tmp)
    if num == 1 :
        break
    tmp += 1

print(max(tmp_list))