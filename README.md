# Phonetic
Phonetic is a second education content of DodamDodam.
As DodamDodam is an Korean learning application for foreigners,
this phonetic content was designed to make foreigners apply their experience of learning any language(especially mother language) to learning Korean.

Korean has special characteristic - we can write Korean as it sounds.
This means that Korean is a phonetic language.

In this curriculum, the learner have to solve some phonetic problems.
The words of their mother tounge will be given, and they should do dictation in Korean,
which means they should find the right Korean word that sounds like mother tounge word when we read them.

The goal of this content is understanding Korean's special characteristic, phonetic,
and develop one's ability to read Korean words.

Currently, DodamDodam has contents only for English users, but we are planning to support Japanese, Chinese, and any other foriegn languages in the future.

To convert English words in Korean, we need to do the followings :

<img width="1008" alt="2018-11-19 11 26 33" src="https://user-images.githubusercontent.com/41565118/48713010-a4bb1e80-ec52-11e8-925d-b289f6f70d1f.png">

1. Secure English vocabulary data.
2. Convert English word to Korean as it sounds.
3. Convert Korean word to pronunciation symbol.
4. Convert pronunciation symbol to English word.

These procedure is needed because Korean word could written different in English due to phonological variation.
If the English word from #4 is same as the English word in #1,
we decide that the word can be used in phonetic learning becasue it has the same result when we convert English word to Korean and Korean word to English according to Korean grammer.

## Usage
1. conversion_engtokor.py

* input : English words(list)

* output : `eng_to_kor.txt` 

`eng_to_kor.txt` : Convert English word to Korean as it sounds Ex) person -> 퍼슨



2. g2p.py

* input : `eng_to_kor.txt`

* output : `kor_to_read.txt`

`kor_to_read.txt` : Convert Korean word to pronunciation symbol, and divide by consonant vowel unit. Phonological variation appears after this step. Ex) 앱소브 -> ㅐㅂㅆㅗㅂㅡ



3. convertion_eng.py

* input : `kor_to_read.txt`

* output : `read_to_eng.txt`, `phonetic_ans.txt`, `phonetic_ans_combine.txt`

`read_to_eng.txt` : Convert the consonant vowel unit seperated korean words in `kor_to_read.txt` to English word. Ex) 말레이시아 -> malreisia

`phonetic_ans.txt` : Divide Korean words without phonological variation by consonant vowel unit. Ex) 말레이시아 -> ㅁㅏㄹㄹㅔㅇㅣ시ㅇㅏ

`phonetic_ans_combine.txt` : Combine the seperated voewls in `phonetic_ans.txt`. Ex) ㅁㅏㄹㄹㅔㅇㅣㅅㅣㅇㅏ -> 말레이시아


4. word_compare.py

* input : `word_list.txt`, `read_to_eng.txt`

* output : `phonetic_words.txt`

`word_list.txt` : English words without any process of transformation. Ex) Shanghai, Penang, Malaysia, ...

`phonetic_words.txt` : The result of comparing 'pure' words in `word_list.txt` and result words in `read_to_eng.txt`. We just use the words that has same results in phonetic learning. Ex) ring, hotel, oil


5. pho_qgenerater.py

* input : `word_list.txt`, `phonetic_words.txt`, `phonetic_ans.txt`, `phonetic_ans_combine.txt`

* output : question generate

The questions are consist of 4 wrong answers and 1 right answer.

`word_list.csv` : Final phonetic word lists used in DodamDodam.


## Sample
You can find 7 files that have similar names.(eng_to_kor * 7, kor_to_read * 7, phonetic_ans * 7, ...)
Ans each of them has (Nothing), _3000, _conv, _ebs, _ele, _fru, _wiki after the file name.

(Nothing) : Cities and Countries

_3000 : Essesntial English word 3000

_conv : Essential words for converstaion

_ebs : Essesntial words from ebs

_ele : Essesntial words for elementary school students

_fru : Fruit

_wiki : Foreign language words from wiki

After Securing the word data, we go through the process aboce(1~5) and finally get the phonetic words that we can use.
