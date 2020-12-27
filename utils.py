import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, ImageSendMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn
from linebot.exceptions import LineBotApiError
to = 'U4b49ae680677e8221bdfea9fd0100d2d'

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(id, img_url):
    pass


def send_start_button(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        # thumbnail_image_url='https://i.imgur.com/fmqsEDp.jpg',    -------------- 放圖片用
        template=ButtonsTemplate(
            title='分享一下今天的生活吧',
            text='(你今天做了甚麼)',
            actions=[
                MessageTemplateAction(
                    label='讀書',
                    text='study'
                ),
                MessageTemplateAction(
                    label='陪伴家人',
                    text='company'
                ),
                MessageTemplateAction(
                    label='運動',
                    text='sports'
                ),
                MessageTemplateAction(
                    label='興趣',
                    text='hobby'
                ),

            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)
    return "ok"


def send_hobby_button(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        # thumbnail_image_url='https://i.imgur.com/fmqsEDp.jpg',    -------------- 放圖片用
        template=ButtonsTemplate(
            title='選擇輸入的興趣',
            text='(可以選擇其中一個)',
            actions=[
                MessageTemplateAction(
                    label='興趣1',
                    text='hobby1'
                ),
                MessageTemplateAction(
                    label='興趣2',
                    text='hobby2'
                ),
                MessageTemplateAction(
                    label='興趣3',
                    text='hobby3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)
    return "ok"


def send_time_button(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        # thumbnail_image_url='https://i.imgur.com/fmqsEDp.jpg',    -------------- 放圖片用
        template=ButtonsTemplate(
            title='今天做了幾個小時呢?',
            text='(選擇時間)',
            actions=[
                MessageTemplateAction(
                    label='1小時以上',
                    text='above'
                ),
                MessageTemplateAction(
                    label='不到一小時',
                    text='below'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)
    return "ok"


def send_button_message(id, text, buttons):
    pass


def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    # message = ImageSendMessage(
    #     type='image',
    #     original_content_url="https://i.imgur.com/eTldj2E.png?1",
    #     preview_image_url="https://i.imgur.com/eTldj2E.png?1"
    # )
    # line_bot_api.reply_message(reply_token, message)
    try:
        line_bot_api.push_message(to, ImageSendMessage(
            original_content_url=url, preview_image_url=url))
    except LineBotApiError as e:
        # error handle
        raise e
    return "OK"


def send_result_message(reply_token, url, text):
    # line_bot_api = LineBotApi(channel_access_token)
    # line_bot_api.push_message(to, ImageSendMessage(
    #     original_content_url=url, preview_image_url=url))
    # line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',

        template=ButtonsTemplate(
            title='恭喜',
            text=text,
            thumbnail_image_url=url,
            actions=[
                MessageTemplateAction(
                    label='完成',
                    text='finish'
                ),

            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)
    return "ok"
