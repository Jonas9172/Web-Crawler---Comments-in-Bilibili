import requests
import json


def get_response():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'referer': 'https://www.bilibili.com/video/BV1ge411f7LY/?spm_id_from=333.337.search-card.all.click&vd_source=0c2a631b6a3f941a8ddf7fdcad920f42'

    }

    target_url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=236711229&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=39b491f6b45e59d45ce75652454b4c9f&wts=1702029472"
    res = requests.get(target_url, headers=headers)

    return res


def get_comments(res):
    comments_json = json.loads(res.text)
    comments = comments_json['data']['replies']
    with open('bilibili_comments.txt', 'w', encoding='utf-8') as file:
        for each in comments:
            file.write(each['member']['uname'] + '(' + str(each['member']['level_info']['current_level']) + '级)' + ':\n')
            file.write(each['content']['message'] + '\n')
            for i in each['replies']:
                file.write('  回复:  ' + i['member']['uname'] + ': ' + i['content']['message'] + '\n')
            file.write('\n')


if __name__ == '__main__':
    res = get_response()
    get_comments(res)