from selenium import webdriver
import time, re
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip
import os

# 主要功能就是访问300mium所有影片详情页，然后挨个下载封面
class Crawl_300mium:
    def main(self, Dir='F:\\pic\\300MIUM\\', page=1):
        current_path = os.getcwd().replace('\\', '/') + '/'
        # custom_path = 'F:\\pic\\300MIUM\\'
        custom_path = Dir
        url = 'https://www.51luxu.com/category/sresource/300mium/' + 'page/' + str(page)
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
            for page in range(1,100):
                try:
                    content = driver.page_source.encode('utf-8')
                    soup = BeautifulSoup(content, 'lxml')
                    img = soup.find_all('img')
                    src1 = re.findall(r'src=".*?"', str(img))
                    name1 = re.findall(r'alt=".*?"', str(img))
                    src2 = []
                    name2 = []
                    for i in src1:
                        src2.append(i.split('=')[1].replace("\"",""))
                    for i in name1:
                        name2.append(i.split('=')[1].replace("\"", ""))
                    src3 = [x for x in src2 if "300" in x]
                    name3 = [x for x in name2 if "300" in x]
                    # 上面是name3和src3 保存了主页面的番号和相应的详情页的链接
                    # 接下来启动第二个浏览器对各个详情页的视频截图进行抓取
                    driver1 = webdriver.Chrome()
                    for i in range(12):
                        title = name3[i].split('【')[1].split('】')[0] # 简化一下番号的名字
                        if title in Exist:
                            print("%s 已经下载！" % (title))
                            continue
                        # 前文提到的判断是否下过，如果是，后面就不用进行了
                        # 进入相应链接的详情页
                        driver1.get(src3[i])
                        wait = WebDriverWait(driver1, 10) # 等待浏览器相应，删除也可以
                        pyautogui.rightClick(x=500, y=500) # 右击图片，位置可根据自己的屏幕调整
                        pyautogui.typewrite(['V']) # 另存为的快捷键为 V
                        time.sleep(2) # 等待电脑响应
                        pyperclip.copy(custom_path + title + '.jpg')  # 复制文件名加路径到粘贴板
                        time.sleep(1)
                        pyautogui.hotkey('ctrlleft', 'V') # 粘贴
                        time.sleep(1)
                        pyautogui.press('enter') # 确认
                        time.sleep(0.2)
                        with open(custom_path + 'history.txt', 'a+') as f:
                            f.writelines(title)
                            f.writelines('\n')
                            f.close()
                        # 在txt中加入当前下载的图片名字
                        print("%s 下载完成！"%(title))
                    driver1.quit()
                    print("第 %d 页爬完"%(page))
                    button =  "//*[@class='next page-numbers']"  #翻页按钮
                    driver.find_elements_by_xpath(button)[0].click()
                except:
                    print("第 %d 页出错！"%(page))
                    continue

        driver = open_browser(url)
        time.sleep(2)
        scrapy(driver)
