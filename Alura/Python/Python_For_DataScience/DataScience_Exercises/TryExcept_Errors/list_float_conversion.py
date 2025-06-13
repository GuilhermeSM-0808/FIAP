data = [11, 32, 53, "12.5", "105.2","wow"]
converted_data = []

try:
    for i in data:
        converted_data.append(float(i))
except Exception as e:
    print(type(e), f"{e}")
    print("Failed to convert one or more values. Insert numbers only.")
else:
    print(converted_data)
finally:
    print("App finalized.")