import argparse
import os
import sys
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser(
        description="""A utility for shortening links and checking
                       the number of site visits""",
    )
    parser.add_argument("url", help="Address of the site to be processed")

    return parser


def is_shorten_link(url):
    if url.startswith("https://vk.cc/") or url.startswith("http://vk.cc/"):
        return True
    return False


def shorten_link(token, url):
    base_url = "https://api.vk.ru/method/utils.getShortLink"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"url": url, "v": "5.199"}

    response = requests.get(base_url, headers=headers, params=payload)
    response.raise_for_status()

    return response.json()


def count_clicks(token, url):
    base_url = "https://api.vk.ru/method/utils.getLinkStats"
    url_parsed = urlparse(url)
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "key": url_parsed.path[1:],
        "interval": "forever",
        "extended": "0",
        "v": "5.199",
    }

    response = requests.get(base_url, headers=headers, params=payload)
    response.raise_for_status()

    return response.json()


def main():
    parser = create_parser()
    args = parser.parse_args()
    load_dotenv()
    token = os.environ["VK_TOKEN"]

    if is_shorten_link(args.url):
        try:
            count_clicks_response = count_clicks(token, args.url)
        except requests.exceptions.HTTPError:
            sys.exit("Failed click count request")

        if count_clicks_response.get("error"):
            sys.exit("There is no such short link")
        elif count_clicks_response["response"]["stats"]:
            print(
                "Number of visits:",
                count_clicks_response["response"]["stats"][0]["views"],
            )
        else:
            print("Number of visits: 0")
    else:
        try:
            short_link_response = shorten_link(token, args.url)
        except requests.exceptions.HTTPError:
            sys.exit("Failed link shortening request")

        if short_link_response.get("error"):
            sys.exit("Check the URL")
        else:
            print(
                "Short link:",
                short_link_response["response"]["short_url"],
            )


if __name__ == "__main__":
    main()
