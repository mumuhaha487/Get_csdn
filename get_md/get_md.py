import subprocess
import Get_blog_id
import os
import yaml
def get_md():
    url_ids=Get_blog_id.Get_blog_id()
    with open("./config.yaml", 'r') as file_1:
        data_1 = yaml.safe_load(file_1)

    path_1=data_1["md_path"]
    os.makedirs(path_1,exist_ok=True)
    current_directory = os.getcwd()
    os.chdir(path_1)
    for url_id in url_ids:
        # 执行 cmd 命令
        cmd_command = f'{current_directory}/npm/clean-mark_1 "{url_id}" --name-title'
        process = subprocess.Popen(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # 打印执行结果
        if output:
            print("命令执行结果：")
            print(output.decode('utf-8'))
        if error:
            print("命令执行错误：")
            print(error.decode('utf-8'))