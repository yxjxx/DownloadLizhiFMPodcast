# coding=utf-8
import requests
import re
import io


def requests_file(file_url, filename):
    r = requests.get(file_url)
    if r.status_code == requests.codes.ok:
        with io.open(filename, 'wb') as file:
            file.write(r.content)
            file.flush()
            file.close()


def main():
    r = requests.get('http://www.lizhi.fm/415593/')

    r1 = r'data-url="(.*?\.mp3)"'
    r1_comp = re.compile(r1)
    r2 = r'data-radio-name="(.*?)"'
    r2_comp = re.compile(r2)
    r3 = r'data-title="(.*?)"'
    r3_comp = re.compile(r3)

    first_mp3_url = re.findall(r1_comp, r.text)[0]
    radio_name = re.findall(r2_comp, r.text)[0]
    title = re.findall(r3_comp, r.text)[0]

    requests_file(first_mp3_url, radio_name + '_' + title + '.mp3')
    print("done")


if __name__ == '__main__':
    main()
