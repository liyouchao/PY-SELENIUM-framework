import os,time
from selenium import webdriver
import  unittest
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH,DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader

# excel = DATA_PATH + '/baidu.xlsx'
# datas = ExcelReader(excel).data
# for d in datas:
#     print(d['search'])

print(time.strftime("%Y-%m-%d %H:%H:%H",time.localtime()))
print(time.localtime())