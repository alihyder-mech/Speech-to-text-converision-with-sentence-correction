import json

f1 = open('valid_corpus.json')
f2 = open('valid_data.txt','a')
for line in f1:
    # data = json.load(f1)['text']
    data = json.loads(line)
    f2.write(data['text']+'\n')

f1.close()
f2.flush()
f2.close()