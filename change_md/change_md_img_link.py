import os
import yaml
def change_md_img_link():
    with open("./config.yaml", 'r') as file_1:
        data_1 = yaml.safe_load(file_1)
    # 指定 Markdown 文件夹路径
    folder_path = data_1["md_path"]

    # 定义要查找和替换的字符串
    old_str = data_1["old_img_link"]
    new_str = data_1["you_blog_link"]

    # 遍历文件夹内的所有文件
    for root, dirs, files in os.walk(f"./{folder_path}"):
        for file_name in files:
            if file_name.endswith('.md'):  # 只处理 Markdown 文件
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # 替换特定字符串
                new_content = content.replace(old_str, new_str)

                # 写入替换后的内容到文件中
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)

    print("图片链接处理完成！")
