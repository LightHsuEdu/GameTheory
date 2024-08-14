# -*- coding: utf-8 -*-
                                           
#  Shapley Value Calculator

import tkinter as tk
from tkinter import scrolledtext 
from itertools import combinations
import re
import math

# 联盟组合
def generateCoalitions(n_players: int):
    _players = [str(i+1) for i in range(n_players)]
    #_players = list(range(1, numPlayers + 1))
    _coalitions = [list(j) for i in range(len(_players)) for j in combinations(_players, i+1)]
    return _players, _coalitions

# 标准模式 输入 characteristic values
def formForInputCoalitionsValue():    
    try:
        numPlayers = int(standardMode_entry.get())

        for _child in scrollable_frame.winfo_children():
            _child.destroy()

        players, coalitions_list = generateCoalitions(numPlayers)

        global std_entries
        std_entries = []

        for _coalition in coalitions_list:
            std_label_text = str(_coalition) + ' : '
            std_label_text = std_label_text.replace("[", "{ ").replace("]", " }")
            coal_label = tk.Label(scrollable_frame, text=std_label_text, font="-family {Arial} -size 12")
            coal_label.grid(row=len(std_entries), column=0, padx=5, pady=5, sticky=tk.W)

            coal_entry = tk.Entry(scrollable_frame, validate="key", validatecommand=validation_pos_cmd, width=20, font="-family {Arial} -size 12")
            coal_entry.grid(row=len(std_entries), column=1, padx=5, pady=5)
   
            std_entries.append(coal_entry)
    except ValueError:
        for _child in scrollable_frame.winfo_children():
            _child.destroy()        
        err_info_label = tk.Label(scrollable_frame, text="\n输入错误！\n\n只能输入正整数", font="-size 12")
        err_info_label.pack(padx=5, pady=5, side=tk.LEFT)

# 夏普利值
def calculateShapleyValues(n_players: int, characteristic_values):
    all_players, all_combinations = generateCoalitions(n_players)    
    shapley_values = []
    
    for player in all_players:
        shapley_value = 0
        for i in range(len(all_combinations)):
            if player in all_combinations[i]:
                continue
            Cui = sorted(all_combinations[i] + [player])
            k = all_combinations.index(Cui)
            l = i
            numerator = (characteristic_values[k] - characteristic_values[l]) * math.factorial(len(all_combinations[i])) * math.factorial(len(all_players) - len(all_combinations[i]) - 1)
            denominator = math.factorial(len(all_players))
            shapley_value += numerator / denominator
        temp_numerator = characteristic_values[all_players.index(player)] * math.factorial(0) * math.factorial(len(all_players) - 1)
        temp_denominator = math.factorial(len(all_players))
        shapley_value += temp_numerator / temp_denominator
        shapley_values.append([f"   Player {player} : ", shapley_value])
    return shapley_values

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(0)

def validate_positive_number(input_string):
    pattern = r'^[0-9\.\/]*$'
    return re.match(pattern, input_string) is not None

def on_positive_validate(d, i, P, s, S, v, V, W):
    if not P or validate_positive_number(P):
        return True
    return False

def validate_positive_integer(input_string):
    pattern = r'^\d+$'
    return re.match(pattern, input_string) is not None

def on_positive_integer_validate(d, i, P, s, S, v, V, W):
    if not P or validate_positive_integer(P):
        return True
    return False

def validate_number(input_string):
    pattern = r'^[0-9\.\/\- ]*$'
    return re.match(pattern, input_string) is not None

def on_validate(d, i, P, s, S, v, V, W):
    return validate_number(P)

# Radiobutton value
def showRadiobuttonChoice():
    pass

def stringConvertToNumber(_Str):
    try:
        return int(_Str)
    except ValueError:
        try:
            return float(_Str)
        except ValueError:
            infoText_area.delete(1.0, "end")
            infoText_area.insert(tk.END, "输入错误", 'infoTextAlign')
            infoText_area.see('end')
            return None
        
