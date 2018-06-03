data = [{'height': 173, 'first_name': 'John', 'last_name': 'Doe'},
        {'height': 180, 'first_name': 'Andrew', 'last_name': 'Peck'},
        {'height': 190, 'first_name': 'Ann', 'last_name': 'Bill'},
        {'height': 165, 'first_name': 'John', 'last_name': 'Murry'}]


total = 0

for record in data:
    total += record['height']

print('Średnia to: ', total / len(data))

heights_by_name = {}

for record in data:
    if record['first_name'] in heights_by_name:
        heights_by_name[record['first_name']].append(record['height'])
    else:
        heights_by_name[record['first_name']] = [record['height']]

print(heights_by_name)


for name, heights in heights_by_name.items():
    print(name, sum(heights) / len(heights))

total_by_name = {}
count_by_name = {}
first_name = record['first_name']

for record in data:

    total_by_name[first_name] = total_by_name.get(first_name, 0) + record['height']
    count_by_name[first_name] = count_by_name.get(first_name, 0) + 1

for name, total in total_by_name.items():
    printdata = [{'height': 173, 'first_name': 'John', 'last_name': 'Doe'},
        {'height': 180, 'first_name': 'Andrew', 'last_name': 'Peck'},
        {'height': 190, 'first_name': 'Ann', 'last_name': 'Bill'},
        {'height': 165, 'first_name': 'John', 'last_name': 'Murry'}]


total = 0

for record in data:
    total += record['height']

print('Średnia to: ', total / len(data))

heights_by_name = {}

for record in data:
    if record['first_name'] in heights_by_name:
        heights_by_name[record['first_name']].append(record['height'])
    else:
        heights_by_name[record['first_name']] = [record['height']]

print(heights_by_name)


for name, heights in heights_by_name.items():
    print(name, sum(heights) / len(heights))

total_by_name = {}
count_by_name = {}
first_name = record['first_name']

for record in data:

    total_by_name[first_name] = total_by_name.get(first_name, 0) + record['height']
    count_by_name[first_name] = count_by_name.get(first_name, 0) + 1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])(name, total / count_by_name[name])