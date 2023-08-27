# import re
#
# text_str="通信行程卡提供服务>通信行程卡通信大缴据行程卡疫情防控,人人有责请收下绿色行程卡133+**6811的动态行程卡更新于:  2022.05.2410:08:32您于前14夭内到达或途经:  河北省唐山市* (注: *表示当前该城市存在中风险或高风险地区,并不表示用户实际到访过这些中高风险地区。)结果包含您在前14天内到访的国家(地区〉与停留4小小时以上的国内城市色卡仅对到访地作提醒。不关联健康状况太眠名旺^埠证通查来了!全国移动电话卡\"一证通查立即点击进入防范诈骗,保护你我"
# re_phone = re.compile('[0-9]{3}\*{4}[0-9]{4}')
# if (re_phone.findall(text_str) == []):
#     re_phone = re.compile("[0-9]{3}.{1,4}[0-9]{4}")
#     result = re_phone.search(text_str)
#     phone_str = result[0]
#     sub=11-len(phone_str)
#     for i in range(0,sub):
#         phone_str=phone_str[0:3]+"*"+phone_str[3:len(phone_str)]
#     for i in range(0,4):
#         phone_str=phone_str[:i+3]+"*"+phone_str[i+4:]
# else:
#     phone_str = re_phone.findall(text_str)[0]


import sys, os
import PySide6

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
print(plugin_path)