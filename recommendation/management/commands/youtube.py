from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup
from recommendation.models import Wine
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Loads data from wine.csv"

    def handle(self, *args, **options):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        wines = Wine.objects.all()
        for i, wine in enumerate(wines):
            if (wine.ytinfo is None) or (wine.ytinfo == ''):
                keyword = wine.name + 'wine'
                keyword = ''.join([i for i in keyword if not i.isdigit()])
                print('keyword:', keyword)

                url = 'https://www.youtube.com/results?search_query={}'.format(keyword)

                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'lxml')

                name = soup.select('a#video-title')
                video_url = soup.select('a#video-title')

                name_list = []
                url_list = []

                for j in range(len(name)):
                    name_list.append(name[j].text.strip())
                for n in video_url:
                    url_list.append('{}{}'.format('https://www.youtube.com', n.get('href')))

                try:
                    # print('name:', name_list[0])
                    # print('url:', url_list[0])
                    wine.ytinfo = name_list[0]
                    wine.yturl = url_list[0]
                    print(f'{i}번째 wine.name:', wine.name)
                    print('wine.ytinfo:', wine.ytinfo)
                    print('wine.yturl:', wine.url_list)
                    print()
                except:
                    pass

            wine.save()

        driver.close()
