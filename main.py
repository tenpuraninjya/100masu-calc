### 100マス計算のアプリ　###

from tkinter import *
from tkinter import ttk
import random
from typing import Sized

# 変数準備
gyo = []
gyo_nums = [0,1,3,5]
retu = []
retu_nums = [2,4,6]


# ベースとなるウィンドウの作成
root = Tk()

# ベースウィンドウにタイトルをつける
root.title("100マス計算")

### ウィジェットの作成

#シンプルな矩形のウィジェットを作成
frame1 = ttk.Frame(root,padding=16)

# Frameを親要素として行ラベルのリストを作成
midasi_label1 = ttk.Label(frame1,text="100マス計算にチャレンジしよう！")
for i in gyo_nums:
    num = ttk.Label(frame1,text=i)
    gyo.append(num)

print(gyo)


# グローバル変数の作成
t = StringVar()

# Frameを親要素として入力ボックス（Entry）を作成
# textvariableで指定した変数に入力値がセットされる
entry1 = ttk.Entry(frame1,textvariable=t)

# Frameを親要素としてボタンを作成
# ボタンに表示される文字はtext属性で指定する。
# command属性には、ボタンをクリックした時に実行される関数を指定する。
button1 = ttk.Button(
    frame1,
    text='ok',
    command=lambda: print('Hello, %s.' % t.get())
)

### レイアウト
# pack()にsideパラメータを指定すると親ウィジェットの
#どの向きのリストに追加されるか指定出来る。
#同じ向きの場合は順に追加（表示）される
frame1.pack()
midasi_label1.pack(side=TOP)
for i in gyo:
    i.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)

# ウィンドウの表示開始
root.mainloop()