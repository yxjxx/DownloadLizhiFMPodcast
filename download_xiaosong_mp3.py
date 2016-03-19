# -*- coding: utf-8 -*-
# @Author: yxjxx
# @Date:   2016-03-20 00:19:37
# @Last Modified by:   yxjxx
# @Last Modified time: 2016-03-20 02:08:27
from ffmpy import FF
import requests
from bs4 import BeautifulSoup
from you_get import *
from you_get.cli_wrapper import *
from you_get.extractors import *
from you_get.common import *


def make_soup(url, tag, name):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    soup_result = soup.find(attrs={tag: name})
    return soup_result


def main():
    url = 'http://www.iqiyi.com/a_19rrgifngp.html'
    tag = 'class'
    name = 'site-piclist_pic_link'
    soup_result = make_soup(url, tag, name)
    video_url = soup_result['href']
    file_name = soup_result.img['title']
    video_name = file_name + '.mp4'
    audio_name = file_name + '.mp3'
    print(video_name, audio_name, video_url)
    iqiyi.download(video_url, output_dir='.', info_only=False,
                   merge=True, stream_id='topspeed', caption=False,
                   output_filename=video_name)

    inputs = {video_name: None}
    outputs = {audio_name: None}
    ff = FF(inputs=inputs, outputs=outputs)
    print(ff.cmd_str)
    ff.run()
    print('done')


if __name__ == '__main__':
    main()
