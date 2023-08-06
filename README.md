# What Is This
コマンドラインから大量の画像を簡単に検索し、取得できるスクリプトです
AIなどの強化学習用の素材収集にぜひご利用ください！

# How To Use
### 事前準備
まず以下のコマンドを実行して必要なモジュールをインストールします。<br>
```
pip install -r req.txt
```
### 基本的な使い方
```
python main.py "いちょう 葉"
```
この場合は実行したディレクトリと同じ層に `output` フォルダが生成されその中に出力されます。<br>

### 出力先指定
```
python main.py "いちょう 葉" --output ./out/test/
```
```
python main.py "いちょう 葉" -o ./out/test/
```
この場合 `./out/test/` 内に出力されます。<br>

### 検索数指定
```
python main.py "いちょう 葉" --length 200
```
```
python main.py "いちょう 葉" --l 200
```
この場合デフォルトの出力先に200枚出力されます。
