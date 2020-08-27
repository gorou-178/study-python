
items = ['book1', 'book2', 'book3']
def getBook(index):
    message = 0
    try:
        message = items[index]
    except IndexError:
        return 'indexが範囲外です: ' + str(index)
    else:
        print('tryのelse句はexceptが実行されない場合に処理される')
    finally:
        print('finally句は必ず実行される')
    return message

numbers = ['1', '2', '3']
def getMessage(index):
    try:
        return numbers[index]
    except (IndexError, TypeError) as e:
        return f'indexが範囲外です: {e}'
    finally:
        print('finally句は必ず実行される')

# raiseで例外を発生させる
def throwException():
    raise ValueError('意図的にエラーを発生')

# except句のraiseは引数なしで実行でき、例外を引きついでthrowできる
def takeOverException():
    try:
        throwException()
    except ValueError:
        raise

print(getBook(1))
print(getBook(10))

print(getMessage(1))
print(getMessage(10))
print(getMessage('1'))

try:
    throwException()
except ValueError as e:
    print(f'{e}')

# オリジナルな例外を定義
class OriginalError(Exception):
    """オリジナル例外"""

# オリジナル例外クラスの継承
class PageNotFoundError(OriginalError):
    def __init__(self, message):
        self.message = message

try:
    raise OriginalError('オリジナル')
except OriginalError as e:
    print(f'{e}')

try:
    raise PageNotFoundError('オリジナルページエラー')
except PageNotFoundError as e:
    print(f'{e}')
