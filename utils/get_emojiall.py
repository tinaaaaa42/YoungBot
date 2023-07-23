import requests
from pyquery import PyQuery as pq

def wechat_emoji():
    response = requests.get("https://www.emojiall.com/zh-hans/platform-wechat")
    print(response.status_code)
    doc = pq(response.text)

    tables = doc(".emoji_card_content .table")
    # print(tables)

    elements = tables("td:nth-child(2)").items()
    texts = [element.text() for element in elements]
    print(texts)

def all_emoji():
    response = requests.get("https://www.freecodecamp.org/news/all-emojis-emoji-list-for-copy-and-paste/")
    print(response.status_code)
    doc = pq(response.text)

    heads = doc("h3")
    # print(heads)

    tables = doc("table")
    elements = tables("td:nth-child(1)")
    descriptions = tables("td:nth-child(2)")

    emoji = [element.text() for element in elements.items()]
    # print(emoji)
    desc = [description.text() for description in descriptions.items()]
    # print(len(desc))
    emoji_dist = dict(zip(desc, emoji))
    for key, value in emoji_dist.items():
        print(f"\"{key}\": \"{value}\",")
    
if __name__ == "__main__":
    # wechat_emoji()
    all_emoji()
