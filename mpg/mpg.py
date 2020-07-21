import operator
class Mpg(object) :
    def __init__(self,mft,model,displ,year,cyl,trans,drv,cty,hwy,fl,clas):
        self.mft = mft
        self.model = model
        self.displ = float(displ)
        self.year = int(year)
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = int(cty)
        self.hwy = int(hwy)
        self.fl = fl
        self.clas = clas
        self.fuel = (self.hwy + self.cty) /2

    def __repr__(self):
        return "mtf : {}, model : {}, displ : {}, year : {}, cyl : {}, trans : {}".format(self.mft,self.model,self.displ,
                                                                                         self.year,self.cyl,self.trans) + "drv : {}, cty : {}, hwy : {}, fl : {}, class : {}".format(self.drv,self.cty,self.hwy,self.fl,self.clas)



#txt file read
file1 = open("C:/test/mpg.txt","r")
mpg_list = []
for i in file1 :
    str = i.strip("\n").split(",")
    if str[0] == "manufacturer" :
        continue
    mpg_list.append(Mpg(str[0],str[1],str[2],str[3],str[4],str[5],str[6],str[7],str[8],str[9],str[10]))


file1.close()

#make manufacturer_list
mft_list = set([tmp.mft for tmp in mpg_list])


def avg(arg) :
    return round(sum(arg) / len(arg),2)

########
#문제 1

displ4_list = [tmp.hwy for tmp in mpg_list if tmp.displ < 5]
displ5_list = [tmp.hwy for tmp in mpg_list if tmp.displ > 4]

displ4_result = avg(displ4_list)
displ5_result = avg(displ5_list)

print("문제 1 : displ 4이하 평균hwy : {} , 5이상 평균 hwy : {}".format(round(displ4_result,1), round(displ5_result,1)))

########
#문제 2
cty_audi_list = [tmp.cty for tmp in mpg_list if tmp.mft == "audi"]
cty_toyota_list = [tmp.cty for tmp in mpg_list if tmp.mft == "toyota"]

cty_audi = avg(cty_audi_list)
cty_toyota = avg(cty_toyota_list)

print("문제 2 : audi 평균cty : {} , toyota 평균cty : {}".format(round(cty_audi,1), round(cty_toyota,1)))

########
#문제 3
hwy_chevrolet_list = [tmp.hwy for tmp in mpg_list if tmp.mft == "chevrolet"]
hwy_ford_list = [tmp.hwy for tmp in mpg_list if tmp.mft == "ford"]
hwy_honda_list = [tmp.hwy for tmp in mpg_list if tmp.mft == "honda"]

result_hwy_chevrolet = avg(hwy_chevrolet_list)
result_hwy_ford = avg(hwy_ford_list)
result_hwy_honda = avg(hwy_honda_list)

print("문제 3 : chevrolet 평균hwy : {} , ford 평균hwy : {}, honda 평균hwy : {}".format(round(result_hwy_chevrolet,1),
                                                                               round(result_hwy_ford,1), round(result_hwy_honda,1)))

########
#문제 4
audi_list = [tmp for tmp in mpg_list if tmp.mft == "audi"]

result = sorted(audi_list,key=lambda  mpg :  mpg.hwy, reverse=True)

print("문제4 : audi hwy 1~5위\n 1위 {}\n 2위 {}\n 3위 {}\n 4위 {}\n 5위 {}".format(result[0],result[1],result[2],result[3],result[4]))

#########
#문제 5
suv_list = [tmp for tmp in mpg_list if tmp.clas == "suv"]

print("문제5")
for i in mft_list :
    tmp_list = [tmp for tmp in suv_list if tmp.mft == i]

    result = sorted(tmp_list, key= lambda tmp : (tmp.hwy+tmp.cty) /2, reverse= True)
    try :
        print(
            "{} hwy 1~5위\n 1위 {}\n 2위 {}\n 3위 {}\n 4위 {}\n 5위 {}".format(i, result[0], result[1], result[2], result[3],
                                                                         result[4]))
    except Exception :
        continue

#######
#문제 6

clas_list = set([tmp.clas for tmp in mpg_list])

def avg_cty(clas) :
    tmp_list = [tmp.cty for tmp in mpg_list if tmp.clas == clas]

    return avg(tmp_list)
result = {}
for i in clas_list :
    result[i] = avg_cty(i)

result = sorted(result.items(),key=lambda x:x[1],reverse=True)
print("문제6")
for i in result :
    print("{} : {}, ".format(i[0],i[1]),end=" ")

#######
#문제 7
def avg_hwy(mft) :
    tmp_list = [tmp.hwy for tmp in mpg_list if tmp.mft == mft]

    return avg(tmp_list)

result = {}
for i in mft_list :
    result[i] = avg_hwy(i)



result = sorted(result,key=lambda x:x[1],reverse=True)

print("\n문제7 : 1위 {}, 2위 {}, 3위 {}".format(result[0],result[1],result[2]))
##########
#문제8
result = {}
def compact(mft) :
    tmp_list = [tmp.clas for tmp in mpg_list if tmp.mft == mft and tmp.clas == "compact"]

    return len(tmp_list)

for i in mft_list :
    result[i] = compact(i)

result = sorted(result.items(),key=lambda x:x[1],reverse=True)

print("문제8 : {}".format(result))
