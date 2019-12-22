file = input('Please input the source file: ')
target = input('Please input the target file: ')

input = open(file, 'r', encoding='utf-8')
output = open(target, 'w', encoding='utf-8')

data = input.readlines()
novel = []
escape = 0
buffer = ''
for line in data:
    if escape > 2:
        novel.append(buffer)
        buffer = ''
    line = line.strip()
    if not line:
        escape = escape + 1
        continue
    escape = 0
    line = line.replace('"', '')
    buffer = buffer + line
json = '['
for section in novel:
    json = json + '"' + section + '",'
json = json[:-1] + ']'
print(json, file=output, end='')