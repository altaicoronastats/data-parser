from bs4 import BeautifulSoup
import requests


def parse_news_page(url="https://rospotrebnadzor.ru/about/info/news/"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = soup.select('li > a')
    # date = soup.select('li > p', class_="date")

    data = list(map(str, data))
    # date = list(map(str, date))

    # print(list_merge(data, date))

    return check(data)


def check(array, title="О подтвержденных случаях новой коронавирусной инфекции COVID-2019 в России"):
    data = []
    for case in array:
        if title in case:
            data.append(case)
    print(len(data))
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
                if stop > 3: break
            else:
                collected.append(data)
    collected = sum(collected, [])
