"""
暖心便签弹窗阵列

运行方式示例:
    python 暖心便签弹窗阵列.py --count 200

参数:
    --count N    要创建的弹窗数量 (默认 200)
    --stagger ms 每个弹窗创建的间隔毫秒 (默认 80)
    --test       使用少量弹窗 (5) 仅用于快速本地测试

打包建议:
    使用 pyinstaller:
      pip install pyinstaller
      pyinstaller --onefile --noconsole 暖心便签弹窗阵列.py

说明:
    弹窗使用 tkinter 创建为顶层窗口, 每个弹窗会在若干秒后自动关闭。
    字体使用 Times New Roman (新罗马字体)。
"""

import random
import argparse
import tkinter as tk
from tkinter import font as tkfont


WARM_MESSAGES = [
    # 中文 - 毛泽东相关 (13个)
    "好好学习，天天向上",
    "为人民服务",
    "世界是你们的，也是我们的，但是归根结底是你们的",
    "星星之火，可以燎原",
    "团结就是力量",
    "没有调查就没有发言权",
    "实事求是",
    "群众路线",
    "自力更生，艰苦奋斗",
    "独立自主",
    "敢于斗争，敢于胜利",
    "谦虚谨慎，戒骄戒躁",
    "理论联系实际",
    # 中文 - 其他关心体贴话 (37个)
    "记得多喝水，照顾好自己",
    "今天也要开心哦",
    "爱自己，从小事做起",
    "休息好了，才能更好地前行",
    "你的笑容是最美的风景",
    "家人永远是你的港湾",
    "健康的身体是最宝贵的财富",
    "睡个好觉，明天会更好",
    "吃好饭，照顾好胃",
    "天气凉了，多穿衣服",
    "心情不好时，听听音乐放松",
    "朋友的关心，是冬日里的暖阳",
    "爱是世界上最温暖的力量",
    "感恩身边的每一个人",
    "生活中的小确幸，要学会珍惜",
    "给自己一个拥抱，你值得被爱",
    "累了就休息，不要勉强自己",
    "梦想虽重要，但健康更重要",
    "温柔对待自己，也温柔对待他人",
    "每一天都是新的开始，充满希望",
    "微笑面对生活，你会更快乐",
    "爱家人，爱朋友，爱自己",
    "心灵的宁静，是最好的礼物",
    "学会原谅自己，也原谅别人",
    "幸福不是拥有多少，而是珍惜多少",
    "照顾好情绪，它是你最好的朋友",
    "多看看风景，放松心情",
    "爱是永恒的，陪伴是最长的告白",
    "珍惜当下，活在当下",
    "你的存在，就是这个世界的美好",
    "温柔以待，世界会温柔以待",
    "休息是充电，爱是动力",
    "健康快乐，就是最大的成功",
    "爱自己，才能更好地爱别人",
    "每一天，都要对自己说声谢谢",
    "心灵的花园，需要细心浇灌",
    "温暖的家，是心灵的归宿",
    "朋友的问候，是生活中的甜蜜",
    # 英文 - 关心体贴话 (50个)
    "Take good care of yourself today",
    "You are loved more than you know",
    "Rest when you need to, it's okay",
    "Your well-being comes first",
    "Smile, it makes everything better",
    "You deserve kindness, especially from yourself",
    "Drink water, stay hydrated",
    "Sleep well, dream sweetly",
    "Eat something nourishing today",
    "Wrap yourself in warmth and love",
    "Listen to your heart, it knows best",
    "You are enough, just as you are",
    "Give yourself a moment of peace",
    "Your feelings matter",
    "Be gentle with your soul",
    "Love yourself fiercely",
    "You are worthy of all good things",
    "Take a deep breath, you're doing fine",
    "Your presence lights up the world",
    "Cherish the little moments",
    "You are beautifully unique",
    "Nurture your inner child",
    "Forgive yourself, you're human",
    "You bring joy to those around you",
    "Embrace your imperfections",
    "Your heart is pure and kind",
    "Take time for what brings you peace",
    "You are stronger than you realize",
    "Love surrounds you always",
    "Be kind to your mind and body",
    "You are a gift to this world",
    "Rest your weary soul",
    "Your smile warms hearts",
    "Cherish your loved ones",
    "You are cherished and valued",
    "Listen to soothing music",
    "Breathe in peace, breathe out worry",
    "You are loved unconditionally",
    "Nourish your spirit daily",
    "Your kindness touches lives",
    "Embrace self-compassion",
    "You are worthy of rest",
    "Love yourself through the storms",
    "Your warmth heals others",
    "Cherish quiet moments",
    "You are a beacon of light",
    "Nurture your dreams gently",
    "Your heart deserves tenderness",
    "Love yourself, always",
    "You are perfectly imperfect",
    "Cherish your inner peace"
]
FINAL_MESSAGE = "Happy birthday to you!"

