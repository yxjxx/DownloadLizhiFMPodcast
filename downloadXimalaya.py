#! /Users/yxj/env3/bin/python
# coding=utf-8
import requests
import re
import io
from bs4 import BeautifulSoup


# 罗辑思维，晓松奇谈
fm_list = ['http://m.ximalaya.com/10936615/album/321701',
           # 'http://m.ximalaya.com/1412917/album/239463',
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

        r1 = r'sound_url="(.*?\.m4a)"'
        r1_comp = re.compile(r1)
        soup = BeautifulSoup(r.text)
        soup_result = soup.find(attrs={'class':'block title ellipsis'})
        # print(soup_result.text)
        first_mp3_url = re.findall(r1_comp, r.text)[0]
        final_filename = soup_result.text + '.mp3'

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
