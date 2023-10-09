s = input()
n = len(s)
s = s[:n // 2].replace('п', '*') + s[n // 2:]
print(s)