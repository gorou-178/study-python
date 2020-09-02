
# f-string
hoge = 'hoge'
print(f'hoge = {hoge}')

# 3.8から末尾に=で、変数および式の出力ができるようになった
print(f'{hoge=}') # hoge='hoge'
print(f'{1+1=}') # 1+1=2

# {}でプレースホルダーのように動く
print('これは{}です{}'.format(hoge, 'か？'))

# 位置指定
print('{1}は{0}です'.format('B', 'A'))

# キーワード指定
print('{book}は{price}円です'.format(book='この本', price=100))

# 辞書のキーと一致したキーワードでformatできる、アンパックという指定方法
book = {'name': 'Python実践入門', 'price': 1500}
print('{name}という本は{price}円です'.format(**book))

# 文字列のバイト列変換
bytesHoge = hoge.encode('UTF-8')
print(type(bytesHoge))
print(bytesHoge)

