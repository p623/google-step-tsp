import itertools
import random
#----------------------------↓solver_greedy.py------------------------------
import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    print("-----print greedyTour-----")
    print(tour)
    return tour
#----------------------------↑solver_greedy.py------------------------------
def makeTour(cities):#道順の初期値をランダムに(テキトーに決めてくれる)
    firstTour=[]
    citiesNumber=len(cities)
    citiesNumberIndex=list(range(0,citiesNumber))
    while True:
        if citiesNumberIndex==[]:
            break
        choicedNumber=random.choice(citiesNumberIndex)
        firstTour.append(choicedNumber)
        citiesNumberIndex.remove(choicedNumber)
    return firstTour


def calcuDist(cities,tour):#道順を与えると、トータル距離を計算してくれる
    allDist=0
    param=0
    while param < len(tour)-1:
        city1Number=tour[param]
        city2Number=tour[param+1]
        allDist+=distance(cities[city1Number],cities[city2Number])
        param+=1
    allDist+=distance(cities[tour[0]],cities[tour[len(tour)-1]]) #distance of first city to last city
    return allDist


def annealingoptimize(cities,firstTour,firstDist,distGreedy,T=100000, cool=0.99):#hill climb(?) or yakinamasi部分

    #初期値
    totalDist=firstDist
    tour=firstTour
    while T>0.0001:
        #値を交換する二つのindexの組み合わせをランダムに決める
        #下記テキトーな二つのcityを入れ替えるための操作
        citiesNumber=len(cities)
        citiesNumberIndex=(list(range(0,citiesNumber)))
        choicedCombi=random.sample(citiesNumberIndex,2)
        index0=choicedCombi[0]
        index1=choicedCombi[1]
        a=tour[index0] #選ばれたindexのcity
        b=tour[index1] #選ばれたindexのcity2
        calculatedTour=[]

        for city in tour:
            calculatedTour.append(city)
        
        calculatedTour[index1]=a
        calculatedTour[index0]=b
        #このcalculatedTourがテキトーに二点のcityを入れ替えた後の道順
        newTotalDist=calcuDist(cities,calculatedTour)
        #↓これの#消すと焼きなましに(?)、pの決め方テキトーです、ググってテキトーに決めた
        #p= pow(math.e, -abs(newTotalDist-totalDist)/T)

        if newTotalDist<totalDist:# or random.random()<p: #←これの#消すと焼きなましに(?)
            tour=calculatedTour
            totalDist=newTotalDist

        T=T*cool
    
    if totalDist>distGreedy:#Greedyより結果が悪かったらやり直す
        makeTour(cities)
        annealingoptimize(cities,tour,firstDist,distGreedy)
    else:
        print("--------the best tour by hill climb---------")
        print(tour)
        print("-------print totalDist--------")
        print(totalDist)
        return tour
        

#----------------------------↓forMain ------------------------------
if __name__ == '__main__':
    #assert len(sys.argv) > 1
    #tour = solve(read_input(sys.argv[1]))
    #print_tour(tour)
    assert len(sys.argv) > 1
    cities=read_input(sys.argv[1])
    tourGreedy = solve(cities)
    distGreedy=calcuDist(cities,tourGreedy)
    print("-----print distGreedy------")
    print(distGreedy)#ここまでgreedyの実行(別にgreedyの実行は必要ないです、greedyによる算出結果が欲しかっただけ)

    firstTour=makeTour(cities)
    firstDist=calcuDist(cities,firstTour)
    annealingoptimize(cities,firstTour,firstDist,distGreedy)
   
#----------------------------↑forMain------------------------------


#-----------------↓コメント-------------------
#よくわからない....
#なんか16以上がかなり重くなる...
#何回か実行すると割と良さげな値が出る(?)
#多分、greedyよりよくなかったらやり直すってとこが重そう
#月以降、あんまり時間取れないからあげちゃった
#勝手にやってごめん...
#何なら無視しちゃって大丈夫だよー！！！

#-----------------↑コメント-------------------

#------------------↓問題点----------------------
#初期値も毎回の山登りのためにランダムに更新しているけど、その意味あるのかわからない
#Tの値はもっと大きい方がいいのか、小さい方がいいのかわからない
#コードに無駄があると思われる
#何回か "$ python inoYaki.py input_n.csv" を実行しないと、最短?(sample/saのoutput)が得られない(n=0,1,2)
#何回か $ python inoYaki.py input_n.csv" を実行しても、最短?(sample/saのoutput)が得られない(n=3)
# "$ python inoYaki.py input_n.csv" を実行すると謎のエラーが出る(n>=4)
#以下、そのエラー文の添付(たぶん、何回も繰り返し呼ばれすぎたことによるエラーかな???)
#Traceback (most recent call last):
  #File "inoYaki.py", line 119, in <module>
    #annealingoptimize(cities,firstTour,firstDist,distGreedy)
  #File "inoYaki.py", line 96, in annealingoptimize
    #annealingoptimize(cities,tour,firstDist,distGreedy)
  #File "inoYaki.py", line 96, in annealingoptimize
    #annealingoptimize(cities,tour,firstDist,distGreedy)
  #File "inoYaki.py", line 96, in annealingoptimize
    #annealingoptimize(cities,tour,firstDist,distGreedy)
  #[Previous line repeated 985 more times]
  #File "inoYaki.py", line 71, in annealingoptimize
    #choicedCombi=random.sample(citiesNumberIndex,2)
  #File "/Users/p/.pyenv/versions/3.6.3/lib/python3.6/random.py", line 310, in sample
    #if isinstance(population, _Set):
  #File "/Users/p/.pyenv/versions/3.6.3/lib/python3.6/abc.py", line 188, in __instancecheck__
    #subclass in cls._abc_negative_cache):
  #File "/Users/p/.pyenv/versions/3.6.3/lib/python3.6/_weakrefset.py", line 75, in __contains__
    #return wr in self.data
#RecursionError: maximum recursion depth exceeded in comparison
#------------------↑問題点----------------------
