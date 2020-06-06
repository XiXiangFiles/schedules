class display:
    def __init__(self,tk,window):
        self.tk = tk
        self.window = window
    def setup_home(self,router):
        window = self.window
        tk = self.tk
        home_frame = tk.Frame(window)
        home_frame.configure(background='white')
        home_frame.pack()
        window.title('自動產生勤務表 APP')
        window.geometry('200x100')
        window.configure(background='white')
        setting_btn = tk.Button(home_frame, text='設定',command=router.navigate_setting)
        setting_btn.pack(pady=10)
        gen_btn = tk.Button(home_frame, text='產生勤務表',command=router.navigate_gen)
        gen_btn.pack()

    