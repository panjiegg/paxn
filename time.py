import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk


def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    label.config(text=current_time)
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

label = tk.Label(root, text="", font=("Helvetica", 24))
label.pack(pady=20)

# 添加关闭按钮
close_button = tk.Button(root, text="关闭", command=close_window)
close_button.pack()

update_time()

root.mainloop()
