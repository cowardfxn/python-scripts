#!/usr/bin/python
# encoding: utf-8
# Author: fanxn
# Date: 2018/4/22

'''
Env:
gekodriver v0.20.1
Firefox 60.0.1 (64 bit)

'''

from selenium_scraper import Action, Selector

action = Action()

main_page = "https://weibo.com/"

action.begin(headless=False, browser_type='firefox')

action.goto_url(main_page)
# action.wait()

action.waiting('XPATH', '/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/input', 20)

action.click('XPATH', '/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/input')

action.enter('XPATH', '/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/input', '12341234')

action.save_img('screenshots', 'before_search')

# action.end()

from urllib.parse import quote, quote_plus
search_user = 'http://s.weibo.com/user/{}&Refer=weibo_user'.format(quote('王志安'))

action.goto_url(search_user)

action.waiting('XPATH', '/html/body/div[1]/div[2]/div/div[2]', 20)

action.save_img('screenshots', 'user search')

action.end()
