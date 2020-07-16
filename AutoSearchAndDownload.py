from selenium import webdriver
import time, re, os
import pyautogui
import pyperclip
from lxml import etree
import os
from bs4 import BeautifulSoup
import cv2
from skimage.measure import compare_ssim
from selenium.common.exceptions import TimeoutException

class AutoSearchAndDownload:
    def main(self, Dir='F:\\pic\\test\\'):
        # custom_path = 'F:\\pic\\141jav\\2020-06-21\\''F:\\pic\\test\\'
        custom_path = Dir
        url = 'https://btsow.space/search/'
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument("--headless")
        chrome_opts.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        def open_browser(url):
            driver = webdriver.Chrome(options=chrome_opts)
            driver.get(url)
            return driver

        # 求搜索到的磁链中，影片尺寸最大的下标，也就是最高清的那个
        def MaxVideoSizeIndex(unit):
            u = []
            for i in range(len(unit)):
                if unit[i][-2:] == 'MB':
                    u.append(float(unit[i][:-2]) / 1024)
                else:
                    u.append(float(unit[i][:-2]))
            return u.index(max(u))

        # 115下载的各个按钮
        # 这里使用了opencv来判断，而没有用pyautogui的locateonscreen
        # 因为实在是太慢了，而且识别准确率太低
        def click_button(name, flag):
            img = cv2.imread(name + '.png', 0)
            w, h = img.shape[::-1]
            pyautogui.screenshot('screen.png')
            screen = cv2.imread('screen.png', 0)
            res = cv2.matchTemplate(img, screen, eval('cv2.TM_CCOEFF'))
            _, _, _, (x, y) = cv2.minMaxLoc(res)
            os.remove('screen.png')
            if flag == 1:
                pyautogui.click(x + w/2, y + h/2)
            return x,y

        # 比较两张图片的相似度，主要用于判断当前磁链是否已经下载过
        # 如果没下载过，那么点完‘立即下载’下载栏就消失了，比对相似度就很低
        # 如果已经下载过，那么点完‘立即下载’下载栏不会消失，那么比对就会成功，相似度接近1
        # 所以，相似度接近1就判定已经下载过，相似度很低说明没下载过，成功下载+1
        def compare_img(img1, img2):
            imageA = cv2.imread(img1)
            imageB = cv2.imread(img2)

            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

            (score, diff) = compare_ssim(grayA, grayB, full=True)
            return score


        def Auto():
            name = [n.split(".")[0] for n in os.listdir(custom_path)]
            # 获取要下载的链接列表，因为是图片名，去掉后面的'.jpg'只取名字
            cnt = 0
            Fcnt = 0
            driver = webdriver.Chrome(options=chrome_opts)
            for n in name:
                if n != 'log':
                # log文件用来判断有没有下载失败的影片，所以不需要加入搜索
                    try:
                        driver.set_page_load_timeout(10)
                        while True:
                            try:
                                driver.get(url + n)
                                break
                            except TimeoutException:
                                print("加载超时，启动F5刷新,等待3秒")
                                # pyautogui.click(x=509, y=33)
                                # pyautogui.hotkey('f5')
                                # driver.get(url + n)
                                driver.refresh()
                                time.sleep(3)
                        Size = [x.text for x in driver.find_elements_by_xpath("//*[@class='col-sm-2 col-lg-1 hidden-xs text-right size']")]
                        # 获取搜索到的磁链的大小
                        content = driver.page_source.encode('utf-8')
                        soup = BeautifulSoup(content, 'lxml')
                        href = ['https://btsow.space/magnet/detail' + x.replace("\"", "") for x in re.findall(r'/hash/.*?"', str(soup))]
                        # 获取搜索到的磁链的超链接
                        print('%s 一共有 %d 个种子'%(n, len(Size)))
                        print("%s 的尺寸最大为 %s" % (n, Size[MaxVideoSizeIndex(Size)]))
                        time.sleep(1)
                        driver.set_page_load_timeout(10)
                        while True:
                            try:
                                driver.get(href[MaxVideoSizeIndex(Size)])
                                break
                            except TimeoutException:
                                print("加载超时，启动F5刷新,等待3秒")
                                # pyautogui.click(x=509, y=33)
                                # pyautogui.hotkey('f5')
                                # driver.get(href[MaxVideoSizeIndex(Size)])
                                driver.refresh()
                                time.sleep(5)
                        # 进入影片尺寸最大的影片磁链页
                        # pyperclip.copy([x.text for x in driver.find_elements_by_xpath("//*[@class='magnet-link hidden-xs']")][0])
                        mag = driver.find_element_by_xpath("//textarea[@id='magnetLink']").text
                        with open(Dir + 'magnet.txt', 'a+') as f:
                            f.writelines(mag)
                            f.writelines("\n")
                            f.close()
                        print("%s 下载成功！" % (n))
                        # 复制磁链
                        # click_button('button',1)
                        # # 点击‘链接任务按钮’
                        # time.sleep(1)
                        # pyautogui.hotkey('ctrlleft', 'V')
                        # # 粘贴磁链
                        # print("%s 粘贴成功！"%(n))
                        # click_button('download',1)
                        # # 点击‘开始下载’按钮
                        # img = cv2.imread('valid.png', 0)
                        # w, h = img.shape[::-1]
                        # x,y = click_button('valid', 0)
                        # im = pyautogui.screenshot(region=(x, y, w, h))
                        # im.save('screen_valid.png')
                        # score = compare_img('valid.png','screen_valid.png')
                        # os.remove('screen_valid.png')
                        # # 上面几步是通过截图与事先截好的图片判断是任务已经存在还是下载成功
                        # if score >= 0.8:
                        #     click_button('close', 1)
                        #     print("%s 任务已经存在！" % (n))
                        #     print("\n")
                        # else:
                        #     cnt += 1
                        #     print("%s 下载成功！" % (n))
                        #     print("\n")
                    except:
                        print("%s 下载出错！"%(n))
                        print("\n")
                        if not os.path.exists(custom_path + 'log.txt'):
                            with open(custom_path + 'log.txt', "w") as f:
                                f.writelines(n)
                                f.writelines('\n')
                                Fcnt += 1
                                f.close()
                        else:
                            with open(custom_path + 'log.txt', "a+") as f:
                                f.writelines(n)
                                f.writelines('\n')
                                Fcnt += 1
                                f.close()
                        # 出错后将失败的番号加入log.txt
                        # 然后关掉下载框，防止后续任务失败
                        # click_button('close', 1)
                        continue
            print("此次一共消耗 %d 个链接任务！, %d 个任务失败"%(cnt,Fcnt))
            driver.quit()

        os.chdir("115Img/")
        Auto()
