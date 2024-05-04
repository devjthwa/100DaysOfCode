import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print(fx(20))
print('Done for 20')
print(fx(2))
print('Done for 2')
print(fx(26))
print('Done for 26')

print(fx(20))
print('Done for 20')
print(fx(2))
print('Done for 2')
print(fx(26))
print('Done for 26')