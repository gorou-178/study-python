
# 3つクオートでヒアドキュメントでかける
message = '''
    test1
    test2
    test3
'''
print(message)

# ()で文字連結もできる
hogeUrl = (
    'https://'
    'www.hoge.com'
    '/posts/123'
)
print(hogeUrl)

# +で文字連結
name = '山田' + '太郎'
print(name)

# 演算で文字列を作れる
book = 'book'
manyBooks = book * 3
print(manyBooks)
