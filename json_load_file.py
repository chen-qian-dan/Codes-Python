import json

with open('files/questions.json') as f:
    data = json.load(f)

print(data.keys())
for q in data['questions']:
    print(q)

for q in data['questions']:
    del q['validation']

with open('files/new_questions.json', 'w') as f:
    json.dump(data, f)


with open('files/new_questions.json', 'w') as f:
    json.dump(data, f, indent=2)