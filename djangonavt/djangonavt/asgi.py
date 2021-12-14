"""
ASGI config for djangonavt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangonavt.settings')

application = get_asgi_application()

'''
print('x y z w F')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = not(x == (not y)) or ((x and w) == (z and not w))
                if F == 0:
                    print(x, y, z, w, F)
'''

# 5
'''
def F(N):
    N = str(N)
    N = N.replace('', ' ').split()
    N = [int(i) for i in N]
    res1 = 0
    res2 = 0
    for dig in range(0, len(N)):
        digit = N[dig]
        if digit % 2 == 0:
            res1 += digit
        if dig % 2 != 0:
            res2 += digit
    R = abs(res2 - res1)
    return R
for i in range(2, 10000):
    if F(i) == 13:
        print(i, F(i))
        break
'''

# 6
'''
counter = 0
for s in range(1, 10000):
    s1 = s
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s += 13
        n *= 2
    if n == 128:
        counter+=1
        print(s1, n, counter)
'''

# 7
'''
v = 160 * 1024 * 8
size = 256 * 640
res = v/size
print(res)
'''

# 8
'''
alphabet = ['А', 'В', 'Т', 'О', 'Р']
alphabet = sorted(alphabet)
count = 0
for A in alphabet:
    for B in alphabet:
        for C in alphabet:
            for D in alphabet:
                res = A + B + C + D
                count += 1
                if res == 'ВАТА':
                    print(count, res)
'''

