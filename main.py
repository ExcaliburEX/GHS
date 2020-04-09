from Crawl_300mium import Crawl_300mium
from Crawl_fc2 import Crawl_fc2

from AutoSearchAndDownload import AutoSearchAndDownload
from AutoSearchAndDownload_Thunder import AutoSearchAndDownload_Thunder


if __name__ == "__main__":
    print("**********************************************")
    print("----------------AutoS&D V1.0------------------")
    print("**********************************************")
    print("*****************主要功能**********************")
    print("*A. 爬取300MIUM图片                           *")
    print("*B. 爬取fc2图片                               *")
    print("*C. 根据图片名，自动搜索磁链添加到115下载     *")
    print("*D. 根据图片名，自动搜索磁链添加到迅雷下载    *")
    print("*****************注意事项**********************")
    print("*1. 默认将图片下载到F:/pic/,从第一页开始爬取  *")
    print("*2. 默认从F:/pic/test/中获取图片爬取表        *")
    print("*3. 使用自动下载前，建议修改115和迅雷的截图   *")
    print("*4. 若要自定义请输入2，否则输入666            *")
    print("***********************************************")
    while True:  
        number = input()
        if number == '666':
            while True:
                choice = input("使用ABCD哪项功能？")
                if choice == 'A':
                    mium = Crawl_300mium()
                    mium.main()
                    break
                elif choice == 'B':
                    fc2 = Crawl_fc2()
                    fc2.main()
                    break
                elif choice == 'C':
                    AutoSandD = AutoSearchAndDownload()
                    AutoSandD.main()
                    break
                elif choice == 'D':
                    AutoSandD_Thunder = AutoSearchAndDownload_Thunder()
                    AutoSandD_Thunder.main()
                    break
                else:
                    print("输入错误，请重新输入！")
            break
        elif number == '2':
            while True:
                choice = input("使用ABCD哪项功能？")
                if choice == 'A':
                    mium = Crawl_300mium()
                    folder = input("请输入存储目录，如F:\\pic\\300mium \n")
                    page = input("请输入下载开始的页码 \n")
                    mium.main(folder + '\\', page)
                    break
                elif choice == 'B':
                    fc2 = Crawl_fc2()
                    folder = input("请输入存储目录，如F:\\pic\\300mium \n")
                    page = input("请输入下载开始的页码 \n")
                    fc2.main(folder + '\\', page)
                    break
                elif choice == 'C':
                    AutoSandD = AutoSearchAndDownload()
                    folder_magnet = input("请输入自动下载要搜寻的目录，如F:\\pic\\test \n")
                    AutoSandD.main(folder_magnet + '\\')
                    break
                elif choice == 'D':
                    AutoSandD_Thunder = AutoSearchAndDownload_Thunder()
                    folder_magnet = input("请输入自动下载要搜寻的目录，如F:\\pic\\test \n")
                    AutoSandD_Thunder.main(folder_magnet + '\\')
                    break
                else:
                    print("输入错误，请重新输入！")
            break
        else:
            print("输入错误，重新输入！")




















