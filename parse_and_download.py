#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import os

def parse(url):
    link_list = []

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    for link in soup.findAll('figure',{"class":"sw-media medium-insert-images"}):
        link_list.append(link.find('img')['data-src'])

    return link_list

def download(link_list, out_folder):
    for link in link_list:
        filename = link.split('/')[-1]
        print(filename)

        outpath = os.path.join(out_folder, filename)


        with open(outpath, 'wb') as wobj:
            image = requests.get(link)
            wobj.write(image.content)
    print('Downloaded')


if __name__ == '__main__':
    os.makedirs('images',exist_ok=True)
    url  ='https://www.scoopwhoop.com/shayari-on-life/' 
    out_folder = 'images/'
    download(parse(url), out_folder)


