#! /usr/bin/env python3

import requests
import bs4
import urllib3 

urllib3.util.ssl_.DEFAULT_CIPHERS += "!DH"
ST_URL = "https://datascience.hawaii.edu/faculty-profiles/"


def get_dsst(url):
    st = []
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    for el in soup.select(".thm-profile"):
        st.append(el.select_one(".thm-profile-title a").text)
    return st


def main():
    st = get_dsst(ST_URL)
    print(", ".join(st))


if __name__ == "__main__":
    main()
