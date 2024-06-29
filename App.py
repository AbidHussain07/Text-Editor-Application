import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_app = tk.Tk()
main_app.title("My Text Editor -----Made By AbidHussain")
main_app.geometry("1200x800")
main_app.wm_iconbitmap("icon.ico")

# -----------------------------------------------------Main menu-------------------------------------------------------------
main_menu = tk.Menu()
# -----------------------------------------------------File menu-------------------------------------------------------------
file = tk.Menu(main_menu,tearoff=False)
# dropdown list usig icon 
new_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\new.png")
open_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\open.png")
save_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\save.png")
save_as_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\save_as.png")
exit_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\exit.png")

# -----------------------------------------------------Edit menu-------------------------------------------------------------
edit = tk.Menu(main_menu,tearoff=False)
# dropdown list usig icon 
copy_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\copy.png")
paste_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\paste.png")
cut_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\cut.png")
clear_all_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\clear_all.png")
find_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\find.png")

# -----------------------------------------------------View menu----------------------------------------------------
view = tk.Menu(main_menu,tearoff=False)
toolbar_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\tool_bar.png")
statusbar_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\status_bar.png")

# -----------------------------------------------------Color menu----------------------------------------------------
color = tk.Menu(main_menu,tearoff=False)
# dropdown list usig icon 
light_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\light_default.png")
light1_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\light_plus.png")
light2_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\dark.png")
light3_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\red.png")
light4_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\monokai.png")
light5_icon = tk.PhotoImage(file = r"D:\New folder\Project-icons\night_blue.png")

theme_choice = tk.StringVar()
color_icon = (light_icon , light1_icon , light2_icon, light3_icon, light4_icon, light5_icon)
color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color , bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(fg = fg_color , bg = bg_color)


count = 0
for i in color_dict:
    color.add_radiobutton(label=i,image=color_icon[count],compound=tk.LEFT,variable=theme_choice)
    count+=1


# cascade to main_menu
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color",menu=color)
# main_menu.add_cascade(label="File",menu=file)

# ---------------------------------------------------End Main menu-----------------------------------------------------------

# -----------------------------------------------------Toolbar-------------------------------------------------------------
# ---------Font box---------
# print(type(tk.font.families()))-------> Only to see font families type

toolbar = ttk.Label(main_app)
toolbar.pack(side=tk.TOP , fill=tk.X)
# agar humme horizontal fill karna hai toh hum likhte hai [fill = tk.X]
# agar humme vertically fill karna hai toh hum likhte hai [fill = tk.Y]
# agar humme both fill karna hai toh hum likhte hai [fill = tk.BOTH]

font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(toolbar,width=30,height=10,textvariable=font_family ,state="readonly")
font_box['values']= font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0,column=0,padx=5)


# -------size box---------
size_var = tk.IntVar()
size_box = ttk.Combobox(toolbar,width=4,textvariable=size_var ,state="readonly")
size_box['values'] = tuple(range(8,71,2))
size_box.current(2)
size_box.grid(row=0,column=1,padx=5)

#------------------Bold Button-------------
bold_icon = tk.PhotoImage(file=r"D:\New folder\Project-icons\bold.png")
bold_btn = ttk.Button(toolbar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#------------------Italic Button-------------
italic_icon = tk.PhotoImage(file=r"D:\New folder\Project-icons\italic.png")
italic_btn = ttk.Button(toolbar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

#------------------Underline Button-------------
underline_icon = tk.PhotoImage(file=r"D:\New folder\Project-icons\underline.png")
underline_btn = ttk.Button(toolbar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# ----------------font color Button-------------
font_color_icon = tk.PhotoImage(file=r"D:\New folder\Project-icons\font_color.png")
font_color_btn = ttk.Button(toolbar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

# ----------------Align left Button-------------
align_left_icon = tk.PhotoImage(file=r"D:\New folder\Project-icons\align_left.png")
align_left_btn = ttk.Button(toolbar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

# ----------------Align center button-------------
align_center_icon = tk.PhotoImage(file=r"D:\New folder\Project-icons\align_center.png")
align_center_btn = ttk.Button(toolbar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

# ----------------Align Right Button-------------
align_right_icon = tk.PhotoImage(file=r"D:\New folder\Project-icons\align_right.png")
align_right_btn = ttk.Button(toolbar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

# ---------------------------------------------------End Toolbar-----------------------------------------------------------

# -----------------------------------------------------Text Editor------------------------------------------------------------
text_editor = tk.Text(main_app)
text_editor.config(wrap="word",relief=tk.FLAT)

scrool_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scrool_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scrool_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrool_bar.set)

# font family and font size 
current_fontfamily = 'Arial'
current_fontsize = 12
def change_font(main_app):
    global current_fontfamily
    current_fontfamily = font_family.get()
    text_editor.configure(font=(current_fontfamily,current_fontsize))

def change_size(main_app):
    global current_fontsize
    current_fontsize = size_var.get()
    text_editor.configure(font=(current_fontfamily,current_fontsize))

font_box.bind("<<ComboboxSelected>>",change_font)
size_box.bind("<<ComboboxSelected>>",change_size)

# -----------Button Functionality-----------------
# Bold Button 
def bold_func():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_fontfamily,current_fontsize,'bold'))
    else:
        text_editor.configure(font=(current_fontfamily,current_fontsize,'normal'))

bold_btn.configure(command=bold_func)

#Italic Button
def italic_func():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_fontfamily,current_fontsize,'italic'))
    else:
        text_editor.configure(font=(current_fontfamily,current_fontsize,'roman'))

italic_btn.configure(command=italic_func)

#Underline Button
def underline_func():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_fontfamily,current_fontsize,'underline'))
    else:
        text_editor.configure(font=(current_fontfamily,current_fontsize,'normal'))

