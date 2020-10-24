# set型
items = {'note', 'notebook', 'pen'}
print(type(items))

# 重複している要素は1つになる
items = {'note', 'notebook', 'pen', 'note'}
print(items)

# 順序がないためindex参照できない
# print(items[0]) ← TypeError発生

# 空のsetはset()を利用する。{}だとdict型になるので注意
print(type(set()))

# 空は偽
print(bool(set()))

# 要素の追加・削除
items.add('book')
print(items)
items.remove('note')
print(items)

# setのpopは取り出される要素は不定
print(items.pop())
print(items)


# frozenset型(setを不変にした型)
readItems = frozenset(['note', 'book', 'pen'])
print(type(readItems))

# 空は偽
print(bool(frozenset()))

# 不変なので追加できない
# readItems.add('test') ← AttributeError発生

# setは和集合・差集合・積集合・対称差の演算が行える。結果が集合であれば新しい集合が作成される
items_a = {'note', 'notebook', 'sketchbook'}
items_b = {'book', 'rulebook', 'sketchbook'}

# 和集合
print(items_a | items_b)
print(items_a.union(items_b))

# 差集合
print(items_a - items_b)
print(items_a.difference(items_b))

# 積集合
print(items_a & items_b)
print(items_a.intersection(items_b))

# 対称差（積集合の逆）
print(items_a ^ items_b)
print(items_a.symmetric_difference(items_b))

# 部分集合判定
print({'note', 'notebook'} <= items_a)

# forで出てくる順序は不定
for item in items:
    print(item)


# リスト内包表記
numbers = []
for i in range(10):
    numbers.append(str(i))

# 上を内包表記で記述
print([str(v) for v in range(10)])

def v2(value):
    return value * 2

print([v2(v) for v in range(10)])

# 内包表記のネスト
tuples = []
for x in [1,2,3]:
    for y in [4,5,6]:
        tuples.append((x,y))
print(tuples)

# [リストの要素 for文 for文]でネストできる（可読性が上がる場合に使う）
[(x,y) for x in [1,2,3] for y in [4,5,6]]

# if文がある内包表記
even = []
for i in range(10):
    if i % 2 == 0:
        even.append(i)

print([x for x in range(10) if x %2 == 0])

# set内包表記
set_comprehension = {i for i in range(10)}
print(set_comprehension)

# disc内包表記
dict_comprehension = {str(x): x for x in range(3)}

# ジェネレーター
gen = (i for i in range(3))
print(type(gen))
