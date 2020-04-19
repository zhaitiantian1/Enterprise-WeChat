import yaml

with open("/Users/zhaitiantian3/PycharmProjects/装饰器/testenter/data/contact.yaml", encoding="utf-8") as f:
    # 注意是list[]而不是list(),因为
    steps = yaml.safe_load(f)
    print(steps)

