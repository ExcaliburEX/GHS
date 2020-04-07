<p align="center">
  <a href="" rel="noopener">
 <img width=300 height=150 src="https://i.loli.net/2020/04/07/3PRFLGBgkeKtbCZ.png" alt="Project logo"></a>
</p>

<h3 align="center">AutoSearchAndDownload</h3>

<div align="center">

[![HitCount](http://hits.dwyl.com/ExcaliburEX/https://githubcom/ExcaliburEX/GHS.svg)](http://hits.dwyl.com/ExcaliburEX/https://githubcom/ExcaliburEX/GHS)
[![GitHub Issues](https://img.shields.io/github/issues/ExcaliburEX/GHS.svg)](https://github.com/ExcaliburEX/GHS/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/ExcaliburEX/GHS.svg)](https://github.com/ExcaliburEX/GHS/pulls)
![forks](https://img.shields.io/github/forks/ExcaliburEX/GHS)
![stars](	https://img.shields.io/github/stars/ExcaliburEX/GHS)
![repo size](https://img.shields.io/github/repo-size/ExcaliburEX/GHS)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
</div>

---

# ✨开始

## 💥1. 运行环境
- chromedriver，通过`chrome://version`查看自己的版本，然后到[chromedriver](http://chromedriver.storage.googleapis.com/index.html)下载对应的chromedriver版本，随便放在哪个文件夹，并把当前文件夹加入到环境变量即可。
- ```python
  pip install -r requirements.txt
  ```
- `button.png`，`download.png`，`valid.png`，`close.png`根据个人电脑的分辨率以及字体显示的不同需要自己截图修改一下。
## 🍓2. 功能介绍
- [fc2_crawl.py](https://github.com/ExcaliburEX/GHS/blob/master/fc2_crawl.py)和[300mium_crawl.py](https://github.com/ExcaliburEX/GHS/blob/master/300mium_crawl.py)
  
  分别从fc2.club按照更新时间抓取图片以及300mium抓取所有图片。并设置history.txt文件主要是为了防止重复下载，所以删除移动图片都没关系。
  - 运行效果图
  ![](https://i.loli.net/2020/04/07/gFXRwJ9xaimDh5W.gif)
- [AutoSearchAndDownload.py](https://github.com/ExcaliburEX/GHS/blob/master/AutoSearchAndDownload.py)
  
  根据下载的图片，人工选出想看的，然后放到`test`文件夹，程序会自动从btsow搜索磁链，筛选出影片尺寸最大的，然后通过`opencv`定位115的磁链下载等按钮，用`pyautogui`实现点击，从而实现搜索云下载自动化。
  - 运行效果图
  ![](https://i.loli.net/2020/04/07/V5pSmMNue8CRj1A.gif)  

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