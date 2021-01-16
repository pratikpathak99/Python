#Write a demo program for exception handling.

(a, b) = (15, 0)
try:
    g = a/b
except ZeroDivisionError as s:
    k = s
    print(k)
