# 長方形の面積を求めるプログラムを開始します。
print('長方形の面積を求めます。')

# ユーザーに高さの入力を促し、入力された値を浮動小数点数に変換して変数heightに保存します。
height = float(input('高さを入力してください: '))

# ユーザーに幅の入力を促し、入力された値を浮動小数点数に変換して変数widthに保存します。
width = float(input('幅を入力してください: '))

# 変数heightとwidthの値を掛け合わせて、長方形の面積を計算し、結果を変数areaに保存します。
area = height * width

# 計算された面積を整数に変換して出力します。
# f文字列を使用して、面積の値をメッセージに組み込んでいます。
print(f'面積: {int(area)}')
