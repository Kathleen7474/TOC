from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_message, send_start_button, send_hobby_button, send_time_button, send_result_message
hobby1_text = ""
hobby2_text = ""
hobby3_text = ""


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_lovelove(self, event):
        text = event.message.text
        return text.lower() == "lovelove"

    def is_going_to_study_init(self, event):
        text = event.message.text
        return text.lower() == "study"

    def is_going_to_study_60up(self, event):
        text = event.message.text
        return text.lower() == "above"

    def is_going_to_study_60below(self, event):
        text = event.message.text
        return text.lower() == "below"

    def is_going_to_company_init(self, event):
        text = event.message.text
        return text.lower() == "company"

    def is_going_to_company_60below(self, event):
        text = event.message.text
        return text.lower() == "below"

    def is_going_to_company_60up(self, event):
        text = event.message.text
        return text.lower() == "above"

    def is_going_to_sports_init(self, event):
        text = event.message.text
        return text.lower() == "sports"

    def is_going_to_sports_60below(self, event):
        text = event.message.text
        return text.lower() == "below"

    def is_going_to_sports_60up(self, event):
        text = event.message.text
        return text.lower() == "above"

    def is_going_to_hobby_init(self, event):
        text = event.message.text
        return text.lower() == "hobby"

    def is_going_to_hobby1_init(self, event):
        text = event.message.text
        return text.lower() == "hobby1"

    def is_going_to_hobby1_60below(self, event):
        text = event.message.text
        return text.lower() == "below"

    def is_going_to_hobby1_60up(self, event):
        text = event.message.text
        return text.lower() == "above"

    def is_going_to_hobby2_init(self, event):
        text = event.message.text
        return text.lower() == "hobby2"

    def is_going_to_hobby2_60below(self, event):
        text = event.message.text
        return text.lower() == "below"

    def is_going_to_hobby2_60up(self, event):
        text = event.message.text
        return text.lower() == "above"

    def is_going_to_hobby3_init(self, event):
        text = event.message.text
        return text.lower() == "hobby3"

    def is_going_to_hobby3_60below(self, event):
        text = event.message.text
        return text.lower() == "below"

    def is_going_to_hobby3_60up(self, event):
        text = event.message.text
        return text.lower() == "above"

    def is_going_to_hobby1_enter(self, event):
        text = event.message.text
        return text.lower() != ""

    def is_going_to_hobby2_enter(self, event):
        text = event.message.text
        return text.lower() != ""

    def is_going_to_hobby3_enter(self, event):
        text = event.message.text
        return text.lower() != ""

    def on_enter_start(self, event):
        print("enter start")

        reply_token = event.reply_token
        send_start_button(reply_token)

    def on_enter_study_init(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_time_button(reply_token)
        # send_image_message(
        #     reply_token, 'https://i.imgur.com/fmqsEDp.jpg')     可以跑出圖片

    def on_enter_lovelove(self, event):
        print("I'm entering lovelove")

        reply_token = event.reply_token
        send_result_message(
            reply_token, 'https://i.imgur.com/3oEqjwh.png', "早生貴子：）））））））\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_study_60up(self, event):
        print("I'm entering study_60up")

        reply_token = event.reply_token
        send_result_message(
            reply_token, 'https://i.imgur.com/s8CPUMb.jpg', "今天很認真ㄛ～\n送你一棵小樹\n明天繼續加油!\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_study_60below(self, event):
        print("I'm entering study_60below")

        reply_token = event.reply_token
        send_result_message(
            reply_token, 'https://i.imgur.com/YvcdZ8u.jpg', "送你可愛小種子ㄛ～\n努力會開花結果\n明天繼續加油呦\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_company_init(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_time_button(reply_token)

    def on_enter_company_60up(self, event):
        print("I'm entering company_60up")

        reply_token = event.reply_token
        send_result_message(
            reply_token, 'https://i.imgur.com/4722NOg.jpg', "你是溫暖小天使～\n送你一棵榕樹\n祝全家人身體健康\n明天繼續加油!\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_company_60below(self, event):
        print("I'm entering company_60below")

        reply_token = event.reply_token
        send_result_message(
            reply_token, 'https://i.imgur.com/YvcdZ8u.jpg', "送你可愛小種子ㄛ～\n努力會開花結果\n明天繼續加油呦\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_sports_init(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_time_button(reply_token)

    def on_enter_sports_60up(self, event):
        print("I'm entering sports_60up")

        reply_token = event.reply_token
        send_result_message(
            reply_token, 'https://i.imgur.com/yVwDjF9.png', "身體健康精神好：）））））\n送你一棵椰子樹\n明天繼續加油!\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_sports_60below(self, event):
        print("I'm entering sports_60below")

        reply_token = event.reply_token
        send_result_message(
            reply_token, 'https://i.imgur.com/YvcdZ8u.jpg', "送你可愛小種子ㄛ～\n努力會開花結果\n明天繼續加油呦\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_hobby_init(self, event):
        print("I'm entering state4")

        global hobby1_text
        hobby1_text = ""
        global hobby2_text
        hobby2_text = ""
        global hobby3_text
        hobby3_text = ""
        reply_token = event.reply_token
        send_hobby_button(reply_token)

    def on_enter_hobby1_init(self, event):
        print("I'm entering hobby1")

        reply_token = event.reply_token
        send_text_message(reply_token, "幫我輸入你的興趣喔～～～\n直接打入對話框")

    def on_enter_hobby2_init(self, event):
        print("I'm entering hobby2")

        reply_token = event.reply_token
        send_text_message(reply_token, "幫我輸入你的興趣喔～～～\n直接打入對話框")

    def on_enter_hobby3_init(self, event):
        print("I'm entering hobby3")

        reply_token = event.reply_token
        send_text_message(reply_token, "幫我輸入你的興趣喔～～～\n直接打入對話框")

    def on_enter_hobby1_enter(self, event):
        print("I'm entering input hobby3")

        reply_token = event.reply_token
        global hobby1_text
        hobby1_text = event.message.text
        send_time_button(reply_token)

    def on_enter_hobby1_60up(self, event):
        print("I'm entering hobby1_60up")

        reply_token = event.reply_token
        global hobby1_text
        # send_text_message(reply_token, "Trigger hobby160up")
        send_result_message(
            reply_token, 'https://i.imgur.com/pgTLCOr.png', "挖賽你是"+hobby1_text+"達人吧～\n你已經太強了\n送你漂亮櫻花樹，可以欣賞漂亮櫻花\n明天繼續加油!\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_hobby1_60below(self, event):
        print("I'm entering hobby1_60below")

        reply_token = event.reply_token
        global hobby1_text
        # send_text_message(reply_token, "Trigger hobby160below")
        send_result_message(
            reply_token, 'https://i.imgur.com/YvcdZ8u.jpg', "送你可愛小種子ㄛ～\n努力會開花結果\n明天繼續加油呦\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_hobby2_enter(self, event):
        print("I'm entering input hobby3")

        reply_token = event.reply_token
        global hobby2_text
        hobby2_text = event.message.text
        send_time_button(reply_token)

    def on_enter_hobby2_60up(self, event):
        print("I'm entering hobby2_60up")

        reply_token = event.reply_token
        global hobby2_text
        # send_text_message(reply_token, "Trigger hobby160up")
        send_result_message(
            reply_token, 'https://i.imgur.com/tPQhM69.jpg', "挖賽你是"+hobby2_text+"達人吧～\n你已經太強了\n送你橘子樹，可以摘橘子吃\n明天繼續加油!\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_hobby2_60below(self, event):
        print("I'm entering hobby2_60below")

        reply_token = event.reply_token
        global hobby2_text
        # send_text_message(reply_token, "Trigger hobby160below")
        send_result_message(
            reply_token, 'https://i.imgur.com/YvcdZ8u.jpg', "送你可愛小種子ㄛ～\n努力會開花結果\n明天繼續加油呦\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_hobby3_enter(self, event):
        print("I'm entering input hobby3")

        reply_token = event.reply_token
        global hobby3_text
        hobby3_text = event.message.text
        send_time_button(reply_token)

    def on_enter_hobby3_60up(self, event):
        print("I'm entering hobby3_60up")

        reply_token = event.reply_token
        global hobby3_text
        # send_text_message(reply_token, "Trigger hobby160up")
        send_result_message(
            reply_token, 'https://i.imgur.com/rNfwHLw.jpg', "挖賽你是"+hobby3_text+"達人吧～\n你已經太強了\n送你一顆小柳樹\n明天繼續加油!\n\n輸入任意文字回到start")
        self.go_back()

    def on_enter_hobby3_60below(self, event):
        print("I'm entering hobby2_60below")

        reply_token = event.reply_token
        global hobby3_text
        # send_text_message(reply_token, "Trigger hobby160below")
        send_result_message(
            reply_token, 'https://i.imgur.com/YvcdZ8u.jpg', "送你可愛小種子ㄛ～\n努力會開花結果\n明天繼續加油呦\n\n輸入任意文字回到start")
        self.go_back()
