import random
r = random.randint(1, 100)
while True:
    guess = input('請輸入你所猜的數字：')
    guess = int(guess)
    if guess == r:
        print('你猜對了恭喜')
        break
    elif guess > r:
        print('比答案小！請重新輸入')
    elif guess < r:
        print('比答案大！請重新輸入')