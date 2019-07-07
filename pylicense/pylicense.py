"""

A python tool for OSS license

author: AtsushiSakai (@Atsushi_twi)

"""

import json
import urllib.request


def get_license_from_url(url):
    license_str = None

    repo_info_json = __get_github_repo_info_from_url(url)
    license_str = repo_info_json["license"]["name"]

    return license_str


def __get_github_repo_info_from_url(url):
    api_url = url.replace("https://github.com/", "https://api.github.com/repos/")
    # print(api_url)
    req = urllib.request.Request(api_url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    res_json = json.loads(body)
    # print(json.dumps(res_json, indent=2))
    return res_json


def main():
    license_str = get_license_from_url("https://github.com/AtsushiSakai/pylicense")
    print(license_str)


if __name__ == '__main__':
    main()