# 开始计算
def startCalculateWork():     
    _Radio_btn = selected_Radiobtn_Var.get()
    if _Radio_btn == " 简单模式 ":
        _simple_args_str = simpleMode_entry.get()
        _simple_args_str = _simple_args_str.strip()
        _simple_args_str = re.sub(r'\s+', ' ', _simple_args_str)

        string_lists = _simple_args_str.split()
        value_ready_list = [stringConvertToNumber(_itm) for _itm in string_lists]        
        if isinstance(value_ready_list[0], int):
            simple_nPlayers = value_ready_list.pop(0)
            simple_ch_values = value_ready_list
            _result = calculateShapleyValues(simple_nPlayers, simple_ch_values)
            _text_to_show = "Shapley values:\n"
            for i_sv in _result:
                _text_to_show += ' '.join([str(elem) for elem in i_sv])
                _text_to_show += "\n"
            infoText_area.delete(1.0, "end")
            infoText_area.insert(tk.END, _text_to_show, 'infoTextAlign')
        else:
            infoText_area.delete(1.0, "end")
            infoText_area.insert(tk.END, "输入错误", 'infoTextAlign')
            infoText_area.see('end')
    elif _Radio_btn == " 标准模式 ":
        global std_entries
        std_entries_str = [_itm.get() for _itm in std_entries]
        if any(not item for item in std_entries_str):
            infoText_area.delete(1.0, "end")
            infoText_area.insert(tk.END, "输入错误", 'infoTextAlign')
            infoText_area.see('end')
        else:
            stand_nPlayers = int(standardMode_entry.get())
            stand_ch_values = [stringConvertToNumber(_itm) for _itm in std_entries_str]
            _result = calculateShapleyValues(stand_nPlayers, stand_ch_values)
            _text_to_show = "Shapley values:\n"
            for i_sv in _result:
                _text_to_show += ' '.join([str(elem) for elem in i_sv])
                _text_to_show += "\n"
            infoText_area.delete(1.0, "end")
            infoText_area.insert(tk.END, _text_to_show, 'infoTextAlign')       
    else:
        pass
    
# tkinter GUI

global std_entries
std_entries = []

global simple_str
simple_str = ""
        
# Main TK window
rootWindow = tk.Tk()
rootWindow.title("Shapley Value Calculator")
rootWindow.geometry("1000x600")

my_frame = tk.Frame(rootWindow)
my_frame.pack(padx=20,pady=20, fill=tk.BOTH)
my_frame.pack_configure(anchor=tk.CENTER)

