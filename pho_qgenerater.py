def phonetic_generater(level, q_num):
    #from flask import jsonify
    import csv
    import random
    import hgtk

    f = open('word_list.csv', 'r', encoding='utf-8')
    line = csv.reader(f)
    word_data = []
    quest_data = []
    err_data = []

    #영어 단어
    ask_data = []

    #정답 string(한글)
    ans_data = []

    #정답지 번호, 0번 1번 2번 3번
    ans_num_data = []

    for data in line:
        word_data.append(data)
    del word_data[0]

    #전체 단어 목록
    #print(word_data)
    f.close()

    #n문제 출제
    while len(quest_data) != q_num:
        order = random.randint(0,len(word_data)-1)
        #print(order)
        if int(word_data[order][3])==level:
            quest_data.append(word_data[order])

    print(quest_data)

    ja_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    mo_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    #오답지 생성
    for i in quest_data:
        save=[]
        #단어 저장
        cpy = list(i[2])
        ans_data.append(i[1])
        ask_data.append(i[0])

        #오답지 3개
        while len(save)<3:
            #자음/모음 변경한 값 저장할 변수
            tmp = cpy[:]

            #change번째 자음 모음을 변경할 예정
            change = random.randint(0,len(cpy)-1)
            sampling = random.randint(0,len(ja_list)-1)
            if tmp[change] in ja_list:
                if tmp[change] != ja_list[sampling]:
                    tmp[change] = ja_list[sampling]
                else:
                    continue
            elif tmp[change] in mo_list:
                if tmp[change] != mo_list[sampling]:
                    tmp[change] = mo_list[sampling]
                else:
                    continue

            if tmp not in save and tmp!=cpy:
                save.append(tmp[:])

            if len(save)==3:
                #save = [오답, 오답, 오답, 정답]
                save.append(cpy)
                #print("save:",save)
                err_data.append(save[:])

    err_cpy = err_data[:]
    combine=[]
    for i in range(0,len(err_cpy)):
        #정답 섞기
        random.shuffle(err_cpy[i])
        word_len = len(err_cpy[i])

        #답지가 4개로 구성
        for j in range(0,4):
            one_combine = []

            #단어를 결합하고 list에서 제거하므로 0보다 클 때만 돌아감
            while len(err_cpy[i][j])>0:
                cnt = len(err_cpy[i][j])
                #한 글자 단어 따로 처리
                if cnt==2:
                    one_combine.append(hgtk.letter.compose(err_cpy[i][j][0],err_cpy[i][j][1]))
                    err_cpy[i][j] = []
                elif cnt==3:
                    one_combine.append(hgtk.letter.compose(err_cpy[i][j][0],err_cpy[i][j][1],err_cpy[i][j][2]))
                    err_cpy[i][j] = []
                #두 글자 이상의 단어 처리
                else:
                    if err_cpy[i][j][3] in ja_list:
                        one_combine.append(hgtk.letter.compose(err_cpy[i][j][0],err_cpy[i][j][1],err_cpy[i][j][2]))
                        err_cpy[i][j] = err_cpy[i][j][3:]
                    elif err_cpy[i][j][3] in mo_list:
                        one_combine.append(hgtk.letter.compose(err_cpy[i][j][0],err_cpy[i][j][1]))
                        err_cpy[i][j] = err_cpy[i][j][2:]
                if len(err_cpy[i][j])==0:
                    combine.append(''.join(one_combine))
                    break

    print(combine)
    combine_by_q = []
    for i in range(0,10):
        combine_by_q.append(combine[4*i:4*(i+1)])

    for i in range(0,10):
        ans_num_data.append(combine_by_q[i].index(ans_data[i]))

    return ask_data, ans_data, ans_num_data, combine_by_q
    #return jsonify(data~)

# ask, ans, ans_num, combine = phonetic_generater(1,10)
# for i in range(0,10):
#     print(i+1,"번 문제입니다.")
#     print(ask[i])
#     print(combine[i])
#     ans = int(input("답을 입력해 주세요."))
#     if ans==ans_num[i]+1:
#         print("정답입니다!")
#     else:
#         print("틀렸습니다! 답은",ans_num[i]+1,"입니다.")
