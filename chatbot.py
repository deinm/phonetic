import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"

    # Define a function that sends a message to the bot: send_message
    # def send_message(message):
        # Print user_template including the user_message
        #print(user_template.format(message))
        # Get the bot's response to the message
        #response = respond(message)
        # Print the bot template including the bot's response.
        #print(bot_template.format(response))

    # Send a message to the bot
    # send_message("hello")

# Define variables
food = "라면"
drink = "콜라"
country = "독일"
hobby = "독서"

# Define a dictionary containing a list of responses for each message
responses = {
    "다듬":[
        "네, 알겠습니다. 염색은 시간이 조금 걸릴 수 있어요.",
        "네. 아, 그리고 염색은 시간이 조금 걸리는데 괜찮으신가요?"
    ],
    "팔아요?": [
      "{0}빼고 다 팔아요.".format(food),
      "{0}만 안 돼고, 나머지는 다 돼요.".format(food)
    ],
    "떡볶이": [
        "알겠습니다. 음료는 안 필요하세요?"
    ],
    "돈까스": [
        "알겠습니다. 음료는 안 필요하세요?"
    ],
    "콜라": [
        "네, 알겠습니다.",
        "주문하신 {0} 먼저 가져다 드리겠습니다.".format(drink)
    ],
    "염색":[
        "네. 더 필요하신 것 있으신가요?",
        "네. 혹시 머리도 조금 잘라 드릴까요?"
    ],
    "주세요": [
        "죄송하지만 오늘은 {0}이 다 팔렸어요.".format(food),
        "{0} 재료가 다 떨어졌어요.".format(food),
        "여기는 {0} 안 팔아요.".format(food)
    ],
    "예약":[
        "아, 그렇군요. 다행히 지금은 손님이 없어서 예약 없이 바로 하실 수 있을 것 같아요. 어떤 스타일을 원하세요?",
        "아, 네네. 이쪽으로 들어와 주세요. 어떻게 해 드릴까요?"
    ],
    "걸":[
        "2시간 정도 걸려요. 잠시 저쪽에 앉으셔서 기다려 주세요!",
        "조금 더 빨리 끝날 수도 있긴 한데, 2시간 정도 잡으셔야 돼요. 잠시 저쪽에서 기다려 주세요!"
    ],
    "도":[
        "흠, 네. 그래도 심하지 않아서 약 먹으면 금방 나으실 거에요. 여기 처방전입니다. 약국에 보여주시면 돼요.",
        "약 먹으면 금방 나으실 거에요. 처방전 드릴테니까 약국에서 약 받아가세요."
    ],
    "부터":[
        "혹시 다른 증상은 없으신가요?",
        "힘드셨겠네요. 다른 곳은 괜찮으신가요?"
    ],
    "아파":[
        "이런. 언제부터 아프셨어요?",
        "그런군요. 증상이 처음 나타났던 게 언제인가요?"
    ],
    "둘러보":[
        "네, 도움 필요하시면 말씀해 주세요.",
        "알겠습니다. 필요한거 있으시면 불러주세요."
    ],
    "얼마":[
        "만원입니다. 마음에 드시면 입어보셔도 돼요.",
        "원래 2만원인데 세일해서 만원에 드려요. 뒤쪽에서 입어보셔도 돼요.",
        "만원에 드릴게요. 입어 보시겠어요?"
    ],
    "입":[
        "계산대 뒤쪽에 있어요. 사이즈 안 맞으면 말씀해 주세요.",
        "이쪽으로 따라와 주세요. 사이즈는 그거 괜찮으신가요?",
        "저쪽으로 가시면 돼요. 사이즈는 맞으신가요?"
    ],
    "사이즈":[
        "네, 가져다 드리겠습니다.",
        "아마 있을 거에요. 한 번 찾아보겠습니다."
    ],
    "안녕":[
        "반가워요. 어느 나라에서 오셨어요?",
        "만나서 반갑습니다! 혹시 어느 나라 사람이세요?"
    ],
    "왔":[
        "{0} 한 번 가 보고 싶었는데! 혹시 한국에 오게 된 계기가 뭔가요?".format(country),
        "예전에 {0} 여행갔었는데, 진짜 재미있었어요. 혹시 한국에 오게 된 계기가 뭐에요?".format(country)
    ],
    "한국":[
        "그렇군요. 다들 이유가 다양한 것 같아서 궁금했어요. 혹시 취미가 뭐에요?",
        "아하! 취미는 뭐에요?"
    ],
    "취미":[
        "저도 {0} 좋아해요. 친하게 지내요!".format(hobby),
        "제 친구중에 {0} 좋아하는 친구 있는데, 소개시켜 드려야 겠네요. 우리 친하게 지내요!".format(hobby)
    ],
    "default": ["다시 말씀해 주시겠어요?"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    for i in responses.keys():
        if i in message:
            bot_message = random.choice(responses[i])
            break
        else:
            bot_message = random.choice(responses["default"])
    #
    # if message in responses.keys():
    #     bot_message = random.choice(responses[message])
    # else:
    #     # Return a random "default" response
    #     bot_message = random.choice(responses["default"])

    return bot_message

print("#1. 음식점")
print("Bot :","무엇을 드릴까요?")
print("#음식(라면) #주세요")
#say = "라면 주세요."
say = input()
print("I :",say)
print("Bot :",respond(say))
print("#팔다 #?")
#say_two = "그럼 뭐 팔아요?"
say_two = input()
print("I :",say_two)
print("Bot :",respond(say_two))
print("#떡볶이 / 돈까스 #주세요")
#say_three = "떡볶이 주세요."
say_three = input()
print("I :",say_three)
print("Bot :",respond(say_three))
print("#음료(콜라) #주세요")
# say_four = "콜라 주세요."
say_four = input()
print("I :",say_four)
print("Bot :",respond(say_four))

print("#2. 미용실")
print("Bot :","안녕하세요. 도담미용실입니다. 혹시 예약 하셨나요?")
print("#예약 #부정")
# bar_say1 = "아니요. 예약 안 했습니다."
bar_say1 = input()
print("I :",bar_say1)
print("Bot :",respond(bar_say1))
print("#색깔 #염색")
# bar_say2 = "갈색으로 염색하고 싶어요."
bar_say2=input()
print("I :",bar_say2)
print("Bot :",respond(bar_say2))
print("#조금 #다듬다")
# bar_say3 = "끝에만 조금 다듬어 주세요."
bar_say3=input()
print("I :",bar_say3)
print("Bot :",respond(bar_say3))
print("#걸리다 #?")
# bar_say4 = "얼마나 걸리나요?" ######ERROR 걸려요
bar_say4 = input()
print("I :",bar_say4)
print("Bot :",respond(bar_say4))

print("#3. 병원")
print("Bot :","안녕하세요. 무슨 일로 오셨나요?")
print("#신체 #아프다")
# hos_say1 = "계속 머리가 아파서 왔어요." ########ERROR 아파서
hos_say1 = input()
print("I :",hos_say1)
print("Bot :",respond(hos_say1))
print("#숫자 #과거")
# hos_say2 = "이틀 전부터 아팠어요." ################어제 네시요.
hos_say2 = input()
print("I :",hos_say2)
print("Bot :",respond(hos_say2))
print("#신체 #도")
# hos_say3 = "배도 조금 아파요."
hos_say3 = input()
print("I :",hos_say3)
print("Bot :",respond(hos_say3))
print("#감사")
# hos_say4 = "감사합니다."
hos_say4 = input()
print("I :",hos_say4)
print("Bot :","네, 안녕히 가세요.")


print("#4. 옷가게")
print("Bot :","안녕하세요. 찾으시는 물건 있으신가요?")
print("#부정 #둘러보다")
# shop_say1 = "아니요, 그냥 둘러보려구요." ###########아니요, 한 번 둘러볼게요.
shop_say1 = input()
print("I :",shop_say1)
print("Bot :",respond(shop_say1))
print("#지칭 #얼마")
# shop_say2 = "이거 얼마에요?"
shop_say2 = input()
print("I :",shop_say2)
print("Bot :",respond(shop_say2))
print("#어디 #입다")
# shop_say3 = "옷 입어보는 곳은 어디에요?"
shop_say3 = input()
print("I :",shop_say3)
print("Bot :",respond(shop_say3))
print("#사이즈, #?") ##########질문이 명확하지 않음
# shop_say4 = "혹시 더 큰 사이즈 있나요?"
shop_say4 = input()
print("I :",shop_say4)
print("Bot :", respond(shop_say4))

print("#5. 자기소개")
print("Bot :","안녕하세요. 처음 뵙겠습니다! 저는 도담이에요.")
print("#안녕 #이름")
# intro_say1 = "안녕하세요, 저는 샐리에요." ################반갑습니다. 제 이름은 차윤지입니다.
intro_say1 = input()
print("I :",intro_say1)
print("Bot :",respond(intro_say1))
print("#국가 #오다")
# intro_say2 = "독일에서 왔어요."#오- -았- -어- 요.
intro_say2 = input()
print("I :",intro_say2)
print("Bot :",respond(intro_say2))
print("#한국")
# intro_say3 = "한류에 관심이 많아서 한국에 오게 되었어요."
intro_say3 = input()
print("I :",intro_say3)
print("Bot :",respond(intro_say3))
print("#취미")
# intro_say4 = "제 취미는 독서에요."
intro_say4 = input()
print("I :",intro_say4)
print("Bot :", respond(intro_say4))


# def respond(message):
#     # Check for a question mark
#     if message.endswith("?"):
#         # Return a random question
#         return random.choice(responses["question"])
#     # Return a random statement
#     return random.choice(responses["statement"])
