from __future__ import unicode_literals
import os

# 增加了 render_template
from flask import Flask, request, abort
from flask import render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

import ConfigParser

import urllib
import re
import random

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('DhIKc3UtGRqczVokSXd66/V6zCbnvWfjilsQ9gzhmugnBKRc0zMBcl8383+aWFIAWvyqZ2YQ94q9vZm2dL772qzldHUTX/vWUFjj6w3CgxoQ2fChWP3Njm9sJ/jxnKNXmH5CgY8VOaDUVUcUszUwAgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a93474f80e67e0971d14357752cfb0a2')

# 增加的這段放在下面
@app.route("/")
def home():
    return render_template("home.html")
# 增加的這段放在上面

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
#
# # 處理訊息
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     message = TextSendMessage(text=event.message.text)
#     line_bot_api.reply_message(event.reply_token, message)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text






    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID

    elif(text=="你好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    else:
        reply_text = text
#如果非以上的選項，就會學你說話





    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)