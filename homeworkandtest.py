import tkinter as tk
from tkinter import filedialog
from tkinter import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="both", expand=True)
        self.text = tk.Text(self)
        self.text.pack(fill="both", expand =True)
        
    def show(self):
        self.lift()

def file_save():
    f=filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: 
        return
    
    txt_content = []
    for page in PAGES:
        
        txt_connect = page.text.get(1.0, END)
        pg_name = page.winfo_class()
        label_text = page.label.cget("text")
        txt_content.append(f"Label: {label_text}\n")
        txt_content.append(f"Content from {pg_name}:\n")
        txt_content.append(txt_connect)
        txt_content.append("===")

    f.write("\n".join(txt_content))
    f.close()

def open_file():
    f=filedialog.askopenfile(mode='r', filetypes=[("text file")])
    if f is None:
        return
    content=f.read()
    pages_content=content.split("===")

    for page in PAGES:
        page.text.delete("1.0", END)
        pg_name=page.winfo_class()
        content_found = False

        for content_section in pages_content:
            if f"Content from {pg_name}:" in content_section:
                page.text.insert(END, content_section)
                content_found=True
                break
        if not content_found:
            page.text.insert("1.0", f"Content from {pg_name}:\n")

    f.close()

class Monday(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label.config(text="Monday's Schedule")

class Tuesday(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label.config(text="Tuesday's Schedule")

class Wednesday(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label.config(text="Wednesday's Schedule")

class Thursday(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label.config(text="Thursday's Schedule")

class Friday(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label.config(text="Friday's Schedule")

class Saturday(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label.config(text="Saturday's Schedule")

class Sunday(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label.config(text="Sunday's Schedule")

class MainView(tk.Frame):
    def __init__(self, *args, **kwarggs):
        tk.Frame.__init__(self, *args, **kwarggs)
        global PAGES
        PAGES = [Monday(self), Tuesday(self), Wednesday(self), Thursday(self), Friday(self), Saturday(self), Sunday(self)]

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        for page in PAGES:
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Monday", command=lambda: PAGES[0].show())
        b2 = tk.Button(buttonframe, text="Tuesday", command=lambda: PAGES[1].show())
        b3 = tk.Button(buttonframe, text="Wednesday", command=lambda: PAGES[2].show())
        b4 = tk.Button(buttonframe, text="Thursday", command=lambda: PAGES[3].show())
        b5 = tk.Button(buttonframe, text="Friday", command=lambda: PAGES[4].show())
        b6 = tk.Button(buttonframe, text="Saturday", command=lambda: PAGES[5].show())
        b7 = tk.Button(buttonframe, text="Sunday", command=lambda: PAGES[6].show())
        save_button = tk.Button(buttonframe, text="Save", command=file_save)
        open_button = tk.Button(buttonframe, text="Open", command=open_file)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        b7.pack(side="left")
        save_button.pack(side="left")
        open_button.pack(side="left")

        PAGES[0].show()

if __name__ == "__main__":
    root=tk.Tk()
    main=MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("465x400")
    root.mainloop()