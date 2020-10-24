
# int型
int_number = 1
print(int_number)

# 数値リテラル（_は無視されるので見やすいように書いて良い
money = 10_000_000
print(money)

# pythonのint型はメモリが許す限り大きな値を扱える
big_value = 1000000000000000000000000000000000000000000000000
print(big_value)

# float
float_number = 1.0
print(type(float_number))
# 指数表記
float_number = 1e-5
print(float_number)
print(type(float('inf')))
print('正の無限大: ' + str(float('inf')))
print('負の無限大: ' + str(float('-inf')))
print('NaNもfloat型: ' + str(type(float('nan'))))

# 複素数 数値リテラルで数値にjをつけると定義できる
complex_number = 1+2j
print(complex_number)
print(type(complex_number))
print('実部: ' + str(complex_number.real))
print('虚部: ' + str(complex_number.imag))
