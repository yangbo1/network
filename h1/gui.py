import hammingCode
from tkinter import *
import random




class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name#设置窗口


    def set_init_window(self):
        self.init_window_name.title("海明码编解码工具")           #窗口名
        self.init_window_name.geometry('650x550')

        # 标签
        self.init_data_label1 = Label(self.init_window_name, text="输入二进制报文")
        self.init_data_label1.grid(row=1, column=10)
        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=50, height=4)
        self.init_data_Text.grid(row=10, column=10)

        # 按钮
        self.encode_button = Button(self.init_window_name, text="编码", bg="lightblue", width=10,
                                              command=self.encode)
        self.encode_button.grid(row=15, column=10)

        self.init_data_label2 = Label(self.init_window_name, text="海明码")
        self.init_data_label2.grid(row=20, column=10)
        self.result_data_Text = Text(self.init_window_name, width=50, height=4)
        self.result_data_Text.grid(row=25, column=10, rowspan=1, columnspan=1)

        self.err_data_Laber = Label(self.init_window_name, text="出错位(多位逗号分隔)")
        self.err_data_Laber.grid(row=25, column=80)

        self.err_data_Text = Text(self.init_window_name, width=15, height=1)
        self.err_data_Text.grid(row=25, column=81)

        self.err_button = Button(self.init_window_name, text="模拟出错", bg="lightblue", width=10,
                                    command=self.err)
        self.err_button.grid(row=26, column=80)

        self.dencode_button = Button(self.init_window_name, text="解码", bg="lightblue", width=10,
                                    command=self.decode)
        self.dencode_button.grid(row=30, column=10)

        self.result_data_Text2 = Text(self.init_window_name, width=50, height=4)
        self.result_data_Text2.grid(row=35, column=10, rowspan=1, columnspan=1)
    def encode(self):
        code = str(self.init_data_Text.get(1.0, END)).strip().replace("\n","")
        # print(code)
        hamming = hammingCode.hamming(code, hammingCode.P(code))
        print(hamming)
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, hamming)
    def err(self):
        code = str(self.init_data_Text.get(1.0, END)).strip().replace("\n","")
        hamming = hammingCode.hamming(code, hammingCode.P(code))
        l = list(hamming)
        err = self.err_data_Text.get(1.0, END).strip().replace("\n", "")
        print('err', err.split(','))
        err = list(err.split(','))
        for i in range(len(err)):
            print(err[i])
            l[int(err[i]) - 1] = str(int(l[int(err[i]) -1]) ^ 1)
        print(''.join(l))
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, ''.join(l))
    def decode(self):
        code = str(self.result_data_Text.get(1.0, END)).strip().replace("\n", "")
        check = hammingCode.check(code)
        print('错位', check)
        decode = hammingCode.decode(code)
        print('解码', decode)
        self.result_data_Text2.delete(1.0, END)
        self.result_data_Text2.insert(1.0, '检错位=' + check + '解码：' + decode)
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()