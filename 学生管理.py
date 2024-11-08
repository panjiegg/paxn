class SearchFrame(tk.Frame):
    # 这里创建的类就是一个frame
    def __init__(self,master):
        self.master = master
        super().__init__(self.master)
        self.stu_list = data.load_data()
        self.create_widget()
    def create_widget(self):
        # 给frame里添加组件
        self.wraper = tk.LabelFrame(self,text="查询学生信息", height = 300)
        self.wraper.pack()
        self.scrollbar = tk.Scrollbar(self.wraper,)
        self.tree = ttk.Treeview(self.wraper,columns=("1","2","3","4","5","6","7","8"),show="headings",height=10)
        self.tree.pack(pady=10)
        self.scrollbar.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scrollbar.set)
        # 设置各列的宽度和对齐方式
        self.tree.column("1", width=50, anchor="center")
        self.tree.column("2", width=80, anchor="center")
        self.tree.column("3", width=50, anchor="center")
        self.tree.column("4", width=60, anchor="center")
        self.tree.column("5", width=120, anchor="center")
        self.tree.column("6", width=100, anchor="center")
        self.tree.column("7", width=100, anchor="center")
        self.tree.column("8", width=170, anchor="center")        # w表示左对齐，e表示右对齐
        # 设置表头
        self.tree.heading("1", text="学号", )
        self.tree.heading("2", text="姓名", )
        self.tree.heading("3", text="性别", )
        self.tree.heading("4", text="年龄", )
        self.tree.heading("5", text="班级", )
        self.tree.heading("6", text="系别", )
        self.tree.heading("7", text="电话", )
        self.tree.heading("8", text="地址", )
        # self.stu_list.append()
        # data.save_data(self.stu_list)
        self.keyword_label = tk.Label(self, text="查询关键字：", pady=30)
        self.keyword_label.pack(side="left")
        self.keyword_entry = tk.Entry(self)
        self.keyword_entry.pack(side="left", padx=10)
        self.search_btn = tk.Button(self, text="查询", command=self.search_stu)
        self.search_btn.pack(side="right")
    def show_message(self):
        self.stu_list = data.load_data()
        # 清空tree中原本含有的所有数据，防止出错
        result = self.tree.get_children()
        self.tree.delete(*result)
        # 将学生信息全部添加到tree中
        for i in self.stu_list:
            self.tree.insert("", "end", values=(i["id"], i["name"], i["gender"], i["age"], i["class"],
                                                i["department"], i["mobile"],
                                                (i["province"] + i["city"] + i["county"] + i["address"])))
    def search_stu(self):
            # 首先获取关键字
            keyword = self.keyword_entry.get()
            if keyword:
                result = self.tree.get_children()
                # result 所有项的Iid
                # 在展示查询结果前，删除所有的学生
                self.tree.delete(*result)
                # 将符合查询关键字的学生信息添加到tree中
                for i in self.stu_list:
                    if keyword in i['name']:
                        self.tree.insert("", "end", values=(i["id"], i["name"], i["gender"], i["age"], i["mobile"], i["address"]))
try:
    f = open('test.txt', 'r')
    content = f.read()
except FileNotFoundError as e:
    print(f"捕获到异常: {e}")
finally:
    # 关闭文件，确保资源被释放
    if 'f' in locals():
        f.close()
