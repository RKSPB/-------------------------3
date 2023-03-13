dict = {}

for n in range(1, 4):
    file = f'{n}.txt'
    with open(file, 'r', encoding='utf-8') as f:
        txt = [] 
        for x in f.read().splitlines():            
            txt.append(x)
            dict[file] = txt
       
with open('all_texts.txt', 'w', encoding='utf-8') as file:
    for key, val in sorted(dict.items(), key=lambda x: len(x[-1])):
        file.write(key + '\n')
        file.write(str(len(val)) + '\n')
        file.write('\n'.join(val))
        file.write('\n')