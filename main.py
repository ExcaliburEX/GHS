from Crawl_51luxu import Crawl_51luxu
from Crawl_fc2 import Crawl_fc2
from Crawl_141jav import Crawl_141jav

from AutoSearchAndDownload import AutoSearchAndDownload
from AutoSearchAndDownload_Thunder import AutoSearchAndDownload_Thunder


if __name__ == "__main__":
    while True:
        print("***********************************************")
        print("----------------AutoS&D V1.0------------------")
        print("***********************************************")
        print("*****************主要功能**********************")
        print("*A. 爬取51luxu图片，可选类别如下              *")
        print("*200GANA，230ORE，259LUXU，261ARA，277DCV     *")
        print("*300MAAN，300MIUM，SIRO，S-cute，KIRAY        *")
        print("*B. 爬取fc2图片                               *")
        print("*C. 按日期爬取141jav.com图片                  *")
        print("*D. 根据图片名，自动搜索磁链添加到115下载     *")
        print("*E. 根据图片名，自动搜索磁链添加到迅雷下载    *")
        print("*****************注意事项**********************")
        print("*1. 默认将图片下载到F:/pic/,从第一页开始爬取  *")
        print("*2. 默认从F:/pic/test/中获取图片爬取表        *")
        print("*3. 使用自动下载前，建议修改115和迅雷的截图   *")
        print("*4. 若要自定义请输入2，否则输入666            *")
        print("***********************************************")
        number = input()
        if number == '666':
            while True:
                choice = input("使用ABCDE哪项功能？\n")
                if choice == 'A':
                    while True:
                        category = input(
                            "请输入想要下载的类别，可选参数有：\n200GANA，230ORE，259LUXU，261ARA，277DCV，300MAAN，300MIUM，SIRO，Scute，KIRAY\n")
                        if category in ['200GANA','230ORE','259LUXU','261ARA','277DCV','300MAAN','300MIUM','SIRO','Scute','KIRAY']:
                            break
                        else:
                            print("参数输入错误，请重新输入！")
                    mium = Crawl_51luxu()
                    mium.main(category = category)
                    break
                elif choice == 'B':
                    fc2 = Crawl_fc2()
                    fc2.main()
                    break
                elif choice == 'C':
                    jav = Crawl_141jav()
                    jav.main()
                    break
                elif choice == 'D':
                    AutoSandD = AutoSearchAndDownload()
                    AutoSandD.main()
                elif choice == 'E':
                    AutoSandD_Thunder = AutoSearchAndDownload_Thunder()
                    AutoSandD_Thunder.main()
                    break
                else:
                    print("输入错误，请重新输入！")
            break
        elif number == '2':
            while True:
                choice = input("使用ABCDE哪项功能？\n")
                if choice == 'A':
                    mium = Crawl_51luxu()
                    while True:
                        category = input(
                            "请输入想要下载的类别，可选参数有：\n200GANA，230ORE，259LUXU，261ARA，277DCV，300MAAN，300MIUM，SIRO，Scute，KIRAY\n")
                        if category in ['200GANA','230ORE','259LUXU','261ARA','277DCV','300MAAN','300MIUM','SIRO','Scute','KIRAY']:
                            break
                        else:
                            print("参数输入错误，请重新输入！")
                    folder = input("请输入存储目录，如F:\\pic\\51luxu \n")
                    page = input("请输入下载开始的页码 \n")
                    mium.main(folder + '\\', page, category)
                    break
                elif choice == 'B':
                    fc2 = Crawl_fc2()
                    folder = input("请输入存储目录，如F:\\pic\\51luxu \n")
                    page = input("请输入下载开始的页码 \n")
                    fc2.main(folder + '\\', page)
                    break
                elif choice == 'C':
                    folder = input("请输入存储目录，如F:\\pic\\51luxu \n")
                    page = input("请输入下载开始的日期，如2020/04/11 \n")
                    jav = Crawl_141jav()
                    jav.main(folder + '\\', page)
                    break
                elif choice == 'D':
                    AutoSandD = AutoSearchAndDownload()
                    folder_magnet = input("请输入自动下载要搜寻的目录，如F:\\pic\\test \n")
                    AutoSandD.main(folder_magnet + '\\')
                    break
                elif choice == 'E':
                    AutoSandD_Thunder = AutoSearchAndDownload_Thunder()
                    folder_magnet = input("请输入自动下载要搜寻的目录，如F:\\pic\\test \n")
                    AutoSandD_Thunder.main(folder_magnet + '\\')
                    break
                else:
                    print("输入错误，请重新输入！")
            break
        else:
            print("输入错误，重新输入！")




















