import re

s = "String, with: mess--sy; Punction!"

out = re.sub('[^\w\d\s]+', '', s)

print(out)
