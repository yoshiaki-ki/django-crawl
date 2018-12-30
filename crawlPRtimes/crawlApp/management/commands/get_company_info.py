# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import json
# ここからスクレイピング必要分
from bs4 import BeautifulSoup
# ここからseleniumでブラウザ操作必要分
from selenium import webdriver
from time import sleep   # 新しくインポート

from ...models import Article, CompanyInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        num = 0
        # 企業DBからaddressが入力されていないオブジェクトを指定
        all_company_obj = CompanyInfo.objects.filter(address=None)
        # オブジェクトごとにURLをクロール
        for company_obj in all_company_obj:
            url = company_obj.PRtimes_URL
            # url = request.args.get('url')

            driver = webdriver.PhantomJS()  # PhantomJSを使う
            driver.get(url)  # URLにアクセスする
            data_list = []  # 全ページのデータを集める配列

            data = driver.page_source.encode('utf-8')  # ページ内の情報をutf-8で用意する
            soup = BeautifulSoup(data, "lxml")  # 加工しやすいようにlxml形式にする
            body_info = soup.find_all(
                "span", class_="body-information")  # スライド単位で抽出

            # 企業情報を格納
            company_obj.official_URL = body_info[0].text.strip()
            company_obj.category = body_info[1].text.strip()
            company_obj.address = body_info[2].text.strip()
            company_obj.tel_number = body_info[3].text.strip()
            company_obj.CEO = body_info[4].text.strip()
            company_obj.jojo = body_info[5].text.strip()
            company_obj.fund = body_info[6].text.strip()
            company_obj.save()

            driver.close()  # ブラウザ操作を終わらせる
            sleep(3)  # 3秒待ち
            num += 1

            print("{}:情報取得完了".format(company_obj.company_name))

            if num == 10:
                break
