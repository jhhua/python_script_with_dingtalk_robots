#coding:utf-8  
import requests,json   
from datetime import timedelta,datetime, date, time, timezone
headers={
     'Content-Type': 'application/json'} 
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=' 
mobile = '1008611'
time = datetime.now()
tm = str(time)
data = {
     
    "msgtype": "text",
    "text": {
     "content": '!!!!!!nbimportant message\r\n' + 'success:'  +  "@" + mobile + '（!!）：\n' + tm +'\ncurrent time' + '            '},
    "at": {
     "atMobiles": "['"+ mobile + "']","isAtAll": False}
}
requests.post(webhook, data=json.dumps(data), headers=headers)
