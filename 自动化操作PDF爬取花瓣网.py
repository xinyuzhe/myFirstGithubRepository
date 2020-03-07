# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2019-11-14 16:30:55
# @Last Modified by:   Anderson
# @Last Modified time: 2019-12-30 15:32:39
from makerbean import web_crawler_bot as wbot
from makerbean import excel_bot as ebot
from makerbean import data_analysis_bot as dbot
from makerbean import pdf_bot as pbot

pbot.open('网易财报.pdf')
print(pbot.get_text(6))
pbot.split(7, '分割后PDF')
pbot.split(1, '分割后PDF')
pbot.split(3, '分割后PDF')
pbot.split(5, '分割后PDF')
pbot.merge(['分割后PDF/网易财报-p1.pdf', '分割后PDF/网易财报-p5.pdf'], '合并后')

for page in range(10):
	data = wbot.get_huaban('工业设计', page)
	for img in data:
		url = img['url']
		name = img['name']
		wbot.download_image(url, name, 'images')