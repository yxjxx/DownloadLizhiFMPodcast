#! /Users/yxj/env3/bin/python
# coding=utf-8
import requests
import re
import io
from bs4 import BeautifulSoup


# 晓松奇谈
fm_list = ['http://www.kaolafm.com/zj/DgD9XxEQ.html#list'
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
        # episodes list html
        r = requests.get(fm)
        soup = BeautifulSoup(r.text)
        soup_result = soup.find(attrs={'class': 'fl sp-name ellipsis'})
        single_episode_title = soup_result['title']

        single_episode_url = soup_result['href']
        single_episode_html = requests.get(single_episode_url)
        r1 = r'value="(.*?\.mp3)"'
        r1_comp = re.compile(r1)
        first_mp3_url = re.findall(r1_comp, single_episode_html.text)[0]
        final_filename = single_episode_title + '.mp3'
        print(first_mp3_url, final_filename)

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
