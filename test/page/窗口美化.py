import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#实例化创建应用程序窗口
root = ttk.Window(
        title="窗口名字",        #设置窗口的标题
        themename="litera",     #设置主题
        size=(500,300),        #窗口的大小
        position=(100,100),     #窗口所在的位置
        alpha=1.0,              #设置窗口的透明度(0.0完全透明）
        )

root.place_window_center()    #让显现出的窗口居中
root.resizable(False,False)   #让窗口不可更改大小
# root.wm_attributes('-topmost', 1)#让窗口位置其它窗口之上

ttk.Button(root, text="Button 1",
           bootstyle=SUCCESS).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 2",
           bootstyle=(INFO, OUTLINE)).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 3",
           bootstyle=(PRIMARY,
                      "outline-toolbutton")).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 4",
           bootstyle="link").pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 5",
           bootstyle="success-link").pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 6",
           state="disabled").pack(side=LEFT, padx=5, pady=10) #在禁用状态下创建按钮

root.mainloop()
