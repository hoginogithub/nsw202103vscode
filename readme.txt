日経ソフトウェア３月号
PythonユーザーのためのVisualStudioCode活用術

[前提]
・GitHub
https://github.com/hoginogithub/nsw202103vscode.git

・仮想環境作成

・Anacondaのインストール
(インストール方法参考ページ)
https://qiita.com/KntKnk0328/items/79782da809a7ee558a73

(Anaconda install元)
https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.pkg

[クローン]
git clone https://github.com/hoginogithub/nsw202103vscode.git nsw202103vscode

[作業環境へ移動]
cd nsw202103vscode

[環境作成]
>conda create -n nsw202103vscode python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/hogino/opt/anaconda3/envs/nsw202103vscode

  added / updated specs:
    - python=3.8


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/osx-64::ca-certificates-2021.1.19-hecd8cb5_1
  certifi            pkgs/main/osx-64::certifi-2020.12.5-py38hecd8cb5_0
  libcxx             pkgs/main/osx-64::libcxx-10.0.0-1
  libffi             pkgs/main/osx-64::libffi-3.3-hb1e8313_2
  ncurses            pkgs/main/osx-64::ncurses-6.2-h0a44026_1
  openssl            pkgs/main/osx-64::openssl-1.1.1k-h9ed2024_0
  pip                pkgs/main/osx-64::pip-21.0.1-py38hecd8cb5_0
  python             pkgs/main/osx-64::python-3.8.8-h88f2d9e_4
  readline           pkgs/main/osx-64::readline-8.1-h9ed2024_0
  setuptools         pkgs/main/osx-64::setuptools-52.0.0-py38hecd8cb5_0
  sqlite             pkgs/main/osx-64::sqlite-3.35.2-hce871da_0
  tk                 pkgs/main/osx-64::tk-8.6.10-hb0a8c7a_0
  wheel              pkgs/main/noarch::wheel-0.36.2-pyhd3eb1b0_0
  xz                 pkgs/main/osx-64::xz-5.2.5-h1de35cc_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate nsw202103vscode
#
# To deactivate an active environment, use
#
#     $ conda deactivate


[環境有効化]
conda activate nsw202103vscode

[パッケージのインストール]
conda install PK名

notebook

Flask
LightGBM(機械学習フレームワーク)
pandas
matplotlib

[VScode起動コマンド作成]
touch start_vscode.command

chmod 744 start_vscode.command

vi start_vscode.command
------------
#!/bin/zsh
CURRENT=$(cd $(dirname $0);pwd)
cd $CURRENT

source ~/opt/anaconda3/etc/profile.d/conda.sh
conda init zsh
conda activate nsw202103vscode

git pull
code .
------------

[データ]
・日経ソフトウェア３月号のサイトからonsen-data.csvをダウンロード
　t32103で展開
https://4c281b16296b2ab02a4e0b2e3f75446d.cdnext.stream.ne.jp/itpro/nsw/202103/t32103.zip


[VScode]
・command+Shift+P 
  Jyupter: Create New Blank Jyupter Notebook
 を選択


[onsenlist.py]
・onsen-data.csvから先頭５件を呼び出す


以下、雑誌に従って処理する

[flaskを使う場面]
・VScode拡張機能を導入する
　REST Client
  request.httpを送信する
 





