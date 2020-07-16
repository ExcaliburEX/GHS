from selenium import webdriver
import time
import re
import os
from bs4 import BeautifulSoup
import pyautogui
import pyperclip
from lxml import etree
import datetime
import requests
from selenium.common.exceptions import TimeoutException






class Crawl_141jav:
    def main(self, Dir='F:\\pic\\141jav\\', startTime= datetime.date.today()):
        #custom_path = 'F:\\pic\\141jav\\'
        custom_path = Dir
        url = 'https://www.141jav.com/date/'
        header = {
            'authority': 'pics.dmm.co.jp: method: GET: path: / mono/movie/adult/h_283pym342/h_283pym342pl.jpg: scheme: https', 'accept': 'text/html, application/xhtml+xml, application/xml;q = 0.9, image/webp, image/apng, */*;q = 0.8, application/signed-exchange;v = b3;q = 0.9', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN, zh;q = 0.9', 'cache-control': 'max-age = 0', 'cookie': 'app_uid = ygb2Cl7o451QgzBdxXNMAg ==', 'if-modified-since': 'Mon, 11 May 2020 07: 05: 40 GMT', 'if-none-match': "5eb8f944-34473", 'referer': 'https: // www.141jav.com/date/2020/06/16?page = 1', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        }
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument("--headless")
        chrome_opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        def timeCount(flag, EndTime='2014/6/6'):
            timeList = []
            begin = datetime.date(2014, 6, 25)
            if flag == 0:
                year = int(EndTime.split('/')[0])
                month = int(EndTime.split('/')[1])
                date = int(EndTime.split('/')[2])
                end = datetime.date(year, month, date)
            else:
                end = datetime.date.today()
            for i in range((end - begin).days+1):
                day = begin + datetime.timedelta(days=(end - begin).days-i)
                timeList.append(str(day).replace("-", "/"))
            return timeList

        def scrapy():
            if startTime == datetime.date.today():
                timeList = timeCount(1)
            else:
                timeList = timeCount(0,startTime)
            driver = webdriver.Chrome(options=chrome_opts)
            Exist = []
            if os.path.exists(custom_path + 'history.txt'):
                with open(custom_path + 'history.txt','r+') as f:
                    lines = f.readlines()
                    for line in lines:
                        Exist.append(line.replace("\n",""))
                    f.close()
            for date in timeList:
                try:
                    driver.set_page_load_timeout(10)
                    while True:
                        try:
                            driver.get(url+date)
                            break
                        except TimeoutException:
                            print("加载超时，启动F5刷新,等待3秒")
                            # pyautogui.click(x=509, y=33)
                            # pyautogui.hotkey('f5')
                            # driver.get(url+date)
                            driver.refresh()
                            time.sleep(3)
                    if not os.path.exists(custom_path):
                        os.mkdir(custom_path)
                    if not os.path.exists(custom_path+date.replace('/','-')+'\\'):
                        os.mkdir(custom_path+date.replace('/', '-')+'\\')
                    videoNumber = 0
                    for page in range(100):
                        try:
                            driver.set_page_load_timeout(10)
                            while True:
                                try:
                                    driver.get(url+date+'?page='+str(page+1))
                                    break
                                except TimeoutException:
                                    print("加载超时，启动F5刷新，等待3秒")
                                    # pyautogui.click(x=509, y=33)
                                    # pyautogui.hotkey('f5')
                                    driver.refresh()
                                    time.sleep(3)
                            content = driver.page_source.encode('utf-8')
                            html = etree.HTML(content)
                            soup = BeautifulSoup(content, 'lxml')
                            href = [x.attrib['src'] for x in html.xpath("//img[@class='image']")]
                            videoNumber += len(href)
                            if len(href) == 0:
                                print("%s 共 %d 部片！" % (date, videoNumber))
                                break
                            name = [x.text.replace("\n", "") for x in html.xpath(
                                "//h5[@class='title is-4 is-spaced']/a")]

                            driver_info = webdriver.Chrome(options=chrome_opts)
                            for i in range(len(href)):
                                if name[i] in Exist:
                                    print('%s 已经存在！' % (name[i]))
                                    continue
                                driver_info.get(href[i])
                                img = driver_info.find_element_by_xpath("//html/body/img")
                                img.screenshot(custom_path + date.replace('/', '-')+'\\' + name[i] + '.jpg')
                                # pyautogui.rightClick(x=500, y=500)
                                # pyautogui.typewrite(['V'])
                                # time.sleep(2)
                                # pyperclip.copy(custom_path + date.replace('/', '-')+'\\' + name[i] + '.jpg')
                                # pyautogui.hotkey('ctrlleft', 'V')
                                # time.sleep(1)
                                # pyautogui.press('enter')
                                # time.sleep(1)

                                # while True:
                                #     try:
                                #         r = requests.get(href[i], headers=header)
                                #         r.raise_for_status()
                                #         break
                                #     except:
                                #         print("超时异常")
                                # with open(date.replace('/', '-')+'\\' + name[i] + '.jpg', 'wb') as f:
                                #     f.write(r.content)
                                # f.close()
                                while True: 
                                    filelist = os.listdir(custom_path+date.replace('/', '-')+'\\')
                                    if name[i] + '.jpg' in filelist:
                                        with open(custom_path + 'history.txt', 'a+') as f:
                                            f.writelines(name[i])
                                            f.writelines('\n')
                                            f.close()
                                        print("%s 下载完成！" % (name[i]))
                                        break   
                                    else:
                                        print("等待响应")
                                        time.sleep(2)
                                        # pyautogui.hotkey('ctrlleft', 'V')  # 粘贴
                                        # time.sleep(1)
                                        # pyautogui.press('enter')  # 确认
                                        # time.sleep(1)
                                        # print("没看到文件")
                            time.sleep(0.5)    
                            driver_info.quit()
                        except:
                            print("%s 共 %d 页结束！" % (date, page+1))
                            break
                except:
                    print("%s 还未发布！"%(date))
                    continue

        scrapy()