underline_btn.configure(command=underline_func)

# Color Button
def color_func():
    color_var = colorchooser.askcolor()
    text_editor.configure(fg=color_var[1]) 
#when we select the color it wil be in form of--->((180, 84, 237), '#b454ed'). We want hexa-code thatswhy we have given index [1]
#we have used askcolor() function to select the color from the color palette
font_color_btn.configure(command=color_func)

# Aliign Left
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

# Align Center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)  

# Align Right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)  

text_editor.configure(font=('Arial',12))
# ---------------------------------------------------End Main menu-----------------------------------------------------------

# -----------------------------------------------------Main Status Bar-------------------------------------------------------------
status_bar = ttk.Label(main_app,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_modified = False
def modified(event=None):#---> bracket mai aap kuch bhi likh sakte hai
    global text_modified
    if text_editor.edit_modified():
        text_modified = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c').replace(' ',''))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)
    
text_editor.bind("<<Modified>>",modified)
# ---------------------------------------------------End Main Status Bar-----------------------------------------------------------

# -----------------------------------------------------Main menu functionality-------------------------------------------------------------
# Empty Variable for File Sub-Menu
url = ''
# To Create New File----> Fnctionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

# To open File----> Fnctionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(f"{url} ---Text Editor"))

# To Save File----> Fnctionality
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

# To Save As File----> Fnctionality
def save_as_file(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return
    
# To Exit ---> functionality
def exit_func(event=None):
    global url,text_modified
    try:
        if text_modified:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save your work?') #askyesnocancel() is used to ask question with yes/no/cancel option
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
            # elif mbox is None:
            #     return
        else:
            main_app.destroy()
    except:
        return          

# Adding command to file Sub-Menu
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)
file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)
file.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)
file.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+S",command=save_as_file)
file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Q",command=exit_func)

# To Find ---> Functionality 
def find_func(event=None):

    def find():
        word = text_find_entry.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True: #while loop is used to find the word in the text
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = text_find_entry.get()
        replace_text = text_replace_entry.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x150+400+100')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)  #---> means user cannot minimize or maximize
    #frame
    find_frame = ttk.LabelFrame(find_dialog,text="Find/Replace ")
    find_frame.pack(pady=10)
    #label
    text_find_label = ttk.Label(find_frame,text="Find : ")
    text_find_label.grid(row=0,column=0,padx=5,pady=5)
    text_replace_label = ttk.Label(find_frame,text="Replace : ")
    text_replace_label.grid(row=1,column=0,padx=5,pady=5)
    #entry
    text_find_entry = ttk.Entry(find_frame,width=30)
    text_find_entry.grid(row=0,column=1,padx=5,pady=5)
    text_replace_entry = ttk.Entry(find_frame,width=30)
    text_replace_entry.grid(row=1,column=1,padx=5,pady=5)
    #button
    find_button = ttk.Button(find_frame,text="Find",width=15,command=find)
    find_button.grid(row=2,column=0,padx=10,pady=5)
    replace_button = ttk.Button(find_frame,text="Replace",width=15,command=replace)
    replace_button.grid(row=2,column=1,padx=5,pady=10)

    find_frame.mainloop()

# Adding command to Edit Sub-Menu
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+X",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F", command=find_func)

# Adding command to View Sub-Menu
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        show_toolbar = True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar = True


view.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,image=toolbar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="Satus Bar",onvalue=1,offvalue=False,image=statusbar_icon,compound=tk.LEFT,command=hide_statusbar)


# ---------------------------------------------------End Main menu functionality-----------------------------------------------------------

main_app.config(menu=main_menu)

# Binding Shortcut keys 
main_app.bind("<Control-n>",new_file)
main_app.bind("<Control-o>",open_file)
main_app.bind("<Control-s>",save_file)
main_app.bind("<Control-Alt-s>",save_as_file)
main_app.bind("<Control-q>",exit_func)
main_app.bind("<Control-f>",find_func)

main_app.mainloop()