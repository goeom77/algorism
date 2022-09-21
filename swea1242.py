# 2번째 : 자리수가 바뀐 것의 개수를 카운트해서 바뀌는 순간 그 리스트의 개수를 56으로 나누고 안 나눠떨어지면 +1 을 더하는 방식으로 배수 확인
# -> 2번째 방법은 제일 앞의 0의 자리수가 최대 105개 여서 배수를 1개 잘못 나오는 경우의 수가 발생한다.(x)
# 3번째 : 16진수로 배수를 최대 15개로 맞춰 그 위에 숫자가 00이 아니라면 배수를 증가시킨다.
# -> 00이 나오더라도 배수로 처리 되는 경우의 수가 있다.(x)
import sys
sys.stdin = open('swea1242.txt')

# 2진수로 나타내서 뒤의 pattern을 통해 마지막의 수가 pattern에 있을 때의 배수를 확인한다.
# 주의점 : pattern의 숫자가 우연히 맞을수 있으니깐 배수라인에 있는 숫자와 같은지 비교한다.
# 암호중에서 pattern에 안맞는 암호가 존재할수 있지 않을까?

pattern = {
    '0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9
}
pattern_lst = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
bi = {
    '0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111',
    '8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'
}

def find_num(idx):                                   # 2진수로 구성된 암호를 불러와서 그 행에 배수를 계산해 올바른 형식의 암호는 result리스트에 넣는다. 
    sentence = idx                                   # 이 sentence에는 몇개의 암호가 들어있는지 알수 없다. -> 남은 문장들은 다시 확인해봐야 할것이다.
    cnt = 1                                          # 몇배수인가를 결정하는 변수
    while True:                                      # 배수가 결정날때까지 계속 확인
        ck = True                                    # 7개 숫자가 모두 나왔는가?
        if cnt >36:                                  # 최대 개수가 35배수이므로
            return                                   # 여긴 답이 나올수 없다. -> 암호 중에 pattern에 맞지 않은 암호인 경우 해결
        compare = ''                                 # 비교군 생성
        for i in range(-6*cnt-1,0,cnt):              # -7,-6,-5,-4,-3,-2,-1(1배수) -13 -11 -9 -7 -5 -3 -1(2배수) -> 뒤에 7개로 숫자가 만들어 지는지 확인해서 배수를 확인
            if cnt == 1:
                compare += sentence[i]               # 1일때는 비교대상이 없으니깐 암호 생성
            else:
                if sentence[i] == sentence[i-1]:     # 가장 마지막 배열을 확인하는데 그 앞에와 숫자가 같은 경우에
                    compare += sentence[i]           # 해당 암호를 비교한다.
                else:
                    ck = False
                    break                            # 조금이라도 속도를 빠르게 하기 위해서 조건 추가
        if ck and compare in pattern_lst:            # 똑같은 pattern이 나올때 까지 배수를 늘린다. key_error 방지
            sentence_l = len(sentence)
            result_value = sentence[sentence_l-cnt*56:]
            result.append(result_value)
            rest = sentence[:sentence_l-cnt*56]      # 문자열 깊은 복사
            rest = rest.rstrip('0')                  # 남은 문자열중 rstrip한 것을 bi_arr에 추가
            if rest:                                 # rstrip하고 남은것이 빈문자열이 아니면
                bi_arr.append(rest.rstrip('0'))      # bi_arr에 추가해서 계속 더할수 있게 만든다.
            return
        else:
            cnt += 1                                 # 배수를 추가한다.(1~35)

def safe(a): # a는 문자열
    tmp = len(a)//56                                 # 배수 찾기(글자 크기는 항상 56의배수 이니깐)
                                                     # 검증 방법 : 홀수자리합*3 + 짝수자리합 + 검증코드 : 10의 배수
                                                     # 0,1,2,3,4,5,6,7-> (0+2+4)*3+1+3+5+7
    even = 0
    odd = 0
    order = 0                                        # 자리순서가 몇번째인지 결정
    for i in range(0,tmp*56,tmp*7):                  # 0부터 배수*56까지 배수*7 간격으로 tmp패턴을 만든다.
        tmp_pattern = ''
        for j in range(0,tmp*7,tmp):                 # 0부터 배수*7까지 배수 간격으로 tmp패턴 제작
            tmp_pattern += a[i+j]
        v = pattern[tmp_pattern]                     # 숫자한개의 패턴 완성 -> int값으로 나온다.
        if order % 2:                                # 홀수이면
            odd += v
        else:                                        # 짝수이면
            even += v
        order+=1                                     # 자리수 +1
    if (even*3+odd) % 10 == 0:                       # 검증에 통과하면
        return odd + even                            # 홀수와 짝수의 합을 반환
    else:
        return 0                                     # 검증 불합격시 0 반환

# 테스트 케이스
T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    # 서로 겹치지 않는 행만 뽑아서 추출
    arr = []
    arr = list(set([input().rstrip('0') for _ in range(n)]))
    bi_arr = []                                      # 2진수로 바꾼 arr
                                                     # arr로 배수만큼 비교한다음 없앤 것에서 strip('0')하고 다시 비교하는 방법
    result = []                                      # set으로 중복된것을 없앤다음 합으로 계산하자.
    for i in range(len(arr)):
        if arr[i]:
            bi_data = ''
            for j in list(arr[i]):
                bi_data += bi[j]                                                                   # 00000000000000000000000000000000000111011011000101110110110001011000100011010010011011101100(원래)
            bi_arr.append(bi_data.rstrip('0'))      # 2진수 안에 있는 오른쪽 0을 모두 제거하기        # 000000000000000000000000000000000001110110110001011101101100010110001000110100100110111011(rstrip)
                                                    # 배수를 알기위해서 7자리씩 끊어서 확인해야하는데 뒤에 있는 7개씩만 확인하면 배수를 알수 있다.
                                                    # 0111011 를 뽑아 왔을 때 이것이 pattern_lst에 있으면 배수는 1
                                                    # 없으면 1자리씩 띄워서 뽑아왔을 때 이것이 pattern_lst에 있으면 배수는
    
    for i in range(len(bi_arr)):
        find_num(bi_arr[i])
    value = 0
    result = list(set(result))
    for j in range(len(result)):
                                                    # 마지막으로 검증코드를 확인해야한다.
        value += safe(result[j])
    print(f'#{t} {value}')