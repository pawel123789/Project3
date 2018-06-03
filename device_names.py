device_names = {1: 'cpu0', 2: 'mem_bank1', 3: 'cpu12'}
device_models = {1: 'Xeon', 2: 'Corsair', 3: 'Bughf'}
devices = {}







for dev_id, name in device_models.items():
    name = device_names[dev_id]
    devices.append({'id': dev_id, 'name': name, 'model': model})

print(devices)

model_map = 0

