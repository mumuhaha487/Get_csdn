import requests
import json
import re
import os
def Get_blog_img(url_1):
    with open("./config.json", 'r') as file_1:
        data_1 = json.load(file_1)

    cookie_1=data_1["cookie"]
    img_1=data_1["img_path"]
    head_1={
        "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Cookie" : cookie_1
    }
    req_1=requests.get(url=url_1,headers=head_1)
    re_1='src="(https://img-blog.csdnimg.cn.*?.png)"'
    re_2='src="https://img-blog.csdnimg.cn/(.*?.png)"'
    img_ids=re.findall(re_2,req_1.text)
    img_urls=re.findall(re_1,req_1.text)
    for i in range(len(img_ids)):
        dir_name,file_name=os.path.split(img_ids[i])
        if dir_name:
            os.makedirs(f"{img_1}/{dir_name}",exist_ok=True)
        img_response=requests.get(url=img_urls[i],headers=head_1)
        if dir_name:
            with open(f'{img_1}/{dir_name}/{file_name}', 'wb') as f:
                f.write(img_response.content)
        else:
            with open(f'{img_1}/{file_name}', 'wb') as f:
                f.write(img_response.content)

