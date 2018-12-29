# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import json
# ここからスクレイピング必要分
from bs4 import BeautifulSoup
# ここからseleniumでブラウザ操作必要分
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 文字を入力する時に使う
from time import sleep   # 新しくインポート
import datetime

from ...models import Article, CompanyInfo


class Command(BaseCommand):

    # コマンドライン引数を指定します。
    def add_arguments(self, parser):
        parser.add_argument('genre', nargs='+', type=str)

    def handle(self, *args, **options):
        for genre in options['genre']:
            print(genre)
            page = 1

            driver = webdriver.PhantomJS()  # PhantomJSを使う
            driver.set_window_size(1124, 850)  # PhantomJSのサイズを指定する
            # 指定した要素などがなかった場合出てくるまでdriverが最大20秒まで自動待機してくれる
            driver.implicitly_wait(20)

            URL = "https://prtimes.jp/" + genre + "/"
            driver.get(URL)  # URLにアクセスする
            data_list = []  # 全ページのデータを集める配列

            driver.execute_script('window.scrollTo(0, 3000)')  # ページャーのある下に移動
            for i in range(1, page):
                next = driver.find_element_by_xpath(
                    "//*[@id='more-load-btn-view']")  # ページャーのNEXT要素を抽出
                next.click()  # Nextボタンをクリック
                sleep(3)

            # for i in range(0, page):
            #     print(str(i + 1) + u"ページ目")
            data = driver.page_source.encode('utf-8')  # ページ内の情報をutf-8で用意する
            soup = BeautifulSoup(data, "lxml")  # 加工しやすいようにlxml形式にする
            article_list = soup.find_all(
                "article", class_="item-ordinary")  # スライド単位で抽出

            for article in article_list:
                article_in = {}  # 記事情報を辞書形式でまとめる

                # 企業名を取得
                company = article.find("a", class_="link-name-company").text
                article_in["company"] = company.strip()

                #　記事名を取得
                title = article.find(
                    "a", class_="link-title-item link-title-item-ordinary").text
                article_in["title"] = title

                # リンクを取得
                link = article.find(
                    "a", class_="link-title-item link-title-item-ordinary").get("href")
                article_in["link"] = "https://prtimes.jp" + link

                #　時間を取得
                time = article.find(
                    "time", class_="time-release time-release-ordinary icon-time-release-svg").get("datetime")
                time = time.replace("+0900", "").replace("T", " ")
                article_in["time"] = time

                # 企業ページのURL
                company_link = article.find(
                    "a", class_="link-name-company name-company name-company-ordinary").get("href")
                article_in["company_link"] = "https://prtimes.jp" + \
                    company_link

                # 記事リストがリストに入っていなかったら追加
                if article_in not in data_list:
                    data_list.append(article_in)

            # print(data_list)

            driver.close()  # ブラウザ操作を終わらせる
            # result = json.dumps(data_list, ensure_ascii=False,
            #                         indent=2)  # 作った配列をjson形式にして出力する

            # DBに保存されている記事タイトルを取得
            all_article_obj = Article.objects.all()
            all_article_titles = []   # 記事タイトルを格納
            for article_obj in all_article_obj:
                all_article_titles.append(article_obj.title)


            # 記事の保存
            for article in data_list:
                # data_company_id = data['company_id']
                article_title = article['title']
                article_release_time = article['time']
                article_url = article['link']
                company = article['company']
                company_url = article['company_link']
                # is_genre = 'is_{}'.format(genre)

                # 企業名を保存
                all_company_obj = CompanyInfo.objects.all()
                all_company_list = []
                for company_already_written in all_company_obj:
                    all_company_list.append(
                        company_already_written.company_name)
                if company not in all_company_list:
                    c = CompanyInfo(company_name=company,
                                    PRtimes_URL=company_url)
                    c.save()

                #　記事を保存
                if article_title not in all_article_titles:
                    a = Article(company_id=CompanyInfo.objects.filter(company_name=company)[0],
                                title=article_title,
                                article_url=article_url,
                                release_time=article_release_time,
                                )
                    a.save()



            print("Article記事　保存完了:ジャンル={}".format(genre))
