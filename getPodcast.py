#! /Users/yxj/env3/bin/python
# coding=utf-8
import requests
import re
import io

# 罗辑思维，晓松奇谈，吴晓波频道
fm_list = [
           'http://www.lizhi.fm/17248/',
           'http://www.lizhi.fm/679472/',
           'http://www.lizhi.fm/176647/'
           ]


def requests_file(file_url, filename):
    r = requests.get(file_url)
    if r.status_code == requests.codes.ok:
        with io.open(filename, 'wb') as file:
            file.write(r.content)
            file.flush()
            file.close()


def main():
    for fm in fm_list:
        r = requests.get(fm)

        r1 = r'data-url="(.*?\.mp3)"'
        r1_comp = re.compile(r1)
        r2 = r'data-radio-name="(.*?)"'
        r2_comp = re.compile(r2)
        r3 = r'data-title="(.*?)"'
        r3_comp = re.compile(r3)

        first_mp3_url = re.findall(r1_comp, r.text)[0]
        radio_name = re.findall(r2_comp, r.text)[0]
        title = re.findall(r3_comp, r.text)[0]
        final_filename = radio_name + '_' + title + '.mp3'

        f = open('latest.txt', 'r+')
        if (final_filename + '\n') not in f.readlines():
            print("downloading " + final_filename)
            requests_file(first_mp3_url, final_filename)
            f.write(final_filename + '\n')
        f.flush()
        f.close()
    print("done")


if __name__ == '__main__':
    main()
