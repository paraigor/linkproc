# VK URL shortener and click count informer

Linkproc is a utility for shortening links and checking the number of site visits using VK API.

### Installation

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

VK API service token is required to use this utility. Token is generated after [creating application](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application) in VK ID personal account and looks like: `82a02da882a02da882a02da8a981b7f3cc882a082a02da8e4af9c41e8551329276dde72`.

Security sensitive information recommended storing in the project using `.env` files.

Key name to store token value is `VK_TOKEN`.

### Usage

It's a very easy to use utility. Just pass URL as an argument and it will show short link, if address is not shorten:
```
$ python linkproc.py https://dvmn.org/modules
Short link: https://vk.cc/cvPDMl
```
or number of visits otherwise:
```
$ python linkproc.py https://vk.cc/cvPDMl 
Number of visits: 12
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).