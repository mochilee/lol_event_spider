import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import random
article_frist_url = []
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}
def get_article_url_page(forum_url):
    """爬取文章頁數"""
    r = requests.get(forum_url, headers=HEADERS)
    if r.status_code != requests.codes.ok:
        print('網頁載入失敗')
        return []
    
    # 爬取每一篇文章網址
    soup = BeautifulSoup(r.text, features='lxml')
    return get_article_total_page(soup)

def get_reply_info_list(url):
    """爬取回覆列表"""
    r = requests.get(url, headers=HEADERS)
    if r.status_code != requests.codes.ok:
        print('網頁載入失敗')
        return {}

    #reply_info_list = []
    soup = BeautifulSoup(r.text, features='lxml')
    reply_blocks = soup.select('section[id^="post_"]')
    #print(get_article_total_page(soup))
    # 對每一則回覆解析資料
    for reply_block in reply_blocks:
        reply_info = {}

        #reply_info['floor'] = int(reply_block.select_one('.floor').get('data-floor'))
        #print(reply_info['floor'] )
        #reply_info['user_name'] = reply_block.select_one('.username').text
        #print(reply_info['user_name'] )

        #reply_info['content'] = reply_block.select_one('.c-article__content').text
        #print(reply_info['content'] )

        #reply_info_list.append(reply_info)
        #article_frist_url.append(reply_info)
        article_frist_url.append(reply_block.select_one('.c-article__content').text)
        random.uniform(1, 3)

    return article_frist_url

def get_article_total_page(soup):
    """取得文章總頁數"""
    article_total_page = soup.select_one('.BH-pagebtnA > a:last-of-type').text
    return int(article_total_page)

if __name__ == "__main__":
 
    i = 0
    #article_frist_url = []
    url = 'https://forum.gamer.com.tw/C.php?bsn=17532&snA=674866&tnum=17210'
    #url1 = 'https://forum.gamer.com.tw/C.php?page=2&bsn=17532&snA=674866&tnum=17210'
    #article_frist_url = get_reply_info_list(url)
    #print(article_frist_url[0]['content'])
    #article_frist_url = get_reply_info_list(url1)
    #print(get_article_total_page(url))
    total_page = get_article_url_page(url)

    for page_number in range(total_page): #倒序
        new_url = "https://forum.gamer.com.tw/C.php?page="+ str(total_page-page_number) + "&bsn=17532&snA=674866&tnum=17210"
        print(new_url)
        if page_number == 25:
            break
        else:
            get_reply_info_list(new_url)
    
    
