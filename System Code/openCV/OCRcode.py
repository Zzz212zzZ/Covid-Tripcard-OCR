import os,sys
import time

import cv2
import re
import glob
import json
import easyocr
from datetime import datetime
from werkzeug.utils import secure_filename
import numpy as np
import collections
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# 项目运行路径与行程码图片路径定义

colorDict= {"red": "红色", "red1": "红色", "orange": "橙色", "yellow": "黄色", "green": "绿色"}


def getColorList():
    """
    返回值: 专门的容器数据类型，提供Python通用内置容器、dict、list、set和tuple的替代品。
    """
    dict = collections.defaultdict(list)

    # 红色
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red'] = color_list

    # 红色2
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red2'] = color_list

    # 橙色
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list

    # 黄色
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list

    # 绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list

    return dict

def getTravelcodeColor(img_np):
  """
  返回值: 行程卡颜色{红、橙、绿}
  """
  hsv = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
  maxsum = -100
  color = None
  color_dict = getColorList()
  for d in color_dict:
    mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
    # cv2.imwrite(os.path.join(os.path.abspath(os.curdir),"img",d+'.jpg')  ,mask)
    binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
    binary = cv2.dilate(binary,None,iterations=2)
    cnts, hiera = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    sum = 0
    for c in cnts:
      sum+=cv2.contourArea(c)
    if sum > maxsum :
      maxsum = sum
      color = d

  return colorDict[color]


def information_filter(file_path,img_np,text_str):
  """
  返回值：有效信息组成的字典
  """
  # 健康码字段
  try:
    re_healthcode = re.compile('请收下(.{,2})行程卡')
    healthcode = re_healthcode.findall(text_str)[0]
  except Exception as _:
    healthcode = getTravelcodeColor(img_np)  # 文字无法识别时采用图片颜色识别
    print("[*] Get Photo Color = ",healthcode)

  # 电话字段
  re_phone = re.compile('[0-9]{3}\*{4}[0-9]{4}')
  if (re_phone.findall(text_str) == []):
      re_phone = re.compile("[0-9]{3}.{1,4}[0-9]{4}")
      result = re_phone.search(text_str)
      phone_str = result[0]
      # 先用星号填充满
      sub = 11 - len(phone_str)
      for i in range(0, sub):
          phone_str = phone_str[0:3] + "*" + phone_str[3:len(phone_str)]
      #再逐一从应该是星号的位置替换星号
      for i in range(0, 4):
          phone_str = phone_str[:i + 3] + "*" + phone_str[i + 4:]
  else:
      phone_str = re_phone.findall(text_str)[0]

  # 日期字段
  re_data = re.compile('2022\.[0-1][0-9]\.[0-3][0-9]')
  data_str = re_data.findall(text_str)[0]

  # 时间字段
  re_time = re.compile('[0-9][0-9]:[0-9][0-9]:[0-9][0-9]')
  time_str = re_time.findall(text_str)[0]

  # 地区城市字段
  citys_re = re.compile('到达或途经:(.+)结果包含')
  citys_str = citys_re.findall(text_str)[0].strip().split('(')[0]

  result_dic = {"status": "succ", "file": file_path ,"类型": healthcode, "电话": phone_str, "日期": data_str, "时间": time_str, "行程": citys_str}
  print("\033[032m",result_dic,"\033[0m")
  return result_dic

def getTravelcodeInfo(filename, img_np):
  """
  返回值：JSON字符串格式
  """
  # 灰度处理
  img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
  # 阈值二进制 - > 127 设置为255(白)，否则0(黑) -> 淡白得更白,淡黑更黑
  _,img_thresh = cv2.threshold(img_gray,180,255,cv2.THRESH_BINARY)
  # 图像 OCR 识别
  t1 = time.time()
  text = reader.readtext(img_thresh, detail=0, batch_size=10)
  result_dic = information_filter(filename, img_np, "".join(text))
  print(time.time() - t1)
  return result_dic


def OCR(fileName,gpuOn):
    global reader
    # img=cv2.imread("img/testnew.jpg")
    # print("应该排第二")
    img=cv2.imread(fileName)
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=gpuOn)
    print(gpuOn)
    result_dic_succ = getTravelcodeInfo(fileName, img)
    return result_dic_succ

if __name__ == '__main__':
    # OCR("../img/cq.jpeg")
    OCR("Z:\\Desktop\\测试集\\testnew.jpg")


