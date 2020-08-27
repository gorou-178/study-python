
def getMessage(status):
    if status == 1:
        print('status 1')
    elif status == 2:
        print('status 2')
    elif status > 10:
        print('status is more than 10')
    else:
        print('default message')

def isTrue(value):
    if value:
        print(str(value) + ' is true')
    else:
        print(str(value) + ' is false')

getMessage(1)
getMessage(2)
getMessage(3)
getMessage(4)
getMessage(20)
getMessage(-1)

isTrue(1)
isTrue(0)
isTrue(0.0)
isTrue(None) # Noneはfalse
isTrue(True)
isTrue(False)
isTrue('') # 空文字はfalse
isTrue("") # 空リテラルはfalse
isTrue([]) # 空配列はfalse
isTrue({}) # 空辞書はfalse

print('value1' == 'value2') # 同一ではないのでFalse
print('value1' != 'value2') # 同一ではないのでTrue

x = 'test'
print(x is None) # オブジェクトが同一ではないのでFalse
print(x is not None) # オブジェクトが同一ではないのでTrue
