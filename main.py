from Crawl_300mium import Crawl_300mium
from Crawl_fc2 import Crawl_fc2

from AutoSearchAndDownload import AutoSearchAndDownload
from AutoSearchAndDownload_Thunder import AutoSearchAndDownload_Thunder


if __name__ == "__main__":
    mium = mium_crawl()
    mium.main()
    fc2 = Crawl_fc2()
    fc2.main()
    AutoSandD = AutoSearchAndDownload()
    AutoSandD.main()
    AutoSandD_Thunder = AutoSearchAndDownload_Thunder()
    AutoSandD_Thunder.main()

