# ABC 081 B - Shift Only 
## 問題概要
黒板に N 個の正の整数 A_1,…,A_N が書かれています。
すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。

* 黒板に書かれている整数すべてを，2で割ったものに置き換える。

すぬけ君は最大で何回操作を行うことができるかを求めてください。

## 制約
* 1≤N≤200
* 1≤A_i≤10^9

## 数値例
* 　N=3

A=(16,12,24) 答え: 2

1回操作を行うと (8, 6, 12) になります。2回操作を行うと (4, 3, 6) になります。2個目の3が奇数なため 3回目の操作は行えません。

## 別解
###　コード
```bash
n = int(input())
a = list(map(int, input().split()))

ans = float("inf")

for i in a:
    ans = min(ans, len(bin(i)) - bin(i).rfind("1") - 1) # (1)…2で割った回数が最小のものを探索
print(ans)
```
###　解説
ポイントは(1)なのでここだけ解説。

* ①len(bin(i))

len()は文字列の長さを出力。

bin()は引数を２進数に変換して出力。

⇒つまりlen(bin(i))は入力iの２進数の桁数を算出する。

　例えば、len(bin(8))⇒0b1000、len(bin(5))⇒0b101となる。※2進数の場合、先頭に0bが入るようだ。


* ②bin(i).rfind("1")

rfindは1の文字を右から数えて何文字目かを出力。

⇒つまりbin(i).rfind("1")で入力iが最初に右から１がでるのは何桁目か？を算出する

　例えば、bin(i).rfind("1")⇒0b1000(=2)、bin(i).rfind("1")⇒0b101(=4)となる。

※rfindは右から数えるけど、出力する桁数は左から数えるのと０から数え始めるのでちょっと混乱しちゃうので注意


* ③len(bin(i)) - bin(i).rfind("1") - 1

①②を組み合わせて、何回２で割り続けられるかがわかる。

例えばi = 10の場合を考えると…

2で割り続けると、10⇒5⇒×で1回

このとき何がおきてるかっていうと2進数で見てみるとよくわかる。

* 10⇒1010
* 5 ⇒101

となっており、つまり何回２で割り続けることができるかは右の０の個数を数えればよいということがわかる。

なので…

③は①-②-1をしてやることで、この右の０の個数がいくつになるのかを導いているためにやっていることがわかる。

* ④ans = min(ans, len(bin(i)) - bin(i).rfind("1") - 1)

そもそもの出題は
黒板に書かれている整数すべてを，2 で割ったものに置き換える。

とあるが、これは言い換えると
２で割り続けて１つでも奇数がでてきたら終了する
ということを表している。

N個の正の整数 A1,…,AN のなかで最初に２で割り続けられなくなる数を探すので
forで回して１つ１つ2で割り切れる回数を算出して最も少ない数を探している