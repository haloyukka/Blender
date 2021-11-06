# 1行1列データ
入力
> N（文字列または数字）

```
# str型で受け取るとき
s = input()
# int型で受け取るとき
s = int(input())
# float型で受け取る時
s = float(input())
```
input()で受け取る型はすべてstr型になる。

# (1,N)行列データ
入力
> A B

入力が文字列の場合
入力例
> Alice Bob Charlie

コード例1
```
# list形で受け取るとき
s = input().split()

# 出力
>>>print(s)
['Alice', 'Bob', ''Charlie]
>>>print(s[0])
Alice
>>print(s[0][0])
A
```

コード例2
```
# 文字列として受け取るとき
A, B, C = input().split()

# 出力
>>>print(s)
Alice
>>>print(A,B,C)
Alice Bob Charlie
```

# 入力変数が整数の場合
入力例
> 1 3

コード例1
```
A, B = map(int, input().split())

# 出力
>>>print(s)
1
>>>print(A,B)
1 3
```

# 入力変数の数がN個の場合
入力
> A1 A2 A3 ... AN

入力例
> 1 3 4 5 6

コード例1
```
# list型で取得
l = list(map(int, input().split()))

# 出力
>>>print(l)
[1, 3, 4, 5, 6]

```

# 文字列と数字の複合
> N, S = map(str, input().split())

# (N, 1)行列データ
入力
> N M  
> A1  
> A2  
> ...  
> AN  

入力例
> 3 4  
> 2  
> 3  
> 3  
> 1  

コード例1(int型)  
空のリストを生成して上から順にリストへ格納することで、(N, 1)行列を(1, N)行列に変換する

```
N, M = map(int, input().split())
# 空のリスト
A = []
# リストAにappend()を使って格納していく
for _ in range(M):
    A.append(int(input())

# 出力
>>>print(A)
[2, 3, 3, 1]
```

コード例2(リスト内包表記)  
```
N, M = map(int, input().split())
# リスト内包表記
A = [int(input()) for _ in range(M)]

# 出力
>>>print(A)
[2, 3, 3, 1]
```

# (N, M)行列データ

# 2変数データ
行に変数が並ぶとき  
入力  
> N
> x1 x2 x3 ... xn  
> y1 y2 y3 ... yn  

入力例
> 3  
> 1 2 3  
> 4 5 6  

コード例
```
N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# 出力
>>>print(x)
[1, 2, 3]
```

# 列に変数が並ぶとき  
入力  
> N  
> x1y1  
> x2y2  
> ...
> nNyN

入力例  
> 5  
> 1 2  
> 3 4  
> 5 6  
> 7 8  
> 9 10  

コード例1 (x,yを独立に格納)
```
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

# 出力
>>>print(x)
[1, 3, 5, 7, 9]
>> print(x[1]+y[1])
7
```

コード例2 ([xi, yi]として格納)
```
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

# 出力
>>>print(l)
[[1, 2], [3, 4], [5, 6]]
```

# int型とstr型混合の場合
入力例  
> 5  
> 1 a  
> 3 b  
> 5 c  
> 7 d  
> 9 e  

```
N = int(input())
list = []
for i in range(N):
    a,b=input().split()
    list.append([int(a), b])

# 出力
>>>print(list)
[[1, 'a'], [3, 'b'], [5, 'c'], [7, 'd'], [9, 'e']]
>>>print(type(list[0][0]))
<class'int'>
>>>print(type(list[0][1]))
<class'str'>
```

# 3変数データ（データの数が変数ごとに異なる場合）
入力  
> X Y A B C  
> P1 P2 P3 ... PA  
> Q1 Q2 Q3 ... QB  
> R1 R2 R3 ... RC  


[E - Red and Green Apples](https://atcoder.jp/contests/abc160/tasks/abc160_e)

入力例  
> 1 2 2 2 1
> 2 4  
> 5 1  
> 3  
```
X, Y, A, B, C = map(int, input().split())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]
R = [int(i) for i in input().split()]

# 出力
>>>print(P)
[2, 4]

# この形でも問題ない
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
```

# 一般行列データ
入力  
> N M  
> A1,1 A1,2 ... A1,N  
> ...  
> AM,1 AM,2 ... AM,N  

入力例(3,3)行列データ  
>3 3  
>2 1 3  
>1 3 3  
>2 2 1  

コード例 (int型)
```
N, M = map(int, input().split())
# リスト内包表記
# 上から順にlistを読み込んでlistに格納していく。
a = [list(map(int, input().split())) for l in range(M)]

# 出力
>>>print(a)
[[2, 1, 3], [1, 3, 3], [2, 2, 1]]

>>>print(a[0])
[2, 1, 3]

>>>print(a[0][0])
2

>>>print(type(a[0][0])
<class'int'>)
```

# 補足-numpy-
numpyを使うとリストをnumpy配列ndarrayに変換できる。  
この変換を行うことで、行列演算だけでなく、実行速度を高速化、コードの簡略化を行うことができる
```
import numpy as np
# 任意のlist
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ndarrayに変換
list_ndarray = np.array(list)
>>>print(list_ndarray)
[[1 2 3]
 [4 5 6]
 [7 8 9]]

# 配列のサイズ（要素数）
>>>print(list_ndarray.size)
9
# 配列の形状
>>>print(list_ndarray.shape)
(3, 3)
# 型
>>>print(type(list_ndarray))
<class'numpy.ndarray'>

# numpy配列→リスト
list_list = list_ndarray.tolist()
>>>print(list_list)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>>print(type(list_list))
<class'list'>
```

# リンク
[Python3での標準入力まとめ](https://qiita.com/pyu666/items/6b8cfefc1ea994639683)  
[Python3で競技プログラミングする時に知っておきたいtips(入力編)](https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c)  
[競プロ等におけるpython3の標準入力](https://qiita.com/zenrshon/items/c4f3849552348b3dbe67)  
[python de 競技プログラミング](https://qiita.com/hahho/items/dcf482d43bc29ebfb53c)  


# 標準入力・標準出力について
[標準入力・標準出力ってなに?](https://qiita.com/angel_p_57/items/03582181e9f7a69f8168)  
