# NFZQueueViewer

## Description
An app which is designed to view places where queues from NFZ appears from different voivodeships at once. Based on [bioweb framework](http://bioweb.sourceforge.net/en/index.html) by [Robert M. Nowak](http://staff.elka.pw.edu.pl/~rnowak2/). Data is collected from [kolejki.nfz.gov.pl](http://kolejki.nfz.gov.pl/)('Pobierz Dane' section).

## Installation

1. All steps from [README_EN](/README_EN) applies. However, there are required packages don't mentioned there, f.e. [scrapy](http://scrapy.org/), [django rest framework](http://www.django-rest-framework.org/), [openpyxl](https://openpyxl.readthedocs.org/en/default/) - all of them are listed in pip_dev_file.

2. To download all files that are necessary to run, it is necessary to run `python2 NFZSpider/update_files.py` once - it should download and unpack all files in `NFZSpider/files` directory.

## Usage

`scons && scons r=l` will do the trick.

Client webapp shows size of data loaded into database(and it checks&updates it in a constant time interval) It is possible also to load downloaded xlsx files(codes in webapp are based on [internal enumeration from NFZ](http://www.nfz.gov.pl/o-nfz/identyfikatory-oddzialow-wojewodzkich-nfz/)) or flush all data from the database.

`Lucky?` button sends a telephone number to C++ module where complex calculations are done(ie. if the sum of all digits from phone number is divisible by seven) and show the answer to the user.

## Known bugs
System where python2 and python3 are installed may encounter problems where django uses incompatible libraries from python3 - solution from [archlinux wiki](https://wiki.archlinux.org/index.php/Python#Dealing_with_version_problem_in_build_scripts) work flawlessly.

## Known limitations

- Loading files into the database makes server irresponsive, end of loading are indicated by message boxes caused by failed status refresh.
- Windows app isn't tested at the moment.
