import yaml
with open("../../data/caps.yaml", 'r', encoding ="utf-8") as f:
    #这个是老方法会提示警告
    # data = yaml.load(f)
    #这个是新的，也可以用SafeLoader，会更加安全
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(type(data))  # 打印data类型
    print(data)  # 打印data返回值

print(data[0]['deviceDesc'])