import tkinter as tk
from tkinter import filedialog
import pygame

# 初始化Pygame
pygame.mixer.init()

def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# 创建主窗口
root = tk.Tk()
root.title("音乐播放器")

# 创建播放按钮
play_button = tk.Button(root, text="播放音乐", command=play_music)
play_button.pack()

# 运行主循环
root.mainloop()