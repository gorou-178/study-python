
for i in range(3): # range(n)で 0からn-1　まで繰り返し処理が実行される
    print('i: ' + str(i))

numbers = [1,2,3]
for number in numbers:
    print('number: ' + str(number))

for index, number in enumerate(numbers):
    print(str(index) + '番目: ' + str(number))

for index, char in enumerate('test'):
    print(str(index) + '番目: ' + char)

print('for文の変数スコープはfor文の外: index = ' + str(index))

items = ['1', '2', '3']
for item in items:
    print('item:' + item)

# for文のelse句。breakが実行されるのでelse句は実行されない
for message in ['one', 'two']:
    if message == 'one':
        break
else:
    print('breakでfor文が終わるので実行されない')

# for文のelse句。breakが実行されないのでelse句が実行される
for message in ['one', 'two']:
    if message == 'hoge':
        break
else:
    print('hogeがないのでelse句が実行される')

# カウンターを利用しない場合のfor文は_を利用する慣習があるらしい（変数として_は定義されはする）
for _ in range(2):
    print('カウンターを利用しないfor')

# while文
n = 0
while n < 3:
    print(n)
    n += 1

# whileのelse句。breakするのでelse句は実行されない
while n < 4:
    n += 1
    if '1' in items:
        break
else:
    print('breakが実行されるのでここは表示されない')

# whileのelse句。breakしないのでelse句が実行される
while n < 4:
    n += 1
    if 'one' in items:
        break
else:
    print('breakが実行されないのでここが表示される')

