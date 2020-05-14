import random
import time
from ..main.requester import requester
from lxml import etree
import re


class CuisineCollection:
    def __init__(self, food, cook, cuisine_elements, materiallist, steplist):
        self.food = food
        self.cook = cook
        self.cuisine_elements = []
        self.materiallist = []
        self.steplist = []

    @property
    def parts(self):
        parts = ''
        for part in self.available_parts:
            p = part.xpath('./a/text()')[0]
            parts = parts+p+' '
        return parts.split()

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

    def add_element(self, cuisinename, cuisine_img, cuisine_taste, cuisine_cook):
        self.cuisine_elements.append([cuisinename, cuisine_img, cuisine_taste, cuisine_cook])

    def add_material(self, food, quantity):
        self.materiallist.append([food, quantity])

    def add_step(self, step_index, step_word, step_img_url):
        self.steplist.append([step_index, step_word, step_img_url])

def get_Cuisine(food, cook = ''):
    #search_url = 'https://home.meishichina.com/search/'+key_word+'/'
    search_url = 'https://home.meishichina.com/search/'+food+' '+cook+'/'
    root = etree.HTML(requester(search_url).content)
    try:
        s = root.xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/span/text()')[0]
    except IndexError:
        return 'dummy'
    
    available_cuisines = int(re.findall(r'\d+', s)[0])
    
    if available_cuisines < 5:
        return 'dummy'
    elif available_cuisines <= 20:
        target_cuisine_url = root.xpath('/html/body/div[3]/div/div[1]/div[2]/ul/li[{}]/div[2]/h4/a/@href'.format(random.randint(1,available_cuisines)))[0]
    else:       
        target_cuisine_url = root.xpath('/html/body/div[3]/div/div[1]/div[2]/ul/li[{}]/div[2]/h4/a/@href'.format(random.randint(1,20)))[0]
    
    #开始构建显示数据类
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
    
    #基本元素
    cuisine_process.add_element(cuisinename, cuisine_img, cuisine_taste, cuisine_cook)
    
    #材料清单
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
    steps = cuisine_root.xpath('/html/body/div[5]/div/div[1]/div[3]/div/div[@class="recipeStep"]')
    for step in steps:
        details = step.xpath('./ul/li')
        for detail in details:
            try:
                step_index = detail.xpath('./div[2]/div/text()')[0] #索引
                step_word = detail.xpath('./div[2]/text()')[0] #文字
                step_img_url = detail.xpath('./div[1]/img/@src')[0] #图片
            except IndexError:
                return 'dummy'
            cuisine_process.add_step(step_index, step_word, step_img_url)
    
    return cuisine_process
