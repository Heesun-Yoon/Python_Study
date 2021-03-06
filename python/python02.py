# Python02.py

"""

    a. 정수형 
        a = 123
        a = -178 
        a = 0

    b. 실수형
        a = 1.2
        a = -3.45
        a = 4.24e10
        a = 4.24e-10

    c. 8진수, 16진수
        a = 0o177
        a = 0x8ff

    d. 복소수
        * python에서는 i 대신 j사용 (대소문자 상관X) 
        a = 1+2j
        b = 3-4j

        *복소수 관련 내장 함수
        복소수.real (실수 부분 리턴)
            a = 1+2j
            a.real
            1.0

        복소수.imag (허수 부분 리턴)
            a = 1+2j
            a.imag
            2.0

        복소수.conjugate() (켤레복소수 리턴)
            a = 1+2j
            a = confugate()
            (1-2j)

        abs(복소수) (복소수의 절댓값 리턴)
            a = 1+2j
            abs(a)
            2.2360679774997898

        
    e. 연산자
        제곱 연산자
        a ** b

        나머지 연산자
        a % b

        몫 연산자
        a / b

        소수점 아랫자리 버림 
        a // b

        
    f. 문자열
        "Hello"
        'Hello'
        큰따옴표 양쪽에 3개 가능.
        '''Hello'''

    
    g. 문자열 연산
        더해서 연결
            head = "python"
            tail = "is fun!"
            head + tail 
            'Python is fun!'

        문자열 곱하기
            a = "python"
            a * 2
            'pythonpython'

    
    h. 문자열 인덱싱과 슬라이싱
        인덱싱?
            a = "Life is too short, You need Python"
            a[3]
            e
            a[-1] -> 뒤에서 첫번째 글자, a[-0] 과 결과 같음.
            n

        슬라이싱?
            a = "Life is too short, You need Python"
            b = a[0] + a[1] + a[2] + a[3]
                or
            b = a[0:4] -> 끝번호는 포함되지 않음.
            b
            'Life'

            * 끝번호 생략 > 시작번호 부터 끝까지 추출
            * 시작번호 생략 > 처음부터 끝번호 까지 추출
            * 시작번호,끝번호 생략 > 처음부터 끝까지 추출 


    i. 문자열 관련 함수
        문자 개수 세기
            a = "hobby"
            a.count('b')
            2

        위치 알려주기(find)
            a = "Python is best choice"
            a.find('b')
            10 (문자열에서 b가 처음나온 위치)
            a.find('k')
            -1 (존재하지 않으면 -1 반환)

        위치 알려주기(index)
            a = "Life is too short"
            a.index('t')
            8
            a.index('k')
            error   -> find는 존재하지 않는 문자 찾으면 -1 반환, index는 error

    
    j. 문자열 삽입
        a = ","
        a.join('abcd')
        'a,b,c,d'

    k. 공백 지우기
        lstrip
        rstrip
        strip

    
    L. 문자열 나누기
        a = "Life is too short"
        a.split()
        ['Life','is','too','short']



    

"""

# ex1)
a = 3
b = 4
c = a/b
print(c)


# ex2)
test = """
    hello
    hi
    thank u
    """

print(test)


# ex3)
print("study python %d" %3)
print("study %s" %"python")
word = "python"
print("study %s" %word)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" %(number, day))


# ex4)
print("%10s" %"hello")
print("%-10sHi" %"hello")

# 소수점 네 번째 자리까지만 표기
print("%0.4f" %1.23456789)
# 총 10자리수, 소수점 네 번째 자리까지만 표기
print("%10.4f" %1.23456789)


# ex5)
print("I eat {0} apples.".format(3))
print("I eat 3 {0}.".format("apples"))
print("I eat {0} {1}.".format(3,"apples"))

# 문자열 왼쪽 정렬 + 10자리수
print("{0:<10}".format("hi"))

# 문자열 오른쪽 정렬 + 10자리수
print("{0:>10}".format("hi"))

# 문자열 가운데 정렬 + 10자리수
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:=<10}".format("hi"))
print("{0:=>10}".format("hi"))

