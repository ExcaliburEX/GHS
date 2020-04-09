from selenium import webdriver
import time
import re
import os
import pyautogui
import pyperclip
from lxml import etree
import os
from bs4 import BeautifulSoup
import cv2
from skimage.measure import compare_ssim


class AutoSearchAndDownload_Thunder:
    def main(self, Dir='F:\\pic\\test\\'):
        # custom_path = 'F:\\pic\\test\\'
        custom_path = Dir
        url = 'https://btsow.club/search/'

        def open_browser(url):
            driver = webdriver.Chrome()
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
            img = cv2.imread(name + '.png', 1)
            w, h = img.shape[:-1]
            pyautogui.screenshot('screen.png')
            screen = cv2.imread('screen.png', 1)
            res = cv2.matchTemplate(img, screen, eval('cv2.TM_CCOEFF'))
            _, _, _, (x, y) = cv2.minMaxLoc(res)
            os.remove('screen.png')
            if flag == 1:  # 1为点击，0就不点击
                pyautogui.click(x + h/2, y + w/2)
            return x, y


        def click_button_2(name):
            img = cv2.imread(name + '.png', 1)
            w, h = img.shape[:-1]
            pyautogui.screenshot('screen.png')
            screen = cv2.imread('screen.png', 1)
            res = cv2.matchTemplate(img, screen, eval('cv2.TM_CCOEFF'))
            _, _, _, (x, y) = cv2.minMaxLoc(res)
            os.remove('screen.png')
            pyautogui.click(x + h/2, y + w/2)
            time.sleep(1)
            pyautogui.click(x + h/2, y + w/2)
            return x, y


        def click_button_right(name):
            img = cv2.imread(name + '.png', 1)
            w, h = img.shape[:-1]
            pyautogui.screenshot('screen.png')
            screen = cv2.imread('screen.png', 1)
            res = cv2.matchTemplate(img, screen, eval('cv2.TM_CCOEFF'))
            _, _, _, (x, y) = cv2.minMaxLoc(res)
            os.remove('screen.png')
            pyautogui.click(x + h/2, y + w/2,button='right')
            return x, y
        # 比较两张图片的相似度，主要用于判断当前磁链是否已经下载过
        # 如果没下载过，那么点完‘立即下载’下载栏就消失了，比对相似度就很低
        # 如果已经下载过，那么点完‘立即下载’下载栏不会消失，那么比对就会成功，相似度接近1
        # 所以，相似度接近1就判定已经下载过，相似度很低说明没下载过，成功下载+1


        def compare_img(img1, img2):
            imageA = cv2.imread(img1, 1)
            imageB = cv2.imread(img2, 1)

            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

            (score, diff) = compare_ssim(grayA, grayB, full=True)
            print("匹配度：%f"%(score))
            return score



        def CreateSpecificScreenShot(PicName):
            img = cv2.imread(PicName + '.png', 1)
            w, h = img.shape[:-1]
            x, y = click_button(PicName, 0)
            im = pyautogui.screenshot(region=(x, y, h, w))
            im.save('screen_valid.png')


        def JudgeIfShow(PicName):
            while True:
                CreateSpecificScreenShot(PicName)
                if compare_img(PicName + '.png', 'screen_valid.png') < 0.8:
                    time.sleep(0.5)  # 只要没有在屏幕上没有匹配到“立即下载”按钮，就不断等待
                    print("等待按钮 %s 出现！" % (PicName))
                    os.remove('screen_valid.png')
                else:
                    os.remove('screen_valid.png')
                    break



        def Auto():
            name = [n.split(".")[0] for n in os.listdir(custom_path)]
            # 获取要下载的链接列表，因为是图片名，去掉后面的'.jpg'只取名字
            cnt = 0
            Fcnt = 0
            driver = webdriver.Chrome()
            for n in name:
                if n != 'log':
                    # log文件用来判断有没有下载失败的影片，所以不需要加入搜索
                    try:
                        driver.get(url + n)
                        Size = [x.text for x in driver.find_elements_by_xpath(
                            "//*[@class='col-sm-2 col-lg-1 hidden-xs text-right size']")]
                        # 获取搜索到的磁链的大小
                        content = driver.page_source.encode('utf-8')
                        soup = BeautifulSoup(content, 'lxml')
                        href = ['https://btsow.club/magnet/detail' +
                                x.replace("\"", "") for x in re.findall(r'/hash/.*?"', str(soup))]
                        # 获取搜索到的磁链的超链接
                        print('%s 一共有 %d 个种子' % (n, len(Size)))
                        print("%s 的尺寸最大为 %s" % (n, Size[MaxVideoSizeIndex(Size)]))
                        time.sleep(2)
                        driver.get(href[MaxVideoSizeIndex(Size)])
                        # 进入影片尺寸最大的影片磁链页
                        pyperclip.copy([x.text for x in driver.find_elements_by_xpath(
                            "//*[@class='magnet-link hidden-xs']")][0])

                        click_button_right('bird')
                        time.sleep(1)
                        click_button('N', 1)
                        JudgeIfShow('ThunderDownload')
                        pyautogui.hotkey('ctrlleft', 'V')
                        # click_button_2('AllCoverPressed')
                        # time.sleep(0.5)
                        # videoType = ['mkv', 'mp4', 'avi', 'rmvb']
                        
                        # for v in videoType:
                        #     CreateSpecificScreenShot(v)
                        #     if compare_img(v + '.png', 'screen_valid.png') >= 0.8:
                        #         click_button(v, 1)
                        #         os.remove('screen_valid.png')
                        #         break
                        #     else:
                        #         os.remove('screen_valid.png')
                        time.sleep(1)
                        click_button('ThunderDownload', 1)
                        JudgeIfShow('ThunderDownload')
                        click_button('ThunderDownload', 1)
                        # 点击‘开始下载’按钮
                        time.sleep(3)
                        CreateSpecificScreenShot('AlreadyDownloaded')
                        score1 = compare_img(
                            'AlreadyDownloaded.png', 'screen_valid.png')
                        os.remove('screen_valid.png')
                        CreateSpecificScreenShot('same')
                        score2 = compare_img(
                            'same.png', 'screen_valid.png')
                        os.remove('screen_valid.png')
                        # 上面几步是通过截图与事先截好的图片判断是任务已经存在还是下载成功
                        time.sleep(1)
                        if score1 >= 0.8:
                            print("%s 任务已经存在！" % (n))
                            click_button('ThunderClose', 1)
                            print("\n")
                        elif score2 >= 0.8:
                            print("%s 相同任务！" % (n))
                            click_button('No', 1)
                            print("\n")
                        else:
                            cnt += 1
                            print("%s 下载成功！" % (n))
                            JudgeIfShow('bird1')
                            click_button_right('bird1')
                            time.sleep(1)
                            click_button('pause', 1)
                            # 暂停的原因是，下一个任务的开启是要找悬浮窗的鸟图标
                            # 任务开始后，显示的是速度，那么没有小鸟就无法定位悬浮窗了
                            # 为了方便起见，还是每次新建任务后暂停所有任务
                            print("\n")
                    except:
                        print("%s 下载出错！" % (n))
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
                        continue
            print("此次一共消耗 %d 个链接任务！, %d 个任务失败" % (cnt, Fcnt))

        os.chdir("ThunderImg/")
        Auto()
