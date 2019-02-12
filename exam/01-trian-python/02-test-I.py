import ast
str = '[1,2,3,4,5,6,7,8,9,7,8,5,4]'
stt = '{1,\'ertery\',\'tinter\'}'

testarray = ast.literal_eval(str)

for i in testarray:
    print(i)