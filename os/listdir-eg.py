import os

dir = '/home/hugo/Pictures'
filenames=os.listdir(dir)

for i in range(0,len(filenames)):
    print(filenames[i])