## やり方
1. ./imgdataset に解析する画像を入れる
2. main.pyで"ファイル名 特徴距離"が出力される。のでパイプでつなげたりして保存する。
3. がんばってソートする。
4. "cat sortout2  | cut -d' ' -f2 > hogehoge"　でファイル名順の特徴量を抽出できる
5. gurahu.pyでグラフ化ができる


## 使うと便利なやーつ

2行目だけ抜いてくれる

```
cat sortout2  | cut -d' ' -f2 > hogehoge
```


