import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from fake_useragent import UserAgent
from time import sleep
from random import randint

root_folder = "dataset" # Папка в которой будут хранится другие

def create_driver():
    """
        Функция создает WebDriver Chrome для выполнения кода
    """
    options = webdriver.ChromeOptions()
    # Добавляем различные опции для того, чтобы браузер не обнаружил Webdriver
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    ua = UserAgent().random
    # selenium-stealth позволяет замаскировать использование Webdriver
    stealth(driver=driver,
            user_agent=ua,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            run_on_insecure_origins=True
            )
    return driver


def createFolder(name : str):
    """
        Функция создает папку name, если её ещё нет
    """
    if not os.path.exists(name):
        print(f"Создаем папку {name}")
        os.mkdir(name)

def saveImages(name : str, urls : set):
    """
        Функция загружает все изображения по ссылкам из urls
        и сохраняет их в папку name
    """
    createFolder(name)
    i = 1
    for img_url in urls:
        try:
            _img = requests.get("https:" + str(img_url))
            file = open(f"{name}/{str(i).zfill(4)}.jpg", "wb")
            file.write(_img.content)
            file.close()
            i+=1
        except:
            continue
    print(f"Сохранено {i-1} фото")


def GetImageUrl(driver, url_list : set):
    """
        Функция собирает все ссылки на первоисточник фото
        со страницы и добавляет их в url_list
    """
    soup = BeautifulSoup(driver.page_source, "lxml")
    links = soup.find_all("img", class_ = "ImagesContentImage-Image ImagesContentImage-Image_clickable")
    for link in links:
         try:
            link = link.get("src")
            url_list.add(link)
         except:
             continue   
    return url_list        


def FindYandexImages(name: str, IMAGE_GOAL = 1050):
    """
        Функция находит name в Яндекс изображениях и собирает более IMAGE_GOAL ссылок
        на них, потом сохраняет их в папке с тем же именем
    """
    try:
        pause = 5 # указывает паузу между запросами
        MAX_LOOPS = 6 # максимальное кол-во циклов
        urls_len = 0 # длина множества с адресами изображений(кол-во ссылок)
        loops_count = 0 # кол-во циклов
        url_list = set() # множество ссылок

        # К запросу в конце добавлено &isize=small для того, чтобы выбирались фото небольшого веса
        # чтобы большее кол-во можно было вложить в архив
        url = f'https://yandex.ru/images/search?text={name}&isize=small'.replace(' ', '+')

        with create_driver() as driver:
            print(f"Посылаем запрос по {name}.\nЗапрашивается около {IMAGE_GOAL} фото.")
            driver.get(url)
            sleep(pause * 3)
            while len(url_list) < IMAGE_GOAL and loops_count < MAX_LOOPS:
                if "captcha" in driver.page_source.lower():
                    print("В браузере появилась капча.\nРешите её сами или завершите программу.")
                    while "captcha" in driver.page_source.lower():
                        sleep(pause * 2)

                print("Собираем ссылки.")
                url_list = GetImageUrl(driver, url_list)

                sleep(randint(pause,pause * 2))
                print(f"Кол-во ссылок {len(url_list)}")
                #Если длинна множества не меняется то, сбор ссылок заканчивается
                if len(url_list) == urls_len:
                    loops_count +=1
                else:
                    urls_len = len(url_list)
                    loops_count = 0

                print("Промотаем страницу вниз")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(randint(pause * 2 ,pause * 3))
                try:
                    #Ищем кнопку "Показать ещё" и если есть нажимаем
                    button = driver.find_element(By.CLASS_NAME, "FetchListButton-Button")
                    button.click()
                    print("Нажали кнопку 'Показать ещё'")
                    sleep(randint(pause * 2 ,pause * 3))
                except:
                    continue

        # Закрывается сессия
        print(f"Поиск фото завершен.")
        # к названию папки добавляется корневая
        full_name = root_folder + "/" + name
        # Фото сохраняются по url
        saveImages(full_name, url_list)
        print(f"Сохранение фото завершено.")

    except Exception as ex:
        print(ex)   

if __name__ == '__main__':
    createFolder(root_folder)
    FindYandexImages("brown bear")
    FindYandexImages("polar bear")