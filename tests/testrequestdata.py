# coding:utf-8
import time
import random
import requests
from lxml import etree
import re
from prettytable import PrettyTable


from requests.exceptions import TooManyRedirects


SESSION = requests.Session()
SESSION.max_redirects = 3

def requester(
        url,
        main_url=None,
        delay=0,
        cook=None,
        headers=None,
        timeout=10,
        host=None,
        user_agents=[None],
        failed=None,
    ):
    """Handle the requests and return the response body."""

    # Pause/sleep the program for specified time
    time.sleep(delay)

    def make_request(url):
        """Default request"""
        final_headers = headers or {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#            'Origin': 'https://codebeautify.org',
            'Connection': 'close',
        }
        try:
            response = SESSION.get(
                url,
                cookies=cook,
                headers=final_headers,
                verify=False,
                timeout=timeout,
                stream=True,
            )
        except TooManyRedirects:
            return 'dummy'

        if 'text/html' in response.headers['content-type'] or \
           'text/plain' in response.headers['content-type']:
            if response.status_code != '404':
                return response
            else:
                response.close()
                return 'dummy'
        else:
            response.close()
            return 'dummy'
    
    return make_request(url)





Food = '吊瓜 豆角 茄子 青椒 西红柿 豌豆'.split()
Cook = '蒸 煮 拌 烤 炸 烩'.split()
#print(Food)
#print(Cook)

headers = {
        'Host': 'hm.baidu.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#       'Origin': 'https://codebeautify.org',
        'Connection': 'keep-alive',
    }

#创建搜索URL
#key_word = ''
#search_url = 'https://home.meishichina.com/search/'+key_word+'/'

#available_species = root.xpath('/html/body/div[5]/div/div/div[@class="category_sub clear"]')
#available_parts = root.xpath('/html/body/div[5]/div/div/div[@class="category_sub clear"]/ul/li')

#搜索数量
#/html/body/div[3]/div/div[1]/div[1]/div/div/span
def Food_random(rule=''):
    #从数据库中随机选择两个关键字，“主材 做法”
    return Food[random.randint(1,6)]

def Cook_random(rule=''):
    return Cook[random.randint(1,6)]

#def select_Cuisine(key_word=''):


print('Start')
#创建搜索URL
#key_word = Food_random()+' '+Cook_random()
#key_word = “牛肉 炖”
#print(key_word)
#search_url = 'https://home.meishichina.com/search/'+key_word+'/'
#print(search_url)
#r=requester(search_url)
# 设置网页编码格式
#r.encoding = 'utf8'
# 将request.content 转化为 Element
#root = etree.HTML(r.content)
#c = random.randint(2,candidate)
#print(c)
#detail_url = root.xpath('/html/body/div[3]/div/div[1]/div[2]/ul/li[{}]/div[2]/h4/a/@href'.format(c))[0]
#print(detail_url)

#test_url = 'https://home.meishichina.com/recipe-127449.html'
#test_url = 'https://home.meishichina.com/recipe-415081.html'
#root_t = etree.HTML(requester(test_url).content)

#print("Status Code: {} \n ".format(u.status_code))
#print("Encoding: {} \n".format(r.encoding))
#print("HTML: {} \n".format(r.text))
#print("\n")

#s=list[MaterialCollection.species]
#p=list[MaterialCollection.parts]

#zhurou = p[p.index(s[0]):p.index(s[1])]
#print(zhurou)
how_to_header= {
    '食材明细',
    '主料',
    '用量',
    '辅料',
    '配料',
    '工艺',
    '口味',
    '步骤图片URL',
    '步骤文字',
    '步骤索引'
}

#print(how_to_header)
#pt = PrettyTable()
#pt._set_field_names(how_to_header)
#print(pt)

#main_materials = []
#main_steps = []
#菜名
#print(root_t.xpath('//*[@id="recipe_title"]/text()')[0])
#图片URL
#print(root_t.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[1]/a/img/@src')[0])
#[口味]&#[工艺]
#/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeCategory_sub_R_mt30 clear"]

#cts = root_t.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeCategory_sub_R mt30 clear"]')
#print(root_t.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[3]/ul/li[2]/span[1]/text()')[0])
#for ct in cts:
#    #[口味]
#    print(ct.xpath('./ul/li[1]/span[1]/a/text()')[0])
    #[工艺]
#    print(ct.xpath('./ul/li[2]/span[1]/a/text()')[0])

#材料清单
#mains = root_t.xpath('/html/body/div[5]/div/div[1]/div[3]/div/fieldset[@class="particulars"]')
#for m in mains:
#    cats = m.xpath('./div/ul/li')
#    for n in cats:
#        try:
#            main_material = [n.xpath('./span[1]/a/b/text()')[0], n.xpath('./span[2]/text()')[0]]
#        except IndexError:
#            main_material = [n.xpath('./span[1]/b/text()')[0], n.xpath('./span[2]/text()')[0]]
#        main_materials.append(main_material)
#print(main_materials)

