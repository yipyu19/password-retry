import random
start = input('請輸入範圍開始的數字：')
end = input('請輸入範圍結束的數字：')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    guess = input('請輸入你所猜的數字：')
    guess = int(guess)
    count = count + 1
    if guess == r:
        print('你猜對了恭喜')
        print('這是你猜的第',count,'次！')
        break
    elif guess > r:
        print('比答案小！請重新輸入')
    elif guess < r:
        print('比答案大！請重新輸入')
    print('這是你猜的第',count,'次！')