import re
texto = 'Java, JAVA, java'


print(re.sub('java', 'python', texto,flags=re.IGNORECASE))


