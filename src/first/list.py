
items = ['first', 'second']
print('second' in items) # リストに対象を含むのでtrue
print('1' in items) # リストに対象を含まないのでfalse
print('1' not in items) # リストに対象を含まないのでtrue


books = {'book1': 1, 'book2': 2}
print('book1' in books) # 辞書の場合はkeyがあるか見る。含むのでtrue
print('1' in books) # 辞書に含まないのでfalse
print('1' not in books) # 辞書に含まないのでtrue
