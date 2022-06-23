import random

print('hello world')
print('한글')
print('짜장이냐 짬뽕이냐')
#만약에 짜장과 짬뽕 둘중에 하나 추천
#내가 짜장이나 짬뽕을 적으면 짜장이나 짬뽕중에 추천
#아니면 둘다(짬짜면)
a = input('먹고 싶은거 입력 : ') 
# print('입력한 값 : ',a)
# print('입력한 값 : %s'%a)
# print('입력한 값 : {}'.format(a))
print(f'입력한 값 : {a}')

menu = '짜장', '짬뽕', 
if a == '짜장' or a == '짬뽕':
    print('나오나?  True') #참일때만 여기 출력
    #여기에서 짜장or짬뽕중에 인공지능이 추천 해주는 결과
    m = random.choice(menu)
    print('인공지능의 추천')
    print(f'{m} 먹어')
    
else:
    print('짬짜면')
 




