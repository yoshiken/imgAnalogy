## やり方

1. ./imgdataset に解析する画像を入れる
2. ` ./main.sh PythonCode ResultFolderName ` で第二引数のフォルダーに各画像ごとの"比較対象画像名,類似度"というcsvで出してくれる

e.g.) 
$./main.sh main.py res
$ tree
main.py
|- res
   |- img01
   |- img02
   |- img03
   |- … 
$cat img01
img01,1
img02,0.876
img03,0.123
…

実験で一回きりで実行できればいいやぐらいの気持ちなのでめちゃくちゃ雑に書いてある(ファイルは400固定とか色々)

## ファイル説明

### main .py

SHIFTとかSOFTとかにデコーダーをコメントアウトしてあるので外せば動く。たぶん。
主に物体認識が書いてある。

### histogram.py

名前の通りヒストグラムでやるやつ。
今白黒だからカラーにしたいよな。

## main.sh

第二引数のフォルダーがなかったら作る。あとはいい感じに画像名前順にソートしたりとかしてくれるやつ。

### k-means.sh

k-meansを実行するときのbashファイル
./kmeansres/以下の実行結果に対してk-meansを総当りでやる。

### k-means.py

k-meansやってくれるやつ

### histgram.py

ColorHistogramの比較を出してくれるやつ
実装は単純で、一つファイルを呼び出して他のファイルに対して総当りで比較するやつ

