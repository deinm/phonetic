# Phonetic
Phonetic is a second education content of DodamDodam.
Phonetic은 도담도담의 두 번째 학습 기능입니다.
외국인들을 위한 한국어 교육인 만큼, 제 1의 언어인 모국어를 학습했던 경험을 살려 한국어를 학습할 수 있도록 기획된 컨텐츠입니다.

한글은 다른 언어와는 달리 뜻이 있기 때문에 그렇게 쓰는 것이 아니라, 그렇게 소리 나기 때문에 그렇게 표기하는 것이라는
표음 언어라는 특성을 가집니다.
본 커리큘럼에서는 주어진 모국어 단어를 보고, 이를 한글로 적절하게 표기한 정답을 고르는 문제 풀이 방식으로 한글을 학습하게 됩니다.
학습의 목표는 한국어의 표음이라는 특성을 이해하고, 한국어 단어를 읽을 수 있는 능력을 기르는 것입니다.

본 코드는 문제 생성 및 문제 생성을 위한 단어 데이터 수집을 위한 코드이며,
현재 도담도담은 영어권 사용자들을 위한 컨텐츠로 구성되어 있으며 차후 일본어, 중국어 등을 지원할 계획입니다.

영단어를 한글로 표기하기 위해서는 영단어 데이터 확보 이후 다음과 같은 과정이 필요합니다.

<img width="1008" alt="2018-11-19 11 26 33" src="https://user-images.githubusercontent.com/41565118/48713010-a4bb1e80-ec52-11e8-925d-b289f6f70d1f.png">

1. 영단어를 한국어 표기로 변경합니다.
2. 한국어 표기로 변경된 단어를 발음기호로 변경합니다.
3. 발음기호로 변경된 한국어를 영어로 변경합니다.

1~3의 과정을 거쳐 최종적으로 나온 영단어가 초기의 영단어와 동일하다면, 
우리나라 문법상으로 영어를 한국어로 표기하거나 한국어를 영어로 표기하였을 때 같은 결과가 나온다고 판단하여
표음 학습에 출제할 수 있는 단어로 분류하게 됩니다.

## Usage
1. conversion_engtokor.py

-input : 영단어(list)

-output : `eng_to_kor.txt` 

eng_to_kor : 영단어를 한글 발음으로 바꿈. Ex) person -> 퍼슨

2. g2p.py

-input : `eng_to_kor.txt`

-output : `kor_to_read.txt`

`kor_to_read.txt` : 한글을 [발음기호] 자음 모음 단위로 분할함. 즉, 음운의 변동 고려. Ex) 앱소브 -> ㅐㅂㅆㅗㅂㅡ

3. convertion_eng.py

-input : `kor_to_read.txt`

-output : `read_to_eng.txt`, `phonetic_ans.txt`, `phonetic_ans_combine.txt`

`read_to_eng.txt` : `kor_to_read.txt`에서 한글 [발음기호]로 변환했던 내용을 다시 영어로 변환 Ex) 말레이시아 -> malreisia
`phonetic_ans.txt` : 영단어->한글(음운변동 X)을 자음 모음 단위로 분할 Ex) 말레이시아 -> ㅁㅏㄹㄹㅔㅇㅣ시ㅇㅏ
`phonetic_ans_combine.txt` : `phonetic_ans.txt`의 분리된 자음 모음을 결합 Ex) ㅁㅏㄹㄹㅔㅇㅣㅅㅣㅇㅏ -> 말레이시아

4. word_compare.py

-input : `word_list.txt`, `read_to_eng.txt`

-output : `phonetic_words.txt`

`word_list.txt` : 변환의 과정을 하나도 거치지않은 순수한 초기 단어 목록들. Ex) Shanghai, Penang, Malaysia, ...
`phonetic_words.txt` : 순수한 단어들(`word_list.txt`)와 영->한->영을 거친 단어들(`read_to_eng.txt`)를 비교해서 동일한 결과가 나온 단어들만 따로 모음. 실제 표음 학습 문제 출제에 사용할 것임. Ex) ring, hotel, oil

5. pho_qgenerater.py

-input : `word_list.txt`, `phonetic_words.txt`, `phonetic_ans.txt`, `phonetic_ans_combine.txt`

-output : 문제 출력

오답지 4개+정답지 1개 총 5지선다로 구성된 문제 출제


word_list.csv : 최종 표음 학습 단어 목록
+ question_generater : ㄱㄴㄷㄹ 자음모음 학습 문제 출제


## Sample
txt 파일이 굉장히 많은데 자세히 보면
비슷한 이름의 파일들이 7개(eng_to_kor 7개, kor_to_read 7개, phonetic_ans 7개, ...)씩 있음
그리고 뒤에 (아무것도 안달림), _3000, _conv, _ebs, _ele, _fru, _wiki등이 붙어 있음

(아무것도 안달림) : 지명
_3000 : 필수 영단어 3000
_conv : 회화 필수 영단어
_ebs : ebs필수 영단어
_ele : 초등 필수 영단어
_fru : 각종 과일 이름
_wiki : 위키백과에 있는 각종 외래어들

이런 영어단어를 바탕으로 돌린 결과값들.
단어 데이터를 많이 확보하기 위한 노력..이랄까..

단어 데이터를 확보하면 다음과 같은 순서로 코드를 돌림
