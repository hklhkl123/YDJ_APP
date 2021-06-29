from appium import webdriver
import yaml

def init_driver(device):

    with open("../data/caps.yaml", 'r', encoding="utf-8") as f:
        # 这个是新的，也可以用SafeLoader，会更加安全
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(type(data))  # 打印data类型
        print(data)  # 打印data返回值
        for i in data:
            if i['deviceDesc'] == device:
                indexnum = data.index(i)
                severurl = 'http://{0}:{1}/wd/hub'.format(data[indexnum]['server_ip'],data[indexnum]['server_port'])
        print(severurl)
        print(data[indexnum]['desired_caps'])

    driver = webdriver.Remote(severurl, data[indexnum]['desired_caps'])
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', data[0]['desired_caps'])
    return driver


# init_driver('Moto')