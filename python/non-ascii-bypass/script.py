def gener_python_non_ascii(s:str):
    """根据给出的目标字符串生成python3可识别的变量字符串\n
    注意：仅作为变量时可被识别，其他情况下无法被识别比如字符串比较时，并且仅在python3下可用\n
    此生成仅支持大小写字母类型，不支持特殊字符，并且该特性无法绕过python关键字比如for"""
    non_ascii_dict = """
a ---> ª
b ---> ᵇ
c ---> ᶜ
d ---> ᵈ
e ---> ᵉ
f ---> ᶠ
g ---> ᵍ
h ---> ʰ
i ---> ᵢ
j ---> ʲ
k ---> ᵏ
l ---> ˡ
m ---> ᵐ
n ---> ⁿ
o ---> º
p ---> ᵖ
q ---> ｑ
r ---> ʳ
s ---> ſ
t ---> ᵗ
u ---> ᵘ
v ---> ᵛ
w ---> ʷ
x ---> ˣ
y ---> ʸ
z ---> ᶻ
A ---> ᴬ
B ---> ᴮ
C ---> ℂ
D ---> ᴰ
E ---> ᴱ
F ---> ℱ
G ---> ᴳ
H ---> ᴴ
I ---> ᴵ
J ---> ᴶ
K ---> ᴷ
L ---> ᴸ
M ---> ᴹ
N ---> ᴺ
O ---> ᴼ
P ---> ᴾ
Q ---> ℚ
R ---> ᴿ
S ---> Ｓ
T ---> ᵀ
U ---> ᵁ
V ---> Ⅴ
W ---> ᵂ
X ---> Ⅹ
Y ---> Ｙ
Z ---> ℤ
    """
    '''
    原始生成代码
    lists = [i for i in s]

    tmp = "".join([i for i in string.ascii_letters])
    exec(f'{tmp} = 1', locals())

    for i in string.ascii_letters:
        for j in range(100,100000):
            try:
                if eval(f'{tmp.replace(i, chr(j))}', locals()) == 1 and chr(j) != i:
                    print(f'{i} ---> {chr(j)}')
                    lists = [n.replace(i, chr(j)) for n in lists]
                    break
            except:
                pass
    
    return ''.join(lists)
    '''

    non_ascii_dict = {i.split(' ---> ')[0]:i.split(' ---> ')[1] for i in non_ascii_dict.strip('\n ').split('\n') if i != ''}
    result = s
    for k, v in non_ascii_dict.items():
        result = result.replace(k, v)
    
    return result
