import requests, re, csv

cookie = ''
input_file = "input.txt"
output_file = "output.csv"

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cookie' : cookie,
        'Connection':'keep-alive'
        }

def search(shop_name):
    url = 'http://shop.m.taobao.com/shop/shop_search.htm?q='+shop_name+'&_input_charset=utf-8&topSearch=1&atype=b&sid=&searchfrom=&action=RedirectAppAction&event_submit_do_search_shop=%E6%90%9C+%E7%B4%A2'
    page = requests.get(url, headers=headers)
    result = re.search('<h3 class="d-title">(.*)</h3>',page.text)
    result_name = result.group(1) if result != None else None
    return "存在" if shop_name == result_name else "不存在"

def main():
    with open(input_file) as f:
        for i, shop_name in enumerate(f):
            shop_name = shop_name.rstrip()
            shop_exist = search(shop_name)
            with open(output_file, 'a', newline='') as fo:
                writer = csv.writer(fo)
                writer.writerow([shop_name, shop_exist])
            print('writing data #{} {} {}'.format(i+1, shop_name, shop_exist))

if __name__ == '__main__':
    main()