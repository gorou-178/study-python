# python3.7から辞書の挿入順が維持されるようになった
# dict型
items = {'note': 100, 'notebook': 200, 'pen': 300}
print(type(items))

# キーだけ取得できる
for key in items:
    print(key)

# 値だけ取得
for value in items.values():
    print(value)

# キーと値のタプルを取得
for key, value in items.items():
    print(f'{key}:{value}')

# キーワード引数での定義
names = dict(taro="20", jiro="30", shun="6")
print(names)

# 追加・pop・削除
names['rin'] = '3'
print(names.pop('shun'))
print(names)
del names['jiro']
print(names)

# キーワード参照（存在しない場合KeyErrorが発生）
print(names['taro'])
# names['hoge] ← KeyErrorが発生する
# getであればKeyErrorは発生しない
print(names.get('jiro')) # Noneを返す
print(names.get('jiro', 'this name is undefine')) # デフォルト値指定

# キーは文字列・数値・タプルなどの不変オブジェクトが利用できる（厳密にはハッシュ可能なものが利用できる）
teams = {('taro', 'jiro'): 1, ('hoge', 'fuga'): 2}
print(teams[('taro', 'jiro')])
# teams = {['taro', 'jiro']: 1} ← リストは不変ではないのでキーに設定できない(TypeError発生)

# 空の辞書は偽
print(bool({}))

# in, not inはキーの存在を確認
print(f'note in items: {"note" in items}')
print(f'book not in items: {"book" not in items}')

# 値の存在確認はvalues()を利用
print(f'200 value in items: {200 in items.values()}')
