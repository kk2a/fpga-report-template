# fpga-report-template

fpgaのレポートで使用したテンプレート．

# 使い方

1. このリポジトリをクローンする．
2. 同じディレクトリに，第 $n$ 回のレポートに使う写真とか，texファイルを置くためのフォルダを作成する (スニペットはこれを想定しています．) ．
3. .vscodeが反映されるように，うまくtexファイルを開いて，\usepackage{../fpga}をする．

## pdfcombiner.py

texで作ったpdfと，表紙のpdfを結合するためのファイル．

```bash
python pdfcombiner.py
```

をすればいい感じのウィンドウが出てきます．

# 注意

- LuaLaTeXでビルドすることを想定しています (LaTeX Workshopの設定を.vscode/settings.jsonに置いときます．) ．私は[このサイト](https://qiita.com/passive-radio/items/623c9a35e86b6666b89e)を見て環境構築しましたが，settings.jsonの部分が微妙にうまくいかないので，そこだけ注意すれば簡単に一から環境構築できると思います．
