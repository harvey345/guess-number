import random
rnum=random.randint(1,100)
for i in range(1,21):
    anum=int(input("請輸入一個數字："))
    if anum==rnum:
        print("恭喜你達對了！！！")
        break
    else:
        if i<20:
            print("在試一次")
            continue
        elif i==20:
            print("下次在努力一點\n")
            break

        
            