# 验证输入是否有效
validation_pos_cmd = (rootWindow.register(on_positive_validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
validation_int_cmd = (rootWindow.register(on_positive_integer_validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
validation_cmd = (rootWindow.register(on_validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

selected_Radiobtn_Var = tk.StringVar(value=" 简单模式 ")

simpleMode_frame = tk.Frame(my_frame, borderwidth=1, relief=tk.RIDGE)
simpleMode_frame.pack(padx=10, pady=10, fill="x", expand=True)

simpleMode_radio_button = tk.Radiobutton(simpleMode_frame, text=" 简单模式 ",
                                                                         variable=selected_Radiobtn_Var, value=" 简单模式 ",
                                                                         command=showRadiobuttonChoice, font="-family {Arial, SimSun} -weight normal -size 12")
simpleMode_radio_button.pack(padx=5,pady=10, side=tk.LEFT)
  
simpleMode_entry = tk.Entry(simpleMode_frame, validate="key", validatecommand=validation_cmd, font="-family {Arial} -weight normal -size 12")
# 输入格式
'''
顺序输入 n_players: int, characteristic_values，空格分隔
以 n_players=3 为例，characteristic_values 顺序为 {1} {2} {3} {1, 2} {1, 3} {2, 3} {1, 2, 3} 
'''
simpleMode_entry.insert(tk.END, "3 6 12 42 12 42 42 42")
simpleMode_entry.pack(padx=10, pady=10, side=tk.LEFT, fill="x", expand=True)

grid_frame = tk.Frame(my_frame, borderwidth=0)
grid_frame.pack(padx=0, pady=0, fill="both", expand=True)

gridTL_frame = tk.Frame(grid_frame, borderwidth=0)
gridTL_frame.grid(row=0, column=0, sticky="nsew")
gridTM_frame = tk.Frame(grid_frame, width=0, borderwidth=0)
gridTM_frame.grid(row=0, column=1, sticky="ew")
gridTR_frame = tk.Frame(grid_frame,  borderwidth=0)
gridTR_frame.grid(row=0, column=2, sticky="nsew")

gridML_frame = tk.Frame(grid_frame, borderwidth=0)
gridML_frame.grid(row=1, column=0, sticky="ew")
gridMM_frame = tk.Frame(grid_frame, width=0, height=0, borderwidth=0)
gridMM_frame.grid(row=1, column=1, sticky="ew")
gridMR_frame = tk.Frame(grid_frame,  borderwidth=0)
gridMR_frame.grid(row=1, column=2, sticky="ew")

gridBL_frame = tk.Frame(grid_frame, borderwidth=1, relief=tk.RIDGE)
gridBL_frame.grid(row=2, column=0, padx=10, sticky="nsew")
gridBM_frame = tk.Frame(grid_frame, width=0, borderwidth=0)
gridBM_frame.grid(row=2, column=1, sticky="nsew")
gridBR_frame = tk.Frame(grid_frame,  borderwidth=1, relief=tk.RIDGE)
gridBR_frame.grid(row=2, column=2, padx=10, sticky="nsew")

grid_frame.columnconfigure(2, weight=1)
grid_frame.rowconfigure(1, weight=1)

standardMode_frame = tk.Frame(gridTL_frame,  borderwidth=1, relief=tk.RIDGE)
standardMode_frame.pack(padx=10, pady=10, side=tk.TOP, fill="x", expand=True)

standardMode_radio_button = tk.Radiobutton(standardMode_frame, text=" 标准模式 ",
                                                                         variable=selected_Radiobtn_Var, value=" 标准模式 ",
                                                                         command=showRadiobuttonChoice, font="-family {Arial, SimSun} -weight normal -size 12")
standardMode_radio_button.pack(padx=5,pady=10, side=tk.LEFT)

standardMode_entry = tk.Entry(standardMode_frame, validate="key", validatecommand=validation_int_cmd, font="-family {Arial} -weight normal -size 12")
standardMode_entry.insert(tk.END, "3")
standardMode_entry.pack(padx=10, pady=10, side=tk.LEFT)

generateCoal_btn = tk.Button(standardMode_frame, text=" 联盟组合 ", command=formForInputCoalitionsValue, font="-family {Arial, SimSun} -weight normal -size 12")
generateCoal_btn.pack(padx=20, pady=10, side=tk.LEFT)

run_frame = tk.Frame(gridTR_frame, borderwidth=0)
run_frame.pack(padx=10, pady=10, fill="both", expand=True)

run_btn = tk.Button(run_frame, text=" 计算 ", command=startCalculateWork, font="-family {Arial, SimSun} -weight bold -size 14")
run_btn.pack(fill="both", expand=True)

canvas = tk.Canvas(gridBL_frame, highlightthickness=0)
scrollbar = tk.Scrollbar(gridBL_frame, orient='vertical', command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", on_canvas_configure)

canvas.create_window((0, 0), window=scrollable_frame, anchor='center')
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

infoText_area = scrolledtext.ScrolledText(gridBR_frame, padx=10, pady=0)
infoText_area.configure(wrap="word") 
infoText_area.configure(bd=0) 

infoText_area.configure(font="-family {Arial} -weight bold -size 14")
infoText_area.tag_configure('infoTextAlign', justify='left', rmargin=10, spacing1=10, spacing2=5, spacing3=5)
infoText_area.pack(padx=10, pady=10)

statusInfo_text = ""

infoText_area.insert(tk.END, statusInfo_text, 'infoTextAlign')
infoText_area.see('end')

rootWindow.mainloop()
