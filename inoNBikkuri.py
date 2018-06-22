import csv
import itertools

csv_file = open("input_0.csv","r", encoding="ms932",errors="",newline="")#csvファイルは適宜変える
f=csv.reader(csv_file, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',skipinitialspace=True)
header=next(f)
x=[]
y=[]
for row in f:
    rowlist=row[0].split(",")
    x.append(float(rowlist[0]))
    y.append(float(rowlist[1]))
# x=[x1,x2,x3,...]
# y=[y1,y2,y3,...]

dataLength=len(x)#=len(y)
indexs=range(0,dataLength)#indexs=[0,1,2,3...dataLength-1]

minimumCombi=[]
minimumDis=0
for combi in itertools.permutations(indexs):#すべての組み合わせを試す
    #combi=[4,2,0,3,1] (ex) 
    #combi[0]=4 (ex)
    #combi[1]=2 (ex)
    #combi[2]=0 (ex)
    #combi[3]=3 (ex)
    #combi[4]=1 (ex)
    #dis1=(x[combi[0]]-x[combi[1]])*(x[combi[0]]-x[combi[1]])+(y[combi[0]]-y[combi[1]])*(y[combi[0]]-y[combi[1]])

    #for distance
    param=0
    disz=[]#それぞれの二点間の距離の二乗を入れる用のリスト
    while param < dataLength-1:
        disz.append((x[combi[param]]-x[combi[param+1]])*(x[combi[param]]-x[combi[param+1]])+(y[combi[param]]-y[combi[param+1]])*(y[combi[param]]-y[combi[param+1]]))
        param+=1
    #一番最後と一番最初の点の距離の二乗だけ特別に計算
    disLast=(x[combi[0]]-x[combi[dataLength-1]])*(x[combi[0]]-x[combi[dataLength-1]])+(y[combi[0]]-y[combi[dataLength-1]])*(y[combi[0]]-y[combi[dataLength-1]])
    # それぞれの距離の二乗を足し合わせる
    totalDistance=disLast
    for dis in disz:
        totalDistance+=dis
    #最小距離(二乗距離の和)が初期値or今のトータル距離より大きい時、データを上書き
    if minimumDis == 0 or minimumDis > totalDistance:
        minimumCombi=combi
        minimumDis=totalDistance

    
print("index")
for number in minimumCombi:
    print(number)

    



    

