import re
d = '+791146306909'
match = bool(re.search(r'^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', d))
print(match)