#步骤清单
#steps = root_t.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeStep"]')
#for s in steps:
#    indexes = s.xpath('./ul/li')
#    for i in indexes:
#        steps = [
#                i.xpath('./div[1]/img/@src')[0],
#                i.xpath('./div[2]/div/text()')[0],
#                i.xpath('./div[2]/text()')[0]
#        ]
#        print(steps['img_url'], steps['index'], steps['word'])
#        main_steps.append(steps)
#print(main_steps)

c_l = ''
#q_l = ''

search_url = 'https://www.meishichina.com/YuanLiao/category/rql/'
print(search_url)
r=requester(search_url)
# 设置网页编码格式
r.encoding = 'utf8'
# 将request.content 转化为 Element

root = etree.HTML(r.content)
items = root.xpath('/html/body/div[5]/div/div/div[@class="category_sub clear"]')
print(root.xpath('/html/body/div[5]/div/div/div[1]/ul/li[1]/a/text()')[0])
for item in items:
    cats = item.xpath('./ul/li')
    for cat in cats:
        c=cat.xpath('./a/text()')[0]
        c_l = c_l+c+' '

with open('suoyouroulei.txt', 'w') as f:
    f.write(c_l)
    f.write('\n'.join(c))

#    b=item.xpath('./b/text()')[0]
#    p=re.compile(r'(?<=共)\d+\.?\d*')
#   print(c)
#   print(p.findall(r'(?<=共)\d+\.?\d*'))



#t= root.xpath('/html/body/div[4]/div/div/div[16]/ul/li')

#for p in t:
#    q = p.xpath('./a/text()')[0]
#    q_l=q_l+q+' '
#with open('zuofa.txt', 'w') as f:        
#    f.write(q_l)


#headers = q_l.split()
#print(headers[45])


#t = item.xpath('./ul/li[1]/a/@title')
#print(t)

#优雅打印
#MaterialCollection(available_species, available_parts).pretty_print()
#HowToMake(root_t).common_print()


class Show_Cuisine(object):
    """docstring for Show_Cuisine"""
    def __init__(self, target_cuisine):
        self.target_cuisine = target_cuisine
        self.cuisine_url = self.target_cuisine
        self.cuisine_elements = []
        #cuisinename = ""
        #cuisine_img = ""
        #cuisine_taste = ""
        #cuisine_cook = ""
        self.materiallist =[]        
        self.steplist = []

    def add_element(self, cuisinename, cuisine_img, cuisine_taste,cuisine_cook):
        self.cuisine_elements.append([cuisinename, cuisine_img, cuisine_taste, cuisine_cook])

    def add_material(self, food, quantity):
        self.materiallist.append([food, quantity])

    def add_step(self, step_index, step_word):#, step_img_url
        self.steplist.append([step_index, step_word])

def get_Cuisine(food, cook):
    #search_url = 'https://home.meishichina.com/search/'+key_word+'/'
    search_url = 'https://home.meishichina.com/search/'+food+' '+cook+'/'
    root = etree.HTML(requester(search_url).content)
    try:
        s = root.xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/span/text()')[0]
    except IndexError:
        return 'dummy'
    available_cuisines = re.findall(r'\d+', s)    
    if int(available_cuisines[0]) <= 20:
       candidate = int(available_cuisines[0])
    else:       
       candidate = 20 
    target_cuisine_url = root.xpath('/html/body/div[3]/div/div[1]/div[2]/ul/li[{}]/div[2]/h4/a/@href'.format(random.randint(2,candidate)))[0]
    cuisine_process = Show_Cuisine(target_cuisine_url)
    cuisine_root = etree.HTML(requester(cuisine_process.cuisine_url).content)
    #菜名
    cuisinename = cuisine_root.xpath('//*[@id="recipe_title"]/text()')[0]
    #图片URL
    cuisine_img = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[1]/a/img/@src')[0]
    #[口味]&#[工艺]
    cook_tastes = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeCategory_sub_R mt30 clear"]')
    for ct in cook_tastes:
        #[口味]
        cuisine_taste = ct.xpath('./ul/li[1]/span[1]/a/text()')[0]
        #[工艺]
        cuisine_cook = ct.xpath('./ul/li[2]/span[1]/a/text()')[0]
    cuisine_process.add_element(cuisinename, cuisine_img, cuisine_taste, cuisine_cook)
    #材料清单
    #materiallist = []
    items = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/fieldset[@class="particulars"]')
    for item in items:
        categories = item.xpath('./div/ul/li')
        for material in categories:
            try:
                food = material.xpath('./span[1]/a/b/text()')[0]
                quantity = material.xpath('./span[2]/text()')[0]
            except IndexError:
                food = material.xpath('./span[1]/b/text()')[0]
                quantity = material.xpath('./span[2]/text()')[0]
            cuisine_process.add_material(food, quantity)
    #步骤清单
    #steplist = []
    steps = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeStep"]')
    for step in steps:
        details = step.xpath('./ul/li')
        for detail in details:
            try:
                step_index = detail.xpath('./div[2]/div/text()')[0],
                step_word = detail.xpath('./div[2]/text()')[0]
                #step_img_url = detial.xpath('./div[1]/img/@src')[0]
            except IndexError:
                return 'dummy'
            cuisine_process.add_step(step_index, step_word)
    return cuisine_process



print('Finished')

