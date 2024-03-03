import os
import yaml
def change_md_quotation_mark():
    with open("./config.yaml", 'r') as file_1:
        data_1 = yaml.safe_load(file_1)
    # 指定包含 markdown_1 文件的文件夹路径
    folder_path = data_1["md_path"]

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            with open(filepath, 'w', encoding='utf-8') as file:
                within_dashes = False
                for line in lines:
                    if line.strip() == '---':
                        within_dashes = not within_dashes
                        file.write(line)
                    elif within_dashes:
                        colon_index = line.find(':')
                        if colon_index != -1:
                            key = line[:colon_index].strip()
                            value = line[colon_index + 1:].strip().strip('\n')
                            updated_line = f"{key}: '{value}'\n"
                            file.write(updated_line)
                        else:
                            file.write(line)
                    else:
                        file.write(line)

    print("md格式处理完成！\n注意：再把md文件导入hugo中时markdown顶部的description（博客简介）一栏中如果存在单引号会引起markdown的语法错误\n作者已经尽力处理了\nhugo在导入报错时记得删去（一般出现该问题的博文很少，或者没有）")