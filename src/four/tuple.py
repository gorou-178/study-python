
# tuple型（不変なリスト）
# items = 'note', 'book' ← これで定義できるが可読性が良くないので()をつけることが多い
items = ('note', 'book')
print(items)

# リストなどのイテラブルなオブジェクトからtuple作成ができる
list = ['test', 'list']
tList = tuple(list)

# 空のtuple
print(tuple())
print(())

# 要素1個のtupleの作成
print(tuple('1',))

# indexアクセス
print(items[1])
# items[0] = 'test' ← tupleにはできない

# スライスは新しいtupleが生成される
print(items[:1])

# 参照
for item in items:
    print(item)

# 空は偽になる
print(f'empty tuple: {bool(tuple())}')

# in, not in
print(f'items in note: { bool("note" in items) }')
print(f'items not in test: { bool("test" not in items) }')
