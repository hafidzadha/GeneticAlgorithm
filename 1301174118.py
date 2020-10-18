import runpy
import random
import math as mt


def generate():
    angka = []
    x = 1
    for x in range(10):
        p = list(range(0, 9))
        hasil = random.sample(p, k=6)
        angka.append(hasil)
    return angka

def dec_kromosom(angka):
    dec_rslt = []
    for s in angka:
        x1 = -1+(((1+2)/(9*(pow(10,-1)+pow(10,-2))))*(s[0]*pow(10,-1)+s[1]*pow(10,-2)))
        x2 = -1+(((1+1)/(9*(pow(10,-1)+pow(10,-2))))*(s[2]*pow(10,-1)+s[3]*pow(10,-2)))
        dec_rslt.append([x1,x2])
    return dec_rslt

def dec1(s):
    x1 = -1+(((1+2)/(9*(pow(10,-1)+pow(10,-2))))*(s[0]*pow(10,-1)+s[1]*pow(10,-2)))
    x2 = -1+(((1+1)/(9*(pow(10,-1)+pow(10,-2))))*(s[2]*pow(10,-1)+s[3]*pow(10,-2)))
    return x1,x2

def fitness_count(dec_rslt):
    fit = []
    fitness=[]
    for q in dec_rslt:
        a =  mt.cos(q[0])*mt.sin(q[1])-(q[0]/(pow(q[1],2)+ 1))
        fit.append(a)

    for w in fit:
        b = 1/(w+10)
        fitness.append(b)
    return fitness

    
def bestFitness(fitness):
   max = 0
   idx = 0
   for i in range(len(fitness)):
     if fitness[i] > max:
        max = fitness[i]
        print("==============")
        print(fitness[i])
        print("==============")
        idx = i
   print(max)
   return max,idx 

def bestKromosom(max,fitnesslist,pop):
    idx=-1
    for i in range(len(fitnesslist)):
        if max == fitnesslist[i]:
            idx = i
    return pop[idx]

def bestValue(krom):
    x1 = -1+(((1+2)/(9*(pow(10,-1)+pow(10,-2))))*(krom[0]*pow(10,-1)+krom[1]*pow(10,-2)))
    x2 = -1+(((1+1)/(9*(pow(10,-1)+pow(10,-2))))*(krom[2]*pow(10,-1)+krom[3]*pow(10,-2)))
    a =  mt.cos(x1)*mt.sin(x2)-(x1/(x2**2 + 1))
    return a,x1,x2

def value(x1,x2):
    h = mt.cos(x1)*mt.sin(x2)-(x1/(x2**2 + 1))
    return  h

def orang_tua(fitness):
    total = 0
    for x in fitness:
        total += x   
    i =[]
    for q in range(2):
        r = random.random()
        indv = 0  
        while (r > 0) and (indv <= 8):
            r -= fitness[indv] / total
            indv = indv + 1
        i.append(indv)
    return i

def search(angka,index):
    p1 = index[0]
    p2 = index[1]
    crs1 = angka[p1]
    crs2 = angka[p2]
    return crs1,crs2

def crossover(p1,p2):
    duarr =  random.randint(0,3)
    prob = random.random()
    if prob<0.1:
        if duarr==3:
            p1[3],p2[3] = p2[3],p1[3]
            return p1,p2
        elif duarr==2:
            p1[3],p2[3],p1[2],p2[2] = p2[3],p1[3],p2[2],p1[2]    
            return p1,p2
        elif duarr==1:
            p1[3],p2[3],p1[2],p2[2],p1[1],p2[1] = p2[3],p1[3],p2[2],p1[2],p2[1],p1[1]
            return p1,p2
        elif duarr==0:
            p1[3],p2[3],p1[2],p2[2],p1[1],p2[1],p1[0],p2[0] = p2[3],p1[3],p2[2],p1[2],p2[1],p1[1],p2[0],p1[0]
            return p1,p2
    else:
        return p1,p2
    

def mutasi(p1,p2):
    hasil_mutasi = []
    for i in range(len(p1)):
        chance = random.random()
        if chance < 0.1:
            p1[i]=random.randint(0,9)

    for j in range(len(p2)):
        chance1 = random.random()
        if chance1 < 0.1:
            p2[j]=random.randint(0,9)
    hasil_mutasi.append(p1)
    hasil_mutasi.append(p2)
    return hasil_mutasi

pop = generate()
decode = dec_kromosom(pop)
fitness=fitness_count(decode)
 
print("POPULASI AwAL : ",pop)
print("====================")
gen = 0
bestGlobal = bestFitness(fitness)
while gen <= 1000:
    arrSimpan = []
    for x in range(5):
        decode = dec_kromosom(pop)
        fitness=fitness_count(decode)
        idx = orang_tua(fitness)
        p1,p2=search(pop,idx)
        anak1,anak2=crossover(p1,p2)
        hasil_mutasi=mutasi(anak1,anak2)
        arrSimpan.append(hasil_mutasi[0])
        arrSimpan.append(hasil_mutasi[1])
    pop = arrSimpan
    decode = dec_kromosom(pop)
    fitness=fitness_count(decode)
    bestLokal = bestFitness(fitness)
    
    print(bestLokal[0])
    if  bestLokal[0] > bestGlobal[0]:
        bestGlobal = bestLokal
        popGlobal = bestKromosom(bestGlobal,fitness,pop)
        bestVal,x1,x2 = bestValue(popGlobal)
    gen+=1

print("==============")
print("fitness terbaik : ",bestGlobal)
print("kromosom terbaik : ",popGlobal)
print("nilai paling minimum : ",bestVal)
print("nilai x1 : ",x1)
print("nilai x2 : ",x2)