class display:
    def __init__(self,tk,window):
        self.tk = tk
        self.window = window
        self.tree = {"window": window, "children":{}}

    def __setup_window(self):
        self.tree['window'].title('自動產生勤務表 APP')
        self.tree['window'].geometry('200x100')
        self.tree['window'].configure(background='white')
    
    def __setup_home_frame(self):
        home_frame = self.tk.Frame(self.tree['window'])
        home_frame.configure(background='white')
        home_frame.pack()
        self.tree["children"]["home_frame"] = home_frame
        self.tree["children"]["children"] = {}

    def __setup_home_frame_btn(self,router):
        setting_btn =self.tk.Button(self.tree["children"]["home_frame"], text='設定',command=router.navigate_setting)
        setting_btn.pack(pady=10)
        gen_btn = self.tk.Button(self.tree["children"]["home_frame"], text='產生勤務表',command=router.navigate_gen)
        gen_btn.pack()
        self.tree["children"]["children"] = {"setting_btn":setting_btn, "gen_btn":gen_btn,"children":{}}

    def setup_home(self,router):
        self.__setup_window()
        self.__setup_home_frame()
        self.__setup_home_frame_btn(router)

    