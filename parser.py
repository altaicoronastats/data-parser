from bs4 import BeautifulSoup
import requests


def parse_news_page(url="https://rospotrebnadzor.ru/about/info/news/"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = soup.select('li > a')
    data = list(map(str, data))

    return check_title(data)


def check_title(array, title="О подтвержденных случаях новой коронавирусной инфекции COVID-2019 в России"):
    data = []
    for case in array:
        if title in case:
            data.append(case)

    return data


def list_merge(list_data, list_date):  # If we want to merge heads and dates, in dev
    ans = []
    print(len(list_date))
    for i in range(len(list_data)):
        ans.append(list_data[i])
        ans.append(list_date[i])

    return ans


def indexer():
    collected = []
    url = "https://rospotrebnadzor.ru/about/info/news/?PAGEN_1="
    stop = 0
    for i in range(200):
        if i == 0:
            d_url = "https://rospotrebnadzor.ru/about/info/news/"
            data = parse_news_page(d_url)
            collected.append(data)
        else:
            d_url = url + str(i + 1)
            data = parse_news_page(d_url)
            if data == []:
                stop += 1
                if stop > 3: break  # eheheh
            else:
                collected.append(data)
    collected = sum(collected, [])

    return collected


def page_indexer(data=indexer(), substring="/about/info/news/news_details.php?ELEMENT_ID="):
    array = []
    for i in range(len(data)):
        if substring in data[i]:
            print(data[i])
            array.append(data[i][54:59])  # specific position because we are sure

    return array


def url_linkage(page_index=page_indexer()):
    urls = []
    url_style = "https://rospotrebnadzor.ru/about/info/news/news_details.php?ELEMENT_ID="
    for i in range(len(page_index)):
        urls.append(url_style + page_index[i])

    return urls
