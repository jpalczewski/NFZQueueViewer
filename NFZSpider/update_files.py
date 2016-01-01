#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tempfile, glob, shutil, json, urllib
from os.path import join, dirname, realpath
from zipfile import ZipFile
url = 'http://kolejki.nfz.gov.pl/Informator/PobierzPlikXLS?term='


files_directory = join(dirname(realpath(__file__)), 'files')

if not os.path.exists(files_directory):
    os.mkdir(files_directory)
else:
    # Krok pierwszy: usunięcie starych plików.
    old_files = glob.glob(os.path.join(files_directory, '*.xlsx'))
    for f in old_files:
        os.remove(f)

# Krok drugi: ściągnięcie nowych plików.
tempdir = tempfile.mkdtemp()
hashfile = os.path.join(tempdir, 'hashlist.json')
os.system("scrapy crawl QueueSpider -o " + hashfile)

with open(hashfile, 'r') as f:
    hashlist = json.load(f)

for hash in hashlist[0]['hash_list']:
    urllib.urlretrieve(url+hash, os.path.join(tempdir, hash))
    with ZipFile(join(tempdir, hash), 'r') as zipped:
        zipped.extractall(files_directory)
