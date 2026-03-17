from PIL import Image
import os
import sys

image=sys.argv[1]
output=sys.argv[2]

if not os.path.exists(output):
    os.makedirs(output)

for file in os.listdir(image):
    img=Image.open(f'{image}{file}')
    clean_name=os.path.splitext(file)[0]
    img.save(f'{output}/{clean_name}.png','png')

print("All done")