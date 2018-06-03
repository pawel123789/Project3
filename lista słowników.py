data = [{'id': 1, 'model': 'AABB'}, {'id': 2, 'model': 'GGJI'}]



for item in data:
    print(item['id'])


print([item['id'] for item in data])
