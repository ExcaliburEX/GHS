<p align="center">
  <a href="" rel="noopener">
 <img width=300 height=150 src="https://blog-1259799643.cos.ap-shanghai.myqcloud.com/AutoS%26D_ytb.png" alt="Project logo"></a>
</p>

<h3 align="center">AutoSearchAndDownload</h3>

<div align="center">

[![HitCount](http://hits.dwyl.com/ExcaliburEX/https://githubcom/ExcaliburEX/GHS.svg)](http://hits.dwyl.com/ExcaliburEX/https://githubcom/ExcaliburEX/GHS)
[![Build Status](https://www.travis-ci.org/ExcaliburEX/GHS.svg?branch=master)](https://www.travis-ci.org/ExcaliburEX/GHS)
[![GitHub Issues](https://img.shields.io/github/issues/ExcaliburEX/GHS.svg)](https://github.com/ExcaliburEX/GHS/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/ExcaliburEX/GHS.svg)](https://github.com/ExcaliburEX/GHS/pulls)
![forks](https://img.shields.io/github/forks/ExcaliburEX/GHS)
![stars](	https://img.shields.io/github/stars/ExcaliburEX/GHS)
![repo size](https://img.shields.io/github/repo-size/ExcaliburEX/GHS)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
</div>

---

# ✨开始
- 直接运行[main.py](https://github.com/ExcaliburEX/GHS/blob/master/main.py)即可
- 运行截图
  ![](https://github.com/ExcaliburEX/GHS/blob/master/gif/main.gif)

## 💥1. 运行环境
- chromedriver，通过`chrome://version`查看自己的版本，然后到[chromedriver](http://chromedriver.storage.googleapis.com/index.html)下载对应的chromedriver版本，随便放在哪个文件夹，并把当前文件夹加入到环境变量即可。
- ```python
  pip install -r requirements.txt
  ```
- 根据个人电脑的分辨率以及字体显示的不同需要自己截图修改一下[`\115Image`](https://github.com/ExcaliburEX/GHS/blob/master/115Image)以及[`\ThunderImage`](https://github.com/ExcaliburEX/GHS/blob/master/ThunderImage)。
## 🍓2. 功能介绍
- [Crawl_fc2.py](https://github.com/ExcaliburEX/GHS/blob/master/Crawl_fc2.py)和[Crawl_51luxu.py](https://github.com/ExcaliburEX/GHS/blob/master/Crawl_51luxu.py)
  
  分别从`fc2.club`按照更新时间抓取图片以及`51luxu`上抓取所有图片，其中`51luxu`可选片商有`200GANA`，`230ORE`，`259LUXU`，`261ARA`，`277DCV`，`300MAAN`，`300MIUM`，`SIRO`，`Scute`，`KIRAY`等。并设置`history.txt`文件主要是为了防止重复下载，所以删除移动图片都没关系。
  - 运行效果图
  ![](https://github.com/ExcaliburEX/GHS/blob/master/gif/300mium.gif)

- [Crawl_141jav.py](https://github.com/ExcaliburEX/GHS/blob/master/Crawl_141jav.py)<br><br>
  从今天往前抓取`141jav`上每日更新的番剧图片，也可以自定义日期。因为`141jav`架构在两年前更新过，所以两年以前的老`141jav`上的番剧列表貌似已经无法访问了。

  - 网站布局图：
  ![141jav.png](https://i.loli.net/2020/04/11/Ov912TWezAUtFZL.png)
- [AutoSearchAndDownload.py](https://github.com/ExcaliburEX/GHS/blob/master/AutoSearchAndDownload.py)
  
  根据下载的图片，人工选出想看的，然后放到`test`文件夹，程序会自动从btsow搜索磁链，筛选出影片尺寸最大的，然后通过`opencv`定位115的磁链下载等按钮，用`pyautogui`实现点击，从而实现搜索云下载自动化。
  - 运行效果图
  ![](https://i.loli.net/2020/04/07/V5pSmMNue8CRj1A.gif)


- [AutoSearchAndDownload_Thunder.py](https://github.com/ExcaliburEX/GHS/blob/master/AutoSearchAndDownload_Thunder.py)

  功能就是115的镜像版，针对迅雷设计的。对于迅雷的使用有几个注意点：
  - 下载悬浮窗一定要开着，而且在开始时，保持没有任务在下载，也就是悬浮窗要保持成鸟的图标的状态，当然我的截图是VIP版的，你可以在自己电脑上截图成你的悬浮窗模样替换；
  - 因为第一个任务下载完之后，下一个任务开始时还是需要寻找悬浮窗的鸟图标，所以每次新建完任务之后需要暂停，以免悬浮窗显示的是速度值而不是鸟图标，导致点击失败。  
  - 所有的截图在我的电脑上匹配很成功，在你的💻上使用时，对应地修改一下那些截图。
  - 运行效果图
  ![](https://github.com/ExcaliburEX/GHS/blob/master/gif/Thunder_demo.gif)


# 🍧补充

- 防止有些磁链已经下载过导致的下载框没有正常关闭，用了判断本地的按钮截图与当前屏幕按钮截图是否相似，判断下载框中的某个部位是否还存在来确定是否下载成功。相似度高，说明下载框没有正常关闭，则已经下载过，导致出现了下载提示，然后启动“关闭”按钮。

图片相似度算法：
```python
def compare_img(img1, img2):
    imageA = cv2.imread(img1)
    imageB = cv2.imread(img2)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    return score
```

- 文件结构

| F:         | ...|  |  |  |  |
| ------------- | ------- | -------- | ------- | ------- | -----------------|
|    |  pic   |  300MIUM  |  300MIUM-xxx.jpg    |  ...  | history.txt|
|  |  ... |    fc2 |    fc2-xxxxxx.jpg  |   ... |    history.txt     |
|  |  ... |    test |   300MIUM-xxx.jpg   |  fc2-xxxxxx.jpg  |  ... |

- 仅供娱乐 
