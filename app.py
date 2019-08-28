# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
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
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton, CarouselContainer
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

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
        
        if isinstance(event, FollowEvent):
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='這裡提供各種遊戲攻略，請輸入"攻略"以接受最新遊戲訊息，不然就會一直發大財'))
        if isinstance(event, MessageEvent):
            text = event.message.text
    #for FGO
            if text == '攻略':
                fgo = BubbleContainer(
                      direction='ltr',
                      header=BoxComponent(
                        layout='horizontal',
                        contents=[
                            TextComponent(
                                text='FGO 最新攻略 (appmedia日文)',
                                size='md',
                                weight='bold', 
                                color='#1CA0DC'
                            ),
                        ]
                      ),
                      hero=ImageComponent(
                        url='https://pbs.twimg.com/media/D1huyvBU4AEiDtf.jpg',
                        size='full',
                        margin='sm',
                        aspect_ratio='1.51:1',
                        aspect_mode='cover',
                        gravity='bottom',
                        align='center',
                      ),
                     body=BoxComponent(
                         layout='horizontal',
                         spacing='md',
                         contents=[
                             BoxComponent(
                                 layout='vertical',
                                 flex=1,
                                 contents=[
                                     ImageComponent(
                                         url='https://appmedia.jp/wp-content/uploads/2019/08/top_banner.png',
                                         size='full',
                                         flex=0,
                                         margin='lg',
                                         align='end',
                                         aspect_ratio='1.91:1',
                                         aspect_mode='cover',
                                         background_color='#060000',
                                         action=URIAction(label='website', uri='https://appmedia.jp/fategrandorder/3706486')
                                     ),
                                     ImageComponent(
                                         url='https://appmedia.jp/wp-content/uploads/2017/09/d91d441543dc34269289e49c36343e25.png',
                                         size='full',
                                         margin='md',
                                         aspect_ratio='1.91:1',
                                         aspect_mode='cover',
                                         background_color='#000000'
                                     ),
                                     ImageComponent(
                                         url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh1KnzPNfkRTC5fSB-X6CvWqxUEgj7Nwx4OBY9pUI-blkt43_r',
                                     
                                     )
                                 ]
                             ),
                             BoxComponent(
                                 layout='vertical',
                                 flex=2,
                                 contents=[
                                     ButtonComponent(
                                         action=URIAction(label='水着剣豪七色勝負 活動攻略', uri='https://appmedia.jp/fategrandorder/3706486'),
                                         style='link',
                                         margin='md',
                                         gravity='top',
                                         height='sm'
                                     ),
                                     SeparatorComponent(margin='md', color='#FFFFFF'),
                                     ButtonComponent(
                                         action=URIAction(label='素材一覧', uri='https://appmedia.jp/fategrandorder/98413'),
                                         style='link',
                                         margin='md',
                                         gravity='top',
                                         height='sm'
                                     ),
                                     SeparatorComponent(margin='md', color='#FFFFFF'),
                                     ButtonComponent(
                                         action=URIAction(label='五星從者攻略一覽', uri='https://appmedia.jp/fategrandorder/96261'),
                                         style='link',
                                         margin='md',
                                         gravity='top',
                                         height='sm'
                                     ),
                                     
                                 ]
                             )
                         ]
                     ),
                    footer=BoxComponent(
                        layout='horizontal',
                        contents=[
                            ButtonComponent(
                                action=URIAction(label='更多攻略', uri='https://appmedia.jp/fategrandorder'),
                                flex=7,
                                gravity='top'
                            )
                        ],
                    )
                 )
                #message = FlexSendMessage(alt_text="Fate/GrandOrder攻略", contents=bubble)
                #line_bot_api.reply_message(event.reply_token, message)
            #elif text.lower()=='gbf'.lower() or text.lower()=='granblue fantasy'.lower() or text=='碧藍幻想':
                gbf = BubbleContainer(
                            direction='ltr',
                            header=BoxComponent(
                                layout='horizontal',
                                contents=[
                                    TextComponent(
                                    text='碧蘭幻想攻略',
                                    size='md',
                                    weight='bold',
                                    color='#18BCF4'
                                   )
                                ]
                            ),
                            hero=ImageComponent(
                                url='https://www.thesubnation.com/dev3/sites/default/files/styles/wide_background/public/2019-06/granblue_fantasy_versus_cover.jpg?h=8f74817f&itok=dnPJIhT8',
                                size='full',
                                aspect_ratio='20:13',
                                aspect_mode='cover'                                                       
                            ),
                            body=BoxComponent(
                                layout='horizontal',
                                spacing = 'md',
                                contents=[
                                    BoxComponent(
                                        layout='vertical',
                                        flex=1,
                                        contents=[
                                            ImageComponent(
                                                url='https://images-na.ssl-images-amazon.com/images/I/A1GKAs+6ykL.jpg',
                                                size='full',
                                                aspect_ratio='16:9',
                                                aspect_mode='cover'
                                            ),
                                            
                                            ImageComponent(
                                                url='https://truth.bahamut.com.tw/s01/201805/e35c8592c8941c560e6d692a20a6440d.JPG',
                                                size='full',
                                                margin='md',
                                                aspect_ratio='16:9',
                                                aspect_mode='cover'
                                            ),
                                            ImageComponent(
                                                url='https://img.ruten.com.tw/s2/6/3c/e8/21742224438504_873.jpg',
                                                margin='md',
                                                size='full',
                                                aspect_ratio='16:9',
                                                aspect_mode='cover'
                                            )                                           
                                        ]
                                    ),
                                    BoxComponent(
                                        layout='vertical',
                                        contents=[
                                            ButtonComponent(
                                                action=URIAction(label='SSR角色', uri='https://gbf.huijiwiki.com/wiki/SSR人物'),
                                                style='primary',
                                             ),
                                            SeparatorComponent(margin='xxl', color='#FFFFFF'),
                                            SeparatorComponent(margin='sm', color='#FFFFFF'),
                                            TextComponent(
                                                text='    新手向武器編成',
                                                size='sm',
                                                weight='bold',
                                                margin='xs'
                                            ),
                                            
                                            ButtonComponent(
                                                action=URIAction(label='攻略連結', uri='https://forum.gamer.com.tw/C.php?bsn=25204&snA=7062'),
                                                style='primary',
                                                margin='sm',
                                                height='sm',
                                                
                                             ),
                                            
                                            SeparatorComponent(margin='sm', color='#FFFFFF'),
                                            SeparatorComponent(margin='lg', color='#FFFFFF'),
                                            ButtonComponent(
                                                action=URIAction(label='最新情報', uri='https://グランブルーファンタジー.gamewith.jp/article/show/21113'),
                                                style='primary',
                                             ),
                                        ]
                                    )
                                ]
                            ),
                            footer=BoxComponent(
                                layout='horizontal',
                                contents=[
                                    ButtonComponent(
                                        action=URIAction(label='更多攻略', uri='https://gbf.huijiwiki.com/wiki/SSR人物'),
                                        
                                    )
                                ]
                            )
                         )
                """
                sv = BubbleContainer(
                        direction='ltr',
                        header=BoxComponent(
                            layout='horizontal',
                            contents=[
                                TextComponent
                            ]
                        )
                )
                """
                
                carousel = CarouselContainer(contents=[fgo, gbf])
                message = FlexSendMessage(alt_text="更多攻略", contents=carousel)
                line_bot_api.reply_message(event.reply_token, message)
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發大財'))
            
        
  
        
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
            
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='fdt'))


    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
    
"""
def gbf():
    bubble = BubbleContainer(
                            direction='ltr',
                            header=BoxComponent(
                                layout='horizontal',
                                contents=[
                                    TextComponent(
                                    text='碧蘭幻想攻略',
                                    size='md',
                                    weight='bold',
                                    color='#18BCF4'
                                   )
                                ]
                            )
                        )
"""
    



