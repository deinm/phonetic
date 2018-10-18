import hgtk
import math

def kortoeng(result):
    result2=[]
    index=0

    chosung_list = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    chosung_list_eng = ['g','kk','n','d','tt','r','m','b','pp','s','ss','','j','jj','ch','k','t','p','h']
    jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']
    jungsung_list_eng = ['a','ae','ya','yae','eo','e','yeo','ye','o','wa','wae','oe','yo','u','wo','we','wi','yu','eu','ui','i']
    jongsung_list = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    jongsung_list_eng = ['','k','k','k','n','n','n','t','l','l','l','l','l','l','l','l','m','p','p','t','t','ng','t','t','k','t','p','h']

    for i in result:
        if index%3==0: #초성
            if i in chosung_list:
                a = chosung_list.index(i)
                result2.append(chosung_list_eng[a])
            else:
                result.insert(index,"ㅇ")

        elif index%3==1: #중성
            if i in jungsung_list:
                a = jungsung_list.index(i)
                result2.append(jungsung_list_eng[a])
            else:
                result.insert(index,"")

        elif index%3==2: #종성
            #마지막이거나, 다음에 오는게 초성이거나
            if i in jongsung_list:
                if index==len(result)-1 or result[index+1] in chosung_list:
                    a = jongsung_list.index(i)
                    result2.append(jongsung_list_eng[a])
                else:
                    result.insert(index,"")
            else:
                result.insert(index,"")

        index+=1
        # print(index)
        # print(result)
        # print(result2)

    return result, result2

words = []
f = open("kor_to_read.txt", 'r')
lines = f.readlines()
for line in lines:
    words.append(line.rstrip())
f.close()

f = open("read_to_eng.txt",'w')
ans = []
final_phoans = []
final_combine = []

for i in words:
    i = list(i)
    pho_ans, read_eng = kortoeng(i)
    cnt = 0
    word_len = len(pho_ans)
    combine_words = []

    if word_len>3:
        for j in range(math.ceil(word_len/3)):
            try:
                combine_words.append(hgtk.letter.compose(pho_ans[3*j+0],pho_ans[3*j+1],pho_ans[3*j+2]))
            except :
                combine_words.append(hgtk.letter.compose(pho_ans[3*j+0],pho_ans[3*j+1]))
    else :
        combine_words.append(hgtk.letter.compose(pho_ans[0],pho_ans[1]))

    final_combine.append(''.join(combine_words))

    pho_ans = "".join(pho_ans)
    read_eng = "".join(read_eng)

    final_phoans.append("".join(pho_ans))
    ans.append("".join(read_eng))

print(final_combine)

final_ans = '\n'.join(ans)
f.write(final_ans)
f.close()


f = open("phonetic_ans.txt","w")
final_phoans = '\n'.join(final_phoans)
f.write(final_phoans)
f.close()

f = open("phonetic_ans_combine.txt","w")
final_phoans = '\n'.join(final_combine)
f.write(final_phoans)
f.close()
