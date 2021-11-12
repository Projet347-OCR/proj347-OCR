import easyocr
import json

ready = easyocr.Reader(['fr'])
results = ready.readtext('data/images/permis-de-conduire2.png')

# f = open("data/output/image_data.txt", "r")
# f_contents = f.read()
# f.close()

with open('data/output/data.txt', 'w') as f:
    for result in results:
        print(result[1], file=f)

# print(f_contents)
# data = json.loads(f_contents)
# print(data)