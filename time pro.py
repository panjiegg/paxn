#二、添加节气信息（如果需要较复杂的计算，可以使用第三方库如 ephem ）

#假设已知一些特定日期的节气，可以通过手动判断来添加节气信息。

import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk


def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    root.after(1000, update_time)


def close_window():
    root.destroy()


root = tk.Tk()
root.title("实时时间显示")

# 加载背景图片
image = Image.open("pjh.jpg")  # 替换成你的背景图片路径
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

time_label = tk.Label(root, text="", font=("Helvetica", 24))
time_label.pack(pady=20)

date_label = tk.Label(root, text="", font=("Helvetica", 16))
date_label.pack(pady=10)

# 添加关闭按钮
close_button = tk.Button(root, text="关闭", command=close_window)
close_button.pack()

update_time()


# 更新日期标签并添加节气信息（假设判断）
def update_date():
    current_date = datetime.now()
    date_str = current_date.strftime('%Y-%m-%d %A')
    if current_date.month == 2 and current_date.day == 4:
        date_str += " 立春"
    elif current_date.month == 5 and current_date.day == 5:
        date_str += " 立夏"
    elif current_date.month == 8 and current_date.day == 7:
        date_str += " 立秋"
    elif current_date.month == 11 and current_date.day == 7:
        date_str += " 立冬"
    date_label.config(text=date_str)
    root.after(86400000, update_date)


update_date()

root.mainloop()

