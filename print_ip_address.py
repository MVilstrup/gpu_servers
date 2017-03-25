import os
import re
def get_ip():
    return re.search(re.compile(r'(?<=inet )(.*)(?=-->)', re.M), os.popen('ifconfig |grep inet').read()).groups()[0]

print(get_ip())
