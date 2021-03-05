import requests
from bs4 import BeautifulSoup
from lxml import etree

headers = {
            "cache-control": "no-cache",
            "postman-token": "72a56deb-825e-3ac3-dd61-4f77c4cbb4d8",
            "Host": "search.51job.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/70.0.3538.67 Safari/537.36",
        }
response1 = requests.get(url="https://jobs.51job.com/chongqing-yzq/126284449.html?s=01&t=0", headers=headers)
response1.encoding = "gbk"
html = etree.HTML(response1.text)
text_ = html.xpath('//div[@class="cn"]')
tl = []
for values in text_:
    gw_name = values.xpath('./h1/text()')
    gz = values.xpath('./strong/text()')
    gs_url = values.xpath('./p[@class="cname"]/a[1]/@href')
    gs_name = values.xpath('./p[@class="cname"]/a[1]/text()')
    position_url = values.xpath('./p[@class="cname"]/a[2]/@href')
    text = values.xpath('./p[@class="msg ltype"]/text()')
    print(gw_name, gz, gs_url, gs_name, position_url, text)
    t = values.xpath('./div[1]/div[1]/span/text()')
    print(t)
    tl.append(t)
    print(tl)
    s = ""
    for j in t:
        s += (j + "\n")
    print(s)
soup = BeautifulSoup(response1.text, "html.parser")
# text = soup.find_all("div", class_="cn")
# print(text)
# # title = soup.find_all("h1")
# title = soup.find_all("h1")
# for i in title:
#     print(i.get_text())
p = soup.find_all("div", class_="bmsg job_msg inbox")
# p1 =
list_p = []

for j in p:
    list_p.append(j.get_text())
    print(j.get_text())
# print(list_p)
print("**********")
# list_p.clear()
# print(list_p)
# print("************")
gz = soup.find_all("div", class_="tmsg inbox")
list_gz = []
for t in gz:
    list_gz.append(t.get_text())
    print(t.get_text())
print("-------------")
# ls = soup.select(".tBorderTop_box > div > p")
# ls1 = []
# print(ls)
# for tl in ls:
#     ls1.append(tl.get_text())
#     print(tl.get_text())
# print(ls1)
# tis = ""
# for ti in ls1:
#     tis += (ti + '\n')
# print(tis)
# ts1 = soup.select(".mt10 > p")
# for t_1 in ts1:
#     print(t_1.get_text())

work = soup.find_all("div", class_="bmsg inbox")
list_work = []
print(work)
for f in work:
    list_work.append(f.get_text())
    print(f.get_text())

for te in zip(list_gz, list_work, list_p):
    print(te)
    print(te[0])
# li = [['通信/电子/计算机方向--专利翻译'], ['通信/电子/计算机方向']] lit = [['成都创思立信信息技术有限公司'], ['通信/电子/']] te = [[
# 'https://jobs.51job.com/all/co2539625.html'], ['通信/电子/计算机方向--专利翻译']] gz = [[''], ['通信/电子/计算机方向--专利翻译']] url = [[
# 'https://jobs.51job.com/all/co2539625.html?#syzw'], ['通信/电子/计算机方向--专利翻译']] di = [['成都\xa0\xa0',
# '\xa0\xa0在校生/应届生\xa0\xa0', '\xa0\xa0本科\xa0\xa0', '\xa0\xa0招3人\xa0\xa0', '\xa0\xa010-27发布'], ['通信/电子/计算机方向--专利翻译']]
# qt = [['五险一金', '员工旅游', '年终奖金', '定期体检', '免费早餐午餐'], ['五险一金', '员工旅游', '年终奖金', '定期体检', '免费早餐午餐']] lt = zip(li, lit, te,
# gz, url, di, qt) for it1 in lt: print(it1) print(it1[1][0]) print(it1[3][0]) s = "" for itr in it1[6]: s += (itr +
# '\n') print(s)
