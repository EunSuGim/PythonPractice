#문제 4
#세자리 수 곱 대칭수 중 가장 큰것

def symmetry(minimum,maxinum) :
    symmetry_list = list()

    for i in range(minimum,maxinum) :
        for j in range(minimum,maxinum) :
            if i*j > 99999 :
                str_num = str(i*j)
                if str_num[0] == str_num[5] and str_num[1] == str_num[4] and str_num[2] == str_num[3] :
                    symmetry_list.append(int(str_num))

    return symmetry_list

#문제 5
#1~20모두 나누어떨어지는것



class Lcm() :

    test = 2
    def __init__(self,pre_num, next_num):
        self.result = 1
        for i in range(pre_num, next_num):
            self.result = Lcm.lcm(self.result,i)

    def lcm(pre_num, next_num):
        return pre_num * next_num / Lcm.gcd(pre_num, next_num)

    def gcd(high_num, low_num):
        tmp = 0
        tmp1 = high_num
        tmp2 = low_num

        while True:
            tmp = tmp1 % tmp2
            if tmp == 0:
                break
            tmp1 = tmp2
            tmp2 = tmp
        return tmp2

#문제 6
#10001번째 소수
#
# elem = [2]
# for i in range(3,20) :
#     for j in range(2,i) :
#         if i % j == 0 :
#             break
#         elif j == i-1 :
#             elem.append(i)

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

print(find_prime(10001))

