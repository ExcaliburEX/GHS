from selenium import webdriver
import time
import re
import os
from bs4 import BeautifulSoup
import pyautogui
import pyperclip
from lxml import etree
import datetime
from selenium.common.exceptions import TimeoutException

class Crawl_141jav:
    def main(self, Dir='F:\\pic\\141jav\\', startTime= datetime.date.today()):
        #custom_path = 'F:\\pic\\141jav\\'
        custom_path = Dir
        url = 'https://www.141jav.com/date/'

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
            driver = webdriver.Chrome()
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
                            print("加载超时，启动F5刷新,等待5秒")
                            pyautogui.click(x=509, y=33)
                            pyautogui.hotkey('f5')
                            driver.get(url+date)
                            time.sleep(5)
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
                                    print("加载超时，启动F5刷新，等待5秒")
                                    pyautogui.click(x=509, y=33)
                                    pyautogui.hotkey('f5')
                                    driver.get(url+date+'?page='+str(page+1))
                                    time.sleep(5)
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

                            driver_info = webdriver.Chrome()
                            for i in range(len(href)):
                                if name[i] in Exist:
                                    print('%s 已经存在！' % (name[i]))
                                    continue
                                driver_info.get(href[i])
                                pyautogui.rightClick(x=500, y=500)
                                pyautogui.typewrite(['V'])
                                time.sleep(2)
                                pyperclip.copy(custom_path + date.replace('/', '-')+'\\' + name[i] + '.jpg')
                                pyautogui.hotkey('ctrlleft', 'V')
                                time.sleep(1)
                                pyautogui.press('enter')
                                time.sleep(1)
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
                                        pyautogui.hotkey('ctrlleft', 'V')  # 粘贴
                                        time.sleep(1)
                                        pyautogui.press('enter')  # 确认
                                        time.sleep(1)
                            time.sleep(2)    
                            driver_info.quit()
                        except:
                            print("%s 共 %d 页结束！" % (date, page+1))
                            break
                except:
                    print("%s 还未发布！"%(date))
                    continue

        scrapy()
