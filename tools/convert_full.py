import sys
import json

target = 'train.json'
source = ''

def main():
    if len(sys.argv) == 2:
        source = sys.argv[1]
    else:
        source = input('Please input the source file: ')
    try:
        current = json.load(open('train.json', encoding='utf-8'))
    except FileNotFoundError:
        current = []
    content = open(source, encoding='utf-8').read()
    content = content.replace('[\r\n\t ]', '')
    current.append(content)
    json.dump(current, open(target, 'w', encoding='utf-8'), ensure_ascii=False)

if __name__ == "__main__":
    main()