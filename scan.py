import os
import re


for root, dirs, files in os.walk("/User/kostyapashko/"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))


#
#• on.corpora.name.name_entity • on.corpora.name.name_bank
#


def file_read_from_head(fname, start, finish):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, start, finish):
            print(line)

namefile = "/Users/kostyapashko/Desktop/ontonotes-release-4.0/data/files/data/" \
           "english/annotations/bc/cctv/00/cctv_0003.name"
matching = r'<ENAMEX TYPE=\"(.*?)\">(.*?)<'


with open(namefile, "r+") as f:
    text = f.read()
    r = re.findall(matching,text)
    for i in r:
        print(i)
