# TSP Challenges  [Team: Python4]
(Google STEP 2018: Traveling Salesman Problem Challenges)

## Member
[Mamiko Ino](https://github.com/p623)/[KyokoMuto](https://github.com/KyokoMuto)/[momo](https://github.com/pes-ca)/[snknokw8048](https://github.com/snknokw8048)/[Nasa](https://github.com/labrador1)/[Nawoko](https://github.com/Nawoko)


## Link
- [Scoreboard]
- [GitHub Issues]

[scoreboard]:
  https://docs.google.com/spreadsheets/d/1Aa_NNQf7sFANuHKt0FTvUBQ83QO3OOKZjifhsmjOxqc/edit?usp=sharhing
[github issues]: https://github.com/hayatoito/google-step-tsp/issues


## Description
焼きなまし法による、巡回セールスマン問題解決のアルゴリズムを用いて求めた値に、2opt、3opt法を用いて値の更新を行い、最小値を求めた．

焼きなまし法とは
[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem):
>焼きなまし法（やきなましほう、英: Simulated Annealing、SAと略記、疑似アニーリング法、擬似焼きなまし法、シミュレーティド・アニーリングともいう）は、大域的最適化問題への汎用の乱択アルゴリズムである．広大な探索空間内の与えられた関数の大域的最適解に対して、よい近似を与える．
SAアルゴリズムは、解を繰り返し求め直すにあたって、現在の解のランダムな近傍の解を求めるのだが、その際に与えられた関数の値とグローバルなパラメータ T（温度を意味する）が影響する．そして、前述の物理過程との相似によって、T（温度）の値は徐々に小さくなっていく．このため、最初はTが大きいので、解は大胆に変化するが、Tがゼロに近づくにつれて収束していく．最初は簡単に勾配を上がっていけるので、山登り法で問題となるようなローカルな極小に陥ったときの対処を考える必要がない．

2opt:
下図のようにルートが交差している場合にはランダムな二点の選択では改善できないため、二点を選択した後それぞれの後の値を入れ替えた後の値が小さければ値の更新を行った．
https://cdn-ak.f.st-hatena.com/images/fotolife/y/y_uti/20171111/20171111095242.png

3opt:
2optでは２本の枝での入れ替えを行ったが、3optでは３本の枝で入れ替えを行った．入れ替えた後の３通りの値のなかにもとの値より小さいものが存在すれば値の更新を行った．



## Problem Statement

In this assignment, you will design an algorithm to solve a fundamental problem
faced by every travelling salesperson, called _Travelling Salesman Problem_
(TSP).  TSP is very famous problem. See
[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem). You can　understand the problem without any difficulties.

Quoted from
[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem):

> The travelling salesman problem (TSP) asks the following question: Given a
> list of cities and the distances between each pair of cities, what is the
> shortest possible route that visits each city exactly once and returns to the
> origin city?


## Requirement
Python3
