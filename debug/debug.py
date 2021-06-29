from appium import webdriver
import yaml
import multiprocessing

devices_list = ['TWGDU16513002866', 'e1a3da18']  # 两个设备

def desiredCaps(udid, port):
    with open('../conf/capability.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platforVersion'] = data['platforVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['noReset'] = data['noReset']
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port)+ '/wd/hub', desired_caps)

    return driver


desired_process = []  # 存储多设备

for i in range(len(devices_list)):
    port = 4723 + 2*i
    desired = multiprocessing.Process(target=desiredCaps, args=(devices_list[i], port))
    desired_process.append(desired)  # 将设备添加到里面，ip和端口


if __name__ == '__main__':
    for desired in desired_process:
        desired.start()

    for desired in desired_process:
        desired.join()