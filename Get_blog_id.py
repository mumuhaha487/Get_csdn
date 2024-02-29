from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains    #用于自动化框架执行动作
import time     #延时操作，方便网站加载完全
import json     #用于读取配置信息
import re   #从源代码中提取文章的链接
with open("./config.json",'r') as file_1:
    data_1=json.load(file_1)

blog_id=data_1["blog_id"]
url_1=f"https://blog.csdn.net/{blog_id}?type=blog"
driver = webdriver.Chrome()
driver.get(url_1)
for i in range(10000):
    time.sleep(0.5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN)  # 可以多次发送 PAGE_DOWN 来实现滚动的距离
    actions.perform()
    if i % 10 == 0:  # 每滑动 10 次进行判断
        prev_page_source = driver.page_source  # 获取前一次滑动后的页面源码
        time.sleep(2)  # 等待页面加载
        current_page_source = driver.page_source  # 获取当前页面源码

        if prev_page_source == current_page_source:
            print("网站滑倒底了，跳出循环...")
            break

req_1=driver.page_source
re_1='<a data-v-6fe2b6a7="" href="(.*?)"'
blog_urls=re.findall(re_1,req_1)
print(f"文章个数为{len(blog_urls)}（看看是不是全爬下来了）")