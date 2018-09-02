#猜数字游戏（1到1000）
#author:CUMTB_LDF
import random
target = random.randint(1,1000)
count = 0
while True:
    try:
        guess = eval(input("请输入一个猜测的整数（1-1000)"))
    except:
        print("输入的数字错误，请重试，不计入猜测次数")
        continue
    count += 1
    if guess == target:
        print("恭喜你，猜对了！")
        print("猜测的次数为{}".format(count))
    elif guess > target:
        print("你猜的数大了")
    else :
        print("你猜的数小了")


