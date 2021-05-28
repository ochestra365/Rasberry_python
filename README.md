# Rasberry_python
Study Python
<br>
<img src="https://github.com/ochestra365/Rasberry_python/blob/main/PUTTY/Image%20for%20github/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%20%ED%8C%8C%EC%9D%B4%20%EC%97%B0%EA%B2%B0.jpg" width="100%" height="100%" ><br><br>
--------------
## 목차 <br>
1. 파이썬
2. 부품
3. PUTTY
4. VNC
5. NETWORK
6. RASBERRYPI
7. 기초 전자공학
8. 회로도(풀다운 풀업저항)
------------------
## 1. 파이썬(각 파일별 소스 연동시키기)
--------------
~~~
라즈베리 파이 구동은 파이썬으로 하는 것이 유리하다. 어차피 임베디드 시스템에 들어가라는 거라 경량이기 때문에 C로하면 무거워진다. 그리고 라즈베리파이 자동으로 깔려져 있고, 오픈 소스라서 좋다. 또한 인터프리터 언어라 컴파일 없이 바로 그 결과가 물리세계로 전달되는 것이 매력적이다.
매우 직관적이고, 가시성이 높은 매력적인 언어이다. 들여쓰기가 중요하다지만 본인의 논리가 충분하다면 헷갈리지 않는다.
~~~

~~~
계이름 주파수 출력 한글로 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    int do =262;
    int re=294;
    int me=349;
    int fa=392;
    int sol=440;
    int ra=494;
    int si=523;
    int dodo=587;
    int rere=659;
    int meme= 699;
    
    char ary[dummy data should be in];
    
    int size = sizeof(ary)/sizeof(ary[0]);
    
    for(int i=0;i<size;i++){
        
    switch(a[i]){
    case 'do' : 
        printf("'%d, '",do);
        break;
    case 're' : 
        printf("'%d, '",re);
        break;
    case 'me' :
         printf("'%d,'",me);
         break;
    case 'fa' :
       printf("'%d,', ",fa);
       break;
    case 'sol' :
         printf("'%d, '",sol);
         break;
    case 'ra' :
         printf("'%d, '",ra);
         break;
    case 'si' :
          printf("''%d, '",si);
          break;
    case 'dodo' :
         printf("'%d, '",dodo);
         break;
    case 'rere' :
         printf("'%d, '",rere);
         break;
     case 'rere' :
         printf("'%d, '",meme);
         break;
}
    }
    
	return 0;
}
~~~
## 2. 부품
------------
<img src="https://github.com/ochestra365/Rasberry_python/blob/main/PUTTY/Image%20for%20github/%EB%8B%A4%EC%9D%B4%EC%98%A4%EB%93%9C.jpg" width="30%" height="40%" ><br>
다이오드 : 전기가 일정한 방향으로 흐르게 한다.
<br>
<img src="https://github.com/ochestra365/Rasberry_python/blob/main/PUTTY/Image%20for%20github/%EC%8A%A4%EC%9C%84%EC%B9%98.jpg" width="30%" height="40%" ><br>
스위치 : 접지가 이뤄지게 된다.
<br>
<img src="https://github.com/ochestra365/Rasberry_python/blob/main/PUTTY/Image%20for%20github/%EC%8A%A4%ED%94%BC%EC%BB%A4.jpg" width="30%" height="40%" ><br>
스피커 : 진동의 폭을 다룬다.
<br>
<img src="https://github.com/ochestra365/Rasberry_python/blob/main/PUTTY/Image%20for%20github/%EC%A0%80%ED%95%AD.jpg" width="30%" height="40%" ><br>
저항 : 노드간 이어주거나 전압을 낮춰준다.
<br>
<img src="https://github.com/ochestra365/Rasberry_python/blob/main/PUTTY/Image%20for%20github/%EC%A0%90%ED%94%84%EC%84%A0.jpg" width="30%" height="40%" ><br>
점프선(암,수 구분) : 각 센서나 브래드보드와 결합하여 사용
<br>
<img src="https://github.com/ochestra365/Rasberry_python/blob/main/PUTTY/Image%20for%20github/%EC%B4%88%EC%9D%8C%ED%8C%8C%EC%84%BC%EC%84%9C.jpg" width="30%" height="40%" ><br>
초음파 센서 : 초음파를 날려 시간을 계산한다. 소리의 속도는 340m/s 따라서 이에 해당하는 수식을 적어주고 거리를 입력하면 쉘창에 결과가 출력된다.
<br>
## 3. PUTTY 리눅스

## 4. VNC
----------------
![Model](https://github.com/ochestra365/StudyAspNet21/tree/main/BasicMVCModel2/MyPortpolioWeb/Models "Model")<br>
## 5. NETWORK
----------------
## 6. RASBERRYPI
----------------
## 7. 기초 전자공학
-----------

## 8. 회로도
-----------
<img src="https://github.com/ochestra365/StudyAspNet21/blob/main/BasicMVCModel2/MyPortpolioWeb/Image_for_Git_hub/%EC%BB%A8%ED%83%9D.png" width="40%" height="30%" ><br>
