import requests
from pyquery import PyQuery as pq

if __name__ == '__main__':
    response = requests.get("https://www.emojiall.com/zh-hans/platform-wechat")
    print(response.status_code)
    doc = pq(response.text)

    tables = doc(".emoji_card_content .table")
    # print(tables)

    elements = tables("td:nth-child(2)").items()
    texts = [element.text() for element in elements]
    print(texts)
