import random

for i in range(5):
    
    print(f'{i+1}. helloworld')
    print('짜장이냐 짬뽕이냐')
    a = input('먹고 싶은거 입력 : ') 
    print(f'입력한 값 : {a}')

    menu = '짜장', '짬뽕', 
    if a == 'a' or a == 'b':
        print('나오나?  True') 
        m = random.choice(menu)
        print('인공지능의 추천')
        print(f'{m} 먹어')
        
    else:
        print('짬짜면')