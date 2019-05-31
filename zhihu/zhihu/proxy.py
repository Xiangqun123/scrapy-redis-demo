import requests
import re

pre_PROXIES = requests.get("http://192.168.1.104:8080/get_all").text
x = proxies_list = re.findall("\"(.*?)\",", pre_PROXIES, re.S)



