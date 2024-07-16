import tkinter as tk
import random

# 创建主窗口
root = tk.Tk()
root.title("随机点人")

# 设置窗口大小
root.geometry("400x250") # 增加窗口高度以提供更多空间

# 读取学生名单文件
with open('students.txt', 'r', encoding='utf-8') as file:
     students = file.readlines()

# 去除每行可能的空白字符，如换行符
students = [student.strip() for student in students if student.strip()]  # 过滤掉空行

# 显示选中的学生
selected_text = tk.StringVar()
selected_label = tk.Label(root, textvariable=selected_text, font=("微软雅黑", 18), padx=10, pady=20)
selected_label.pack()

# 创建再次随机选人的按钮
def random_select():
    selected_text.set("随机选人中...")
    root.after(1200, lambda: selected_text.set(f"选中的学生是：{random.choice(students)}"))

reselect_button = tk.Button(root, text="再次随机选人", command=random_select, font=("微软雅黑", 12))
reselect_button.pack(pady=10)

# 添加版权信息
copyright_text = tk.StringVar()
copyright_text.set("轻云网络 @郭师傅 @Xe阿霖 版权所有")
copyright_label = tk.Label(root, textvariable=copyright_text, font=("微软雅黑", 10), justify='right', padx=10)
copyright_label.pack(side='bottom', fill='x')

# 添加版本信息
version_text = tk.StringVar()
version_text.set("Version 1.1.5")
version_label = tk.Label(root, textvariable=version_text, font=("微软雅黑", 10), justify='right', padx=10)
version_label.pack(side='bottom')

# 第一次选人延迟
random_select()

# 运行主循环
root.mainloop()
