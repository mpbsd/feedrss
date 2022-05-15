#!/usr/bin/env python3


import re
import bs4
import requests


def ime():
    with requests.session() as rs:
        resp = rs.get("https://ime.ufg.br", verify=False)
        soup = bs4.BeautifulSoup(resp.content, "lxml")
        news = [
            x
            for x in soup.find_all("a", {"target": "_self"})
            if "class" in x.attrs and x["class"] == ["news-image"]
        ]
        feed = {
            news.index(x): {
                "title": x["title"].strip(),
                "href": x["href"],
            }
            for x in news
        }
        return feed


def main():
    rss_ime = ime()
    with open("brew/ime.md", "w") as f:
        for k in rss_ime.keys():
            list_item = "{}. [{}][]".format(k, rss_ime[k]["title"])
            print(list_item, file=f)
        print("\n", file=f)
        for k in rss_ime.keys():
            reference = "[{}]: {}".format(
                rss_ime[k]["title"], rss_ime[k]["href"]
            )
            print(reference, file=f)


if __name__ == "__main__":
    main()
