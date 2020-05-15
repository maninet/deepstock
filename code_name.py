import json

code_name = {}
with open('data.txt', 'r') as f:
    txts = f.readlines()
    # print(txts)
    i = 0
    
    for txt in txts:
        if txt.endswith(')') or txt.endswith(')\n'):
            name = txt.split('(')[0]
            code = txt.split('(')[1]
            if code.startswith('0') or code.startswith('3') or code.startswith('6'):
                # print(name, code)
                if code.endswith(')\n'):
                    code_name[name] = code[:-2]
                else:
                    code_name[name] = code[:-1]
            # print(txt)
                i += 1
    print(i)
# print(code_name)
print(len(code_name))

with open('code.json', 'w') as f:
    json.dump(code_name, f, ensure_ascii=False)
