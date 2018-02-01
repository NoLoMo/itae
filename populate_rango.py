import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itae.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
	
	python_pages = [
		{"title": "Offical Python Tutorial", "url": "http://docs.python.org/2/tutorial/", "views" : 27},
		{"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython", "views" : 82},
		{"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/", "views" : 12}
	]

	django_pages = [
		{"title": "Offical Django Tutorial", "url": "https://docs.djangopro.com/en/1.9/intro/tutorial01/", "views" : 85},
		{"title": "Django Rocks", "url": "http://www.djangorocks.com/", "views" : 25},
		{"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/", "views" : 72}
	]

	other_pages = [
		{"title": "Bottle", "url": "http://bottlepy.org/docs/dev/", "views" : 51},
		{"title": "Flask", "url": "http://flask.pocoo.org", "views" : 34}
	]

	cats = {
		"Python": {"pages": python_pages, "views": 128, "likes": 64},
		"Django": {"pages": django_pages, "views": 64, "likes": 32},
		"Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
	}

	# 循环字典
	for key,value in cats.items():
		c = add_cat(key, value["views"], value["likes"])
		for p in value["pages"]:
			add_page(c, p["title"], p["url"], p["views"])

	# 打印进度
	for c in Category.objects.all():
		for p in Page.objects.filter(category = c):
			print("- {0} - {1} ".format(str(c), str(p)))

# 添加page值
def add_page(cat, title, url, views):
	p = Page.objects.get_or_create(category = cat, title = title)[0]
	p.url = url
	p.views = views
	p.save()
	return p

# 添加category值
def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name = name)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()