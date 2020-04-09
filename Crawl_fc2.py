from selenium import webdriver
import time, re, os
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip
from lxml import etree
import os
from bs4 import BeautifulSoup

# 主要功能就是访问fc2所有影片按时间更新的详情页，然后挨个下载具体影片的视频截图
class Crawl_fc2:
    def main(self, Dir='F:\\pic\\fc2\\', page=1):
        url = 'https://fc2club.com/index.php?m=content&c=index&a=lists&catid=12' + '&page=' + str(page)
        url_prefix = 'https://fc2club.com/html/'
        # custom_path = 'F:\\pic\\fc2' + '\\'
        custom_path = Dir
        def open_browser(url):
            driver = webdriver.Chrome()
            driver.get(url)
            return driver

        def scrapy(driver):
            if not os.path.exists(custom_path):
                os.mkdir(custom_path)
            Exist = []
            if os.path.exists(custom_path + 'history.txt'):
                with open(custom_path + 'history.txt','r+') as f:
                    lines = f.readlines()
                    for line in lines:
                        Exist.append(line.replace("\n",""))
                    f.close()
            # 从history中读入历史的所下载的图片的名字，以免重复下载
            # 这一步主要是为了，当我筛选图片时，看到好看的要保留，看到不好看的要删除
            # 那么读取文件列表就乱了套了，所以把历史下载保存在txt文件中，就知道之前有没有下过这个番号了
            for page in range(1000):
                try:
                    html = driver.page_source
                    html = etree.HTML(html)
                    name = [x.text for x in html.xpath("//a[@class='author']")]
                    # 返回的是element的对象，所以要取它的text
                    driver_info = webdriver.Chrome()
                    for i in range(len(name)):
                        if name[i] in Exist:
                            print('%s 已经存在！' % (name[i]))
                            continue
                        # 前文提到的判断是否下过，如果是，后面就不用进行了
                        # 进入相应链接的详情页
                        driver_info.get(url_prefix + name[i] + '.html')
                        # 进入各个影片的详情页，因为链接就是名字加html，所以直接保存番号就行了
                        content = driver_info.page_source.encode('utf-8')
                        soup = BeautifulSoup(content, 'lxml')
                        href = url_prefix[:-5] + ''.join(re.findall(r'href="/uploadfile/.*?"',str(soup))).split("\"")[1].split("\"")[0]
                        # 进入详情页后，获取视频截图的链接
                        driver_info.get(href) # 进入视频截图页面
                        wait = WebDriverWait(driver_info, 10)  # 等待浏览器相应，删除也可以
                        pyautogui.rightClick(x=500, y=500)  # 右击图片，位置可根据自己的屏幕调整
                        pyautogui.typewrite(['V'])  # 另存为的快捷键为 V
                        time.sleep(3)
                        pyperclip.copy(custom_path + name[i] + '.jpg')  # 复制文件名加路径到粘贴板
                        pyautogui.hotkey('ctrlleft', 'V')  # 粘贴
                        time.sleep(1)
                        pyautogui.press('enter')  # 确认
                        with open(custom_path + 'history.txt', 'a+') as f:
                            f.writelines(name[i])
                            f.writelines('\n')
                            f.close()
                        # 在txt中加入当前下载的图片名字
                        print("%s 下载完成！" % (name[i]))
                        time.sleep(0.2)
                    driver_info.quit()
                    print("第 %d 页爬完" % (page + 1))
                    button = "//*[@href='https://fc2club.com/index.php?m=content&c=index&a=lists&catid=12&page=" + str(page + 2) + "']"  #翻页按钮
                    driver.find_elements_by_xpath(button)[0].click()
                except:
                    print("第 %d 页出错！" % (page))
                    driver_info.quit()
                    button = "//*[@href='https://fc2club.com/index.php?m=content&c=index&a=lists&catid=12&page=" + str(page + 2) + "']"  #翻页按钮
                    driver.find_elements_by_xpath(button)[0].click()


        driver = open_browser(url)
        scrapy(driver)
