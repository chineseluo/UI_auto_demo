#coding:utf-8
import os
import configparser

#获取项目路劲
def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]

def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + "\config.ini")
    print(project_path() + "\config.ini")
    return config.get("testUrl","url")

if __name__ == "__main__":
    print("项目路径为："+project_path())
    print("被测系统的URL为:"+config_url())
