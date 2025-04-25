from linebot import (LineBotApi, WebhookHandler)
from linebot.models import RichMenu, RichMenuArea, RichMenuBounds, MessageAction, URIAction
import os
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# 建立 Rich Menu
rich_menu_to_create = RichMenu(
    size={"width":2500,"height":1686},
    selected=True,
    name="主選單",
    chat_bar_text="點我打開主選單",
    areas=[
        # 第一列
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=833, height=843),
            action=MessageAction(label="查詢匯率", text="查詢匯率")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=833, y=0, width=833, height=843),
            action=MessageAction(label="營業時間", text="營業時間")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=1666, y=0, width=833, height=843),
            action=MessageAction(label="營業地址", text="營業地址")
        ),
        # 第二列
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=843, width=833, height=843),
            action=MessageAction(label="貼圖或表情符號", text="貼圖或表情符號")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=833, y=843, width=833, height=843),
            action=MessageAction(label="門市照片", text="門市照片")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=1666, y=843, width=416, height=843),
            action=MessageAction(label="交通資訊", text="交通")
        ),
        # 第三列
        RichMenuArea(
            bounds=RichMenuBounds(x=2082, y=843, width=418, height=843),
            action=URIAction(label="官方網站", uri="https://www.google.com/search?q=nba&rlz=1C1RXQR_zh-TWTW944TW944&oq=nba&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyBwgBEC4YgAQyDQgCEAAYgwEYsQMYgAQyDQgDEAAYgwEYsQMYgAQyDQgEEAAYgwEYsQMYgAQyDQgFEAAYgwEYsQMYgAQyDQgGEAAYgwEYsQMYgAQyDQgHEAAYgwEYsQMYgAQyDQgIEAAYgwEYsQMYgAQyDQgJEAAYgwEYsQMYgATSAQg1NjQ0ajBqN6gCCLACAfEFtDLUdEBxHuA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11y43tsvgm;3;/m/05jvx;mt;fp;1;;;")
        )
    ]
)
# 建立選單並取得 ID
rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# 上傳圖片
with open("喬丹和柯比.png", "rb") as image_file:
    line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", image_file)
# 設為預設選單（所有人都會看到）
line_bot_api.set_default_rich_menu(rich_menu_id)
