#do and understand again
from re import finditer
s, k = input().strip(), input().strip()
print(*[(m.start(1), m.end(1) - 1) for m in finditer(f'(?=({k}))', s)] or [(-1, -1)], sep='\n')