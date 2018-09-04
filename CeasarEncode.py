# 凯撒密码（加密部分）
# 每一个英文字符循环替换为字母表序列该字符后面第三个字符
etxt = input("请输入加密后文本: ")
for p in etxt:
    if "a" <= p <= "z":
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26), end='')
    elif "A" <= p <= "Z":
            print(chr(ord("A")+(ord(p)-ord("A")+3)%26), end='')
    else:
            print(p, end='')