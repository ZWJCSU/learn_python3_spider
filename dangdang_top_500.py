import requests
import re
import json
from bs4 import BeautifulSoup


def request_dandan(url,headers):
    print(f"正在爬取：{url}")
    try:
        response = requests.get(url,headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.select("ul li")
    print(lis)
    for li in lis:
        print(soup.select(".list_num"))

        # index = li.find('em').text
        # title = li.find('span', class_='title').text
        # rating = li.find('span', class_='rating_num').text
        # strInfo = re.search("(?<=<br/>).*?(?=<)", str(li.select_one(".list_num")), re.S | re.M).group().strip()
        # str1=li.select(".list_num")
        # print(str1)
        # infos = strInfo.split('/')
        # range = infos[0].strip()
        # image = infos[1].strip()
        # title = infos[2].strip()
        # recommend = infos[3].strip()
        # author = infos[4].strip()
        # times = infos[5].strip()
        # price = infos[6].strip()
        # write_fo_file(range, image, title, recommend, author, times,price)
    # pattern = re.compile(
    #     '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">¥(.*?)</span>.*?</li>',
    #     re.S)
    #
    # items = re.findall(pattern, html)
    #
    # for item in items:
    #     yield {
    #         'range': item[0],
    #         'image': item[1],
    #         'title': item[2],
    #         'recommend': item[3],
    #         'author': item[4],
    #         'times': item[5],
    #         'price': item[6]
    #     }



def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

def write_fo_file(index, title, rating, year, area, type):
    print(1)
    f = open('book.txt', 'a')
    f.write(f'{index},{title},{rating},{year},{area},{type}\n')
    f.closed

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                      ' Chrome/87.0.4280.88 Safari/537.36'}
    html = request_dandan(url,headers)
    items = parse_result(html)  # 解析过滤我们想要的信息



if __name__ == "__main__":
    for i in range(1,10):
        main(i)