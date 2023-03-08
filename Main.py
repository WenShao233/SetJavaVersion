import os
import time
import json

print("欢迎使用Java切换器! 若有疑问, 可在任意可输入的地方输入help获得帮助文档")

t1 = 0 
JavaVersionList = []
JavaList = {}

for i in range(1, 21):
    if os.environ.get(f"JAVA{i}_HOME") != None:
        JavaVersionList.append(i)
    else:
        t1 += 1
if t1 == 20:
    n1 = input("请问你要添加多少个Java: ")
    for j in range(n1):
        JavaVersion = input(f"请输入第{j + 1}个Java版本号(Java8就写8, Java17就写17): ")
        VersionPath = input(f"请输入第{j + 1}个Java目录: ")
        os.system(f"setx \"JAVA{JavaVersion}_HOME\" \"{VersionPath}\"")

try:
    if os.environ.get("JAVA_HOME") != None:
        JAVA_HOME = os.environ.get("JAVA_HOME")
except:
    pass
finally:
    t1 = 0
    for y in JavaVersionList:
        if os.environ.get(f"JAVA{y}_HOME") == JAVA_HOME:
            print(f"当前Java为{y}, 位于{JAVA_HOME}")
            continue
        else:
            t1 += 1
    if t1 == len(JavaVersionList):
        print("当前JAVA变量不正常, 请立即更换!")

version = input("请输入要切换的Java版本: ")
if version == "help":
    print(
        """
帮助文档
常用指令:
1. help
打开帮助文档
2. add
打开 [添加新的Java] 面板
3. remove
打开 [移除一个Java] 面板
4. reset
移除所有该程序修改过的系统变量(不包括JAVA_HOME)
        """
        )

if os.environ.get(f"JAVA{version}_HOME") == None:
    print("当前没有该Java, 若您已安装该Java, 请输入help查看帮助文档")
else:
    os.system(f"setx \"JAVA_HOME\" \"%JAVA{version}_HOME%\"")

time.sleep(2)
