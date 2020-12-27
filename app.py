import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn
from linebot.exceptions import LineBotApiError

from fsm import TocMachine
from utils import send_text_message
from utils import send_image_message
from utils import send_start_button
to = 'U4b49ae680677e8221bdfea9fd0100d2d'
load_dotenv()


machine = TocMachine(
    states=["start", "user", "study_init",
            "company_init", "sports_init", "hobby_init", "hobby1_init", "hobby2_init", "hobby3_init",
            "hobby1_enter", "hobby2_enter", "hobby3_enter",
            "study_60up", "study_60below",
            "company_60up", "company_60below",
            "sports_60up", "sports_60below",
            "hobby1_60up", "hobby1_60below",
            "hobby2_60up", "hobby2_60below",
            "hobby3_60up", "hobby3_60below", "lovelove"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "lovelove",
            "conditions": "is_going_to_lovelove",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "study_init",
            "conditions": "is_going_to_study_init",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "company_init",
            "conditions": "is_going_to_company_init",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "sports_init",
            "conditions": "is_going_to_sports_init",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "hobby_init",
            "conditions": "is_going_to_hobby_init",
        },
        {
            "trigger": "advance",
            "source": "hobby_init",
            "dest": "hobby1_init",
            "conditions": "is_going_to_hobby1_init",
        },
        {
            "trigger": "advance",
            "source": "hobby_init",
            "dest": "hobby2_init",
            "conditions": "is_going_to_hobby2_init",
        },
        {
            "trigger": "advance",
            "source": "hobby_init",
            "dest": "hobby3_init",
            "conditions": "is_going_to_hobby3_init",
        },
        {
            "trigger": "advance",
            "source": "hobby3_init",
            "dest": "hobby3_enter",
            "conditions": "is_going_to_hobby3_enter",
        },
        {
            "trigger": "advance",
            "source": "hobby1_init",
            "dest": "hobby1_enter",
            "conditions": "is_going_to_hobby1_enter",
        },
        {
            "trigger": "advance",
            "source": "hobby2_init",
            "dest": "hobby2_enter",
            "conditions": "is_going_to_hobby2_enter",
        },
        {
            "trigger": "advance",
            "source": "study_init",
            "dest": "study_60up",
            "conditions": "is_going_to_study_60up",
        },
        {
            "trigger": "advance",
            "source": "study_init",
            "dest": "study_60below",
            "conditions": "is_going_to_study_60below",
        },
        {
            "trigger": "advance",
            "source": "company_init",
            "dest": "company_60up",
            "conditions": "is_going_to_company_60up",
        },
        {
            "trigger": "advance",
            "source": "company_init",
            "dest": "company_60below",
            "conditions": "is_going_to_company_60below",
        },
        {
            "trigger": "advance",
            "source": "sports_init",
            "dest": "sports_60up",
            "conditions": "is_going_to_sports_60up",
        },
        {
            "trigger": "advance",
            "source": "sports_init",
            "dest": "sports_60below",
            "conditions": "is_going_to_sports_60below",
        },
        {
            "trigger": "advance",
            "source": "hobby1_enter",
            "dest": "hobby1_60up",
            "conditions": "is_going_to_hobby1_60up",
        },
        {
            "trigger": "advance",
            "source": "hobby1_enter",
            "dest": "hobby1_60below",
            "conditions": "is_going_to_hobby1_60below",
        },
        {
            "trigger": "advance",
            "source": "hobby2_enter",
            "dest": "hobby2_60up",
            "conditions": "is_going_to_hobby2_60up",
        },
        {
            "trigger": "advance",
            "source": "hobby2_enter",
            "dest": "hobby2_60below",
            "conditions": "is_going_to_hobby2_60below",
        },
        {
            "trigger": "advance",
            "source": "hobby3_enter",
            "dest": "hobby3_60up",
            "conditions": "is_going_to_hobby3_60up",
        },
        {
            "trigger": "advance",
            "source": "hobby3_enter",
            "dest": "hobby3_60below",
            "conditions": "is_going_to_hobby3_60below",
        },
        {"trigger": "go_back", "source": [
            "study_60up", "study_60below",
            "company_60up", "company_60below",
            "sports_60up", "sports_60below",
            "hobby1_60up", "hobby1_60below",
            "hobby2_60up", "hobby2_60below",
            "hobby3_60up", "hobby3_60below", "lovelove"], "dest": "start"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():

    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:

        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if event.message.text == 'fsm':
                send_image_message(
                    event.reply_token, 'https://concentrate-tree.herokuapp.com//show-fsm')
            elif event.message.text == 'button':
                url = 'https://i.imgur.com/fmqsEDp.jpg'
                buttons_template = TemplateSendMessage(
                    alt_text='Buttons Template',
                    template=ButtonsTemplate(
                        title='這是ButtonsTemplate',
                        text='ButtonsTemplate可以傳送text,uri',
                        thumbnail_image_url=url,
                        actions=[
                            MessageTemplateAction(
                                label='ButtonsTemplate',
                                text='button'
                            ),
                            # URITemplateAction(
                            #     label='VIDEO1',
                            #     uri='影片網址'
                            # ),
                            PostbackTemplateAction(
                                label='postback',
                                text='postback text',
                                data='postback1'
                            )
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, buttons_template)
            else:
                if machine.state == "start":
                    send_start_button(event.reply_token)
                elif machine.state == "user":
                    send_text_message(event.reply_token, "輸入'start'來開始呦～～～")
                else:
                    send_text_message(event.reply_token, "我沒空做防呆，不要亂按")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
