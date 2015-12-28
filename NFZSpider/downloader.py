import json
import urllib
with open("list.json", 'r') as f:
    hashlist = json.load(f)


url = 'http://kolejki.nfz.gov.pl/Informator/PobierzPlikXLS?term='
for x in hashlist[0]['hash_list']:
    urllib.urlretrieve(url+x, 'files/'+x)
    pass
