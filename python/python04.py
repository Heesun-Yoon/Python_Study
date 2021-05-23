# Python04.py

"""

    튜플
        > 리스트는 [] 으로 둘러싸지만, 튜플은 ()으로 둘러싼다. 
        > 리스트는 그 값의 생성,삭제,수정이 가능하지만 튜플은 값을 바꿀 수 없다.
        > 프로그램 실행되는 동안 값이 항상 변하지 않기를 바라는 경우 튜플 사용. 
        > 1개의 요소만을 가질 경우 요소뒤에 , 반드시 붙여야 함.
        
        인덱싱
            t1 = (1,2,'a','b')
            t1[0]
            1

        슬라이싱
            t1 = (1,2,'a','b')
            t1[1:]
            (2,'a','b')

        더하기
            t2 = (3,4)
            t1 + t2 // (1,2,'a','b') + (3,4)
            (1,2,'a','b',3,4)

        곱하기
            t2 * 3
            (3,4,3,4,3,4)

        
    
    딕서녀리 자료형
        : 대응관계를 나타내는 자료형 (hash와 비슷)
        : 순차적으로 해당 요소값을 구하지 않고(순서를 따지지 않음) Key를 통해 Value를 얻음. 
        {Key1:Value1, Key2:Value2, Key3:Value3}
        
        dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
        a = {1: 'hi'}
        a = {'a':[1,2,3]} > Value에 리스트도 넣을 수 있음

        쌍 추가
            a = {1: 'a'}
            a[2] = 'b'          > {2:'b'} 추가
            a
            {2:'b',1:'a'}

            a['name'] = 'pey'   > {'name':'pey'} 추가
            
            a[3] = [1,2,3]      > {3:[1,2,3]} 추가
            {'name':'pey',3:[1,2,3],2:'b',1:'a'}

        
        쌍 삭제
            del a[1]
            a
            {'name': 'pey', 3:[1,2,3],2:'b'}
        


"""