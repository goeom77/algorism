# 거짓말
# 진실을 아는사람 주어진다.
# 각 파티에 오는 사람들의 번호가 주어진다.
# 거짓말 쟁이가 아니면서 거짓말 할수 있는 파티 개수의 최댓값 구하시오

# 거짓말 했는데 진실말해야하면 그것도 거짓말 쟁이가된다.
# 사람수n 파티수 m
n, m = map(int, input().split())
# 진실아는 사람수와 번호 0~50
tr, *tr_num = map(int, input().split())
# 진실아는 사람이 party_num에 있으면 진실말해야하는 사람이 늘어나는 것!
tru_list = [0]*51
for i in range(tr):
    tru_list[tr_num[i]] = 1
all_party = []
for i in range(m): # 1~50
    party, *party_num = map(int, input().split())
    for j in party_num:
        if tru_list[j] == 1:
            for j in party_num:
                tru_list[j] = 1
            break
        # 한개라도 밑에 숫자가 있으면 그 숫자의 묶음은 전부 tru_list에 넣고 전부 비교해야된다.
    all_party.append(party_num)
