"""主题选择功能模块

提供 ttkbootstrap 主题选择和预览功能
"""
import ttkbootstrap as tk
from tkinter import messagebox

class ThemeSelector(tk.Window):
    """
    主题选择窗口类，继承自 ttkbootstrap.Window
    用于选择和预览不同的 ttkbootstrap 主题
    """
    
    def __init__(self):
        try:
            # 默认主题
            default_theme = "litera"
            
            # 初始化窗口
            tk.Window.__init__(self,
                               themename=default_theme,
                               title="主题选择",
                               size=(500, 600),
                               minsize=(500, 600),
                               resizable=None)
            
            # 获取可用主题列表
            self.available_themes = self.get_available_themes()
            
            # 当前选中的主题
            self.current_theme = tk.StringVar(value=default_theme)
            
            # 创建 UI 组件
            self.create_widgets()

        except Exception as e:
            messagebox.showerror("错误", f"主题选择窗口初始化失败：{e}")

    def get_available_themes(self):
        """
        获取 ttkbootstrap 所有可用主题
        
        Returns:
            list: 主题名称列表
        """
        # ttkbootstrap 内置主题
        themes = [
            "litera",      # 浅色主题，蓝白配色
            "minty",       # 浅色主题，薄荷绿配色
            "pulse",       # 浅色主题，紫色配色
            "flatly",      # 浅色主题，扁平化设计
            "journal",     # 浅色主题，暖色调
            "darkly",      # 深色主题
            "cyborg",      # 深色主题，科技感
            "vapor",       # 深色主题，蒸汽波风格
            "superhero",   # 深色主题，超级英雄风格
            "solar",       # 浅色主题，太阳能风格
            "quartz",      # 浅色主题，石英风格
            "zephyr",      # 浅色主题，微风风格
            "lumen",       # 浅色主题，光感风格
        ]
        return themes
    
    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # 标题标签
        title_label = tk.Label(
            main_frame,
            text="请选择主题",
            font=("Arial", 16, "bold"),
            anchor="center"
        )
        title_label.pack(pady=(0, 20))
        
        # 主题选择下拉框
        select_frame = tk.Frame(main_frame)
        select_frame.pack(fill=tk.X, pady=10)
        
        select_label = tk.Label(select_frame, text="主题:", font=("Arial", 12))
        select_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.theme_combo = tk.Combobox(
            select_frame,
            values=self.available_themes,
            textvariable=self.current_theme,
            state="readonly",
            width=20
        )
        self.theme_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.theme_combo.bind("<<ComboboxSelected>>", self.on_theme_change)
        
        # 主题预览区域
        preview_frame = tk.LabelFrame(main_frame, text="主题预览", padding=10)
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # 预览按钮示例
        btn_frame = tk.Frame(preview_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(btn_frame, text="主要按钮", bootstyle="primary").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="成功按钮", bootstyle="success").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="危险按钮", bootstyle="danger").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="警告按钮", bootstyle="warning").pack(side=tk.LEFT, padx=5)
        
        # 轮廓按钮示例
        outline_frame = tk.Frame(preview_frame)
        outline_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(outline_frame, text="主要轮廓", bootstyle="primary-outline").pack(side=tk.LEFT, padx=5)
        tk.Button(outline_frame, text="成功轮廓", bootstyle="success-outline").pack(side=tk.LEFT, padx=5)
        tk.Button(outline_frame, text="危险轮廓", bootstyle="danger-outline").pack(side=tk.LEFT, padx=5)
        tk.Button(outline_frame, text="警告轮廓", bootstyle="warning-outline").pack(side=tk.LEFT, padx=5)
        
        # 输入框示例
        input_frame = tk.Frame(preview_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(input_frame, text="文本输入:").pack(anchor=tk.W)
        tk.Entry(input_frame).pack(fill=tk.X, pady=5)
        
        # 复选框和单选按钮
        check_frame = tk.Frame(preview_frame)
        check_frame.pack(fill=tk.X, pady=5)
        
        tk.Checkbutton(check_frame, text="复选框 1").pack(side=tk.LEFT, padx=10)
        tk.Checkbutton(check_frame, text="复选框 2").pack(side=tk.LEFT, padx=10)
        
        # 进度条示例
        progress_frame = tk.Frame(preview_frame)
        progress_frame.pack(fill=tk.X, pady=10)
        
        progress = tk.Progressbar(progress_frame, mode="indeterminate")
        progress.pack(fill=tk.X)
        progress.start(10)
        
        # 底部按钮区域
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # 应用按钮
        apply_btn = tk.Button(
            button_frame,
            text="应用主题",
            command=self.apply_theme,
            bootstyle="primary",
            width=15
        )
        apply_btn.pack(side=tk.LEFT, padx=5)
        
        # 重置按钮
        reset_btn = tk.Button(
            button_frame,
            text="重置",
            command=self.reset_theme,
            bootstyle="warning",
            width=15
        )
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        # 关闭按钮
        close_btn = tk.Button(
            button_frame,
            text="关闭",
            command=self.destroy,
            bootstyle="danger-outline",
            width=15
        )
        close_btn.pack(side=tk.RIGHT, padx=5)
    
    def on_theme_change(self, event=None):
        """
        主题改变时的回调函数
        
        Args:
            event: 事件对象（可选）
        """
        selected_theme = self.current_theme.get()
    
    def apply_theme(self):
        """应用选中的主题"""
        try:
            selected_theme = self.current_theme.get()
            
            # 更新窗口主题
            self.style.theme_use(selected_theme)

            # 显示提示信息
            from tkinter import messagebox
            messagebox.showinfo("主题已应用", f"主题已成功更改为：{selected_theme}\n\n注意：此更改仅在当前窗口生效。")
            
        except Exception as e:
            error_msg = f"应用主题失败：{str(e)}"

            messagebox.showerror("错误", error_msg)
    
    def reset_theme(self):
        """重置主题为默认值"""
        try:
            default_theme = "litera"
            self.current_theme.set(default_theme)
            self.style.theme_use(default_theme)

        except Exception as e:
            pass


if __name__ == '__main__':
    theme_selector = ThemeSelector()
    theme_selector.mainloop()