def pastel_color():
    # generate a soft pastel color
    r = int((random.randint(150, 255) + 255) / 2)
    g = int((random.randint(150, 255) + 255) / 2)
    b = int((random.randint(150, 255) + 255) / 2)
    return f"#{r:02x}{g:02x}{b:02x}"


def draw_rounded_rect(canvas: tk.Canvas, x1: int, y1: int, x2: int, y2: int, radius: int, **kwargs) -> None:
    radius = max(radius, 0)
    if radius == 0:
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
        return
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)
    canvas.create_oval(x1, y1, x1 + 2 * radius, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y1, x2, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x1, y2 - 2 * radius, x1 + 2 * radius, y2, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y2 - 2 * radius, x2, y2, **kwargs)


def create_popup(root, msg, x, y, bgcolor, index, close_after, final=False, all_windows=None):
    win = tk.Toplevel(root)
    win.title("")
    try:
        win.overrideredirect(True)
    except Exception:
        pass
    transparent = "#010101"
    win.configure(bg=transparent)
    try:
        win.wm_attributes("-transparentcolor", transparent)
    except Exception:
        win.configure(bg=bgcolor)
        transparent = bgcolor
    try:
        win.wm_attributes("-topmost", True)
    except Exception:
        win.attributes("-topmost", True)

    if final:
        width, height, radius = 420, 220, 48
    else:
        width, height, radius = 260, 150, 36

    win.geometry(f"{width}x{height}+{x}+{y}")

    canvas = tk.Canvas(win, bg=transparent, highlightthickness=0, width=width, height=height)
    canvas.pack(fill=tk.BOTH, expand=True)

    draw_rounded_rect(canvas, 8, 8, width - 8, height - 8, radius, fill=bgcolor, outline="")

    font_size = 18 if final else 15
    # Choose font based on message content
    if any('\u4e00' <= c <= '\u9fff' for c in msg):
        font_family = "宋体"  # Chinese font
    else:
        font_family = "Times New Roman"  # English font
    lbl_font = tkfont.Font(family=font_family, size=font_size, weight="bold")

    text_wrap = width - 80 if final else width - 60
    text_x = width / 2
    text_y = height / 2 if final else height / 2 - 6
    canvas.create_text(
        text_x,
        text_y,
        text=msg,
        font=lbl_font,
        width=text_wrap,
        fill="#2c2c2c",
        justify=tk.CENTER,
    )

    if all_windows is not None:
        all_windows.append(win)

    def close_all(_event=None):
        if all_windows:
            for w in all_windows:
                try:
                    w.destroy()
                except Exception:
                    pass
        try:
            root.quit()
        except Exception:
            pass

    if final:
        btn_font = tkfont.Font(family="Times New Roman", size=12, weight="bold")
        close_button = tk.Button(
            win,
            text="X",
            command=close_all,
            relief=tk.FLAT,
            font=btn_font,
            bg=bgcolor,
            fg="#333333",
            activebackground=bgcolor,
            activeforeground="#111111",
            bd=0,
            cursor="hand2",
        )
        canvas.create_window(width - 32, 32, window=close_button, anchor="ne")
        win.bind("<Escape>", close_all)
    # No auto-close for any popup


def schedule_popups(root: tk.Tk, count: int, stagger_ms: int, screen_w: int, screen_h: int) -> None:
    all_windows = []
    normal_count = max(count - 1, 0)

    # Select messages for normal popups, repeat if needed
    if normal_count <= len(WARM_MESSAGES):
        selected_messages = random.sample(WARM_MESSAGES, normal_count)
    else:
        # Need more messages than available, so repeat them
        times_to_repeat = (normal_count // len(WARM_MESSAGES)) + 1
        selected_messages = (WARM_MESSAGES * times_to_repeat)[:normal_count]
        random.shuffle(selected_messages)

    for i in range(normal_count):
        msg = selected_messages[i]
        bgcolor = pastel_color()
        margin_x = 80
        margin_y = 120
        x = random.randint(margin_x, max(margin_x, screen_w - 320))
        y = random.randint(margin_y, max(margin_y, screen_h - 240))

        root.after(
            i * stagger_ms,
            create_popup,
            root,
            msg,
            x,
            y,
            bgcolor,
            i,
            0,  # no auto close
            False,
            all_windows,
        )

    center_x = (screen_w - 420) // 2
    center_y = (screen_h - 220) // 2
    final_delay = normal_count * stagger_ms
    root.after(
        final_delay,
        create_popup,
        root,
        FINAL_MESSAGE,
        center_x,
        center_y,
        "#f7cade",
        count - 1,
        0.0,
        True,
        all_windows,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=150, help="number of popups to create")
    parser.add_argument("--stagger", type=int, default=80, help="ms between popup creation")
    parser.add_argument("--test", action="store_true", help="create only 5 popups for quick test")
    args = parser.parse_args()

    count = 5 if args.test else max(args.count, 1)

    root = tk.Tk()
    root.withdraw()  # hide main window

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    schedule_popups(root, count, max(args.stagger, 10), screen_w, screen_h)

    # when all popups are scheduled, start the mainloop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
