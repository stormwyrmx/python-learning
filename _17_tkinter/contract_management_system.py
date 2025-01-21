import tkinter as tk
from tkinter import ttk, messagebox

class ContractManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("合同管理档案表")

        # 创建表格
        columns = ("合同编号", "客户名称", "签订时间", "合同标的", "合同数量",
                   "应履行时间", "实际履行时间", "应履行金额", "实际履行金额")

        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        self.tree.pack(pady=20, padx=20, fill="both", expand=True)

        # 按钮布局
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="新增合同", command=self.open_add_contract_window).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="修改合同", command=self.open_edit_contract_window).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="删除合同", command=self.delete_contract).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="查询合同", command=self.search_contracts).grid(row=0, column=3, padx=10)
        tk.Button(btn_frame, text="退出", command=root.quit).grid(row=0, column=4, padx=10)

    def open_add_contract_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("新增合同")

        fields = ["合同编号", "客户名称", "签订时间", "合同标的", "合同数量", "应履行时间", "实际履行时间",
                  "应履行金额", "实际履行金额"]
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(add_window, text=field).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry

        tk.Button(add_window, text="保存", command=lambda: self.save_contract(entries, add_window)).grid(
            row=len(fields), column=0, columnspan=2, pady=10)

    def open_edit_contract_window(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("修改合同")

        tk.Label(edit_window, text="请输入合同编号：").grid(row=0, column=0, padx=10, pady=5)
        contract_id_entry = tk.Entry(edit_window)
        contract_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(edit_window, text="查询",
                  command=lambda: self.show_contract_details(contract_id_entry.get(), edit_window)).grid(row=0,
                                                                                                         column=2,
                                                                                                         padx=10,
                                                                                                         pady=5)

    def save_contract(self, entries, window):
        # 这里可以加入校验逻辑
        values = [entry.get() for entry in entries.values()]
        self.tree.insert("", "end", values=values)
        messagebox.showinfo("提示", "合同已添加成功！")
        window.destroy()

    def delete_contract(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            messagebox.showinfo("提示", "合同已删除！")
        else:
            messagebox.showwarning("警告", "请先选择一个合同！")

    def search_contracts(self):
        messagebox.showinfo("提示", "功能暂未实现")

    def show_contract_details(self, contract_id, window):
        messagebox.showinfo("提示", f"查询合同编号：{contract_id}，功能待实现")
        window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ContractManagementApp(root)
    root.mainloop()
