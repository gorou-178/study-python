
items = ['note', 'book']
print(type(items))

# listへの追加・削除
items.append('paper')
print(items)

del items[1]
print(items)

# listの結合
items = ['notebook', 'note'] + items
print(items)

# listのpop
print(items.pop(0))
print(items)

# indexアクセス（マイナスは左末尾からアクセス）
print(items[0])
print(items[-1])
# print(items[-4]) ← これは要素数を超えるため IndexError

# スライス [start index:end indexの前まで]
# 文字と文字の間の数を数えるとイメージしやすい（スライスでもマイナス使える）
#　 -----------------------------
# 　| A | | B | | C | | D | | E | 
#　 -----------------------------
#　 0    1     2     3     4     5
#　-5   -4    -3    -2    -1
print(items[0:2])
print(items[1:3])

# start indexを省略すると先頭から
print(items[:2])
# end indexを省略すると末尾まで
print(items[1:])

# スライス指定箇所の上書きができる
items[0:2] = [1,2,3]
print(items)
