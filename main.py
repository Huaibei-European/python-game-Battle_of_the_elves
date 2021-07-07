import random
import string
import time
import tkinter as tk
from tkinter import ttk, messagebox
from Wizard_Information import proxy
import threading

who = 1
root = tk.Tk()
root.title('精灵大作战')
root.attributes("-topmost", True)
root.geometry("410x260+850+30")
root.resizable(0, 0)
root.iconbitmap("favicon.ico")

select_tree_wizard1_var = tk.StringVar()
select_tree_wizard2_var = tk.StringVar()
show_animate_var = tk.StringVar()
show_state_label1_var = tk.StringVar()
show_active1_var = tk.StringVar()
show_state_label2_var = tk.StringVar()
show_active2_var = tk.StringVar()
show_state_label1_var.set('当前状态')
show_active1_var.set('效果')
show_state_label2_var.set('当前状态')
show_active2_var.set('效果')
show_animate_var.set(''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 6)))

frame = tk.Frame(root)
select_elves_button = tk.Button(frame, text='选择精灵')
select_tree_wizard1 = ttk.Combobox(frame, textvariable=select_tree_wizard1_var,
                                   values=('辛迪拉', '风沁', '玛格', '金轮赤乌', '学神'), state="readonly")
select_tree_wizard2 = ttk.Combobox(frame, textvariable=select_tree_wizard2_var,
                                   values=('辛迪拉', '风沁', '玛格', '金轮赤乌', '学神'), state="readonly")
select_tree_wizard1_var.set('选择甲方精灵')
select_tree_wizard2_var.set('选择乙方精灵')

frame.pack()
select_elves_button.grid(row=1, column=1, columnspan=2, pady=15)
select_tree_wizard1.grid(row=2, column=1, padx=10)
select_tree_wizard2.grid(row=2, column=2, padx=10)

player_1 = ''
player_2 = ''
player_1obj = ''
player_2obj = ''
hp_show_player1 = ''
hp_show_player2 = ''
frame2 = ''
skill_player_1_button1 = ''
skill_player_1_button2 = ''
skill_player_1_button3 = ''
skill_player_1_button4 = ''
skill_player_2_button1 = ''
skill_player_2_button2 = ''
skill_player_2_button3 = ''
skill_player_2_button4 = ''
bout = 2
attack_value_temp = ''
thread_show = ''


def select_wizard():
    global player_1, player_2, player_1obj, player_2obj
    import wizard_process
    player_1 = select_tree_wizard1_var.get()  # 玩家1的精灵名称
    player_2 = select_tree_wizard2_var.get()  # 玩家2的精灵名称
    player_1obj = proxy.get(wizard_process.Chinese_to_English(player_1))()  # 玩家1的精灵实例化对象
    player_2obj = proxy.get(wizard_process.Chinese_to_English(player_2))()  # 玩家2的精灵实例化对象
    frame.destroy()
    play_against()


def play_against():
    global hp_show_player1, hp_show_player2, frame2, attack_value_temp
    global skill_player_1_button1
    global skill_player_1_button2
    global skill_player_1_button3
    global skill_player_1_button4
    global skill_player_2_button1
    global skill_player_2_button2
    global skill_player_2_button3
    global skill_player_2_button4
    attack_value_temp = {
        'player1_end_attack': abs(player_1obj.attack - player_2obj.defense) * 0.3,
        'player1_normal_attack': abs(player_1obj.attack - player_2obj.defense) * 0.3,
        'player2_end_attack': abs(player_2obj.attack - player_1obj.defense) * 0.3,
        'player2_normal_attack': abs(player_2obj.attack - player_1obj.defense) * 0.3,
    }
    print(attack_value_temp)
    thread_show = threading.Thread(target=modify_show)
    thread_show.start()
    frame2 = tk.Frame(root)
    frame2.pack()
    player_1_config_label = tk.Label(frame2, text='甲方精灵')
    player_2_config_label = tk.Label(frame2, text='乙方精灵')
    hp_show_player1 = ttk.Progressbar(frame2, value=100)
    hp_show_player2 = ttk.Progressbar(frame2, value=100)
    player_1_name_label = tk.Label(frame2, text=player_1)
    player_2_name_label = tk.Label(frame2, text=player_2)
    frame3 = tk.Frame(frame2)
    frame4 = tk.Frame(frame3)
    frame5 = tk.Frame(frame3)

    skill_player_1_button1 = tk.Button(frame4, text=player_1obj.skill[0], width=10)
    skill_player_1_button2 = tk.Button(frame4, text=player_1obj.skill[1], width=10)
    skill_player_1_button3 = tk.Button(frame4, text=player_1obj.skill[2], width=10)
    skill_player_1_button4 = tk.Button(frame4, text=player_1obj.skill[3], width=10)

    show_animate_label = tk.Label(frame3, textvariable=show_animate_var, width=6)

    skill_player_2_button1 = tk.Button(frame5, text=player_2obj.skill[0], width=10)
    skill_player_2_button2 = tk.Button(frame5, text=player_2obj.skill[1], width=10)
    skill_player_2_button3 = tk.Button(frame5, text=player_2obj.skill[2], width=10)
    skill_player_2_button4 = tk.Button(frame5, text=player_2obj.skill[3], width=10)

    show_state_label1 = tk.Label(frame4, text='当前状态', textvariable=show_state_label1_var)
    show_active1 = tk.Label(frame4, text='效果', textvariable=show_active1_var)
    show_state_label2 = tk.Label(frame5, text='当前状态', textvariable=show_state_label2_var)
    show_active2 = tk.Label(frame5, text='效果', textvariable=show_active2_var)

    player_1_config_label.grid(row=1, column=1, pady=5)
    player_2_config_label.grid(row=1, column=2, pady=5)
    hp_show_player1.grid(row=2, column=1)
    hp_show_player2.grid(row=2, column=2)
    player_1_name_label.grid(row=3, column=1, pady=10)
    player_2_name_label.grid(row=3, column=2, pady=10)
    frame3.grid(row=4, column=1, columnspan=2, pady=12)

    frame4.grid(row=1, column=1)
    show_animate_label.grid(row=1, column=2)
    frame5.grid(row=1, column=3)

    skill_player_1_button1.grid(row=1, column=1, padx=4)
    skill_player_1_button2.grid(row=1, column=2, padx=4)
    skill_player_1_button3.grid(row=2, column=1, padx=4, pady=8)
    skill_player_1_button4.grid(row=2, column=2, padx=4, pady=8)

    skill_player_2_button1.grid(row=1, column=1, padx=4)
    skill_player_2_button2.grid(row=1, column=2, padx=4)
    skill_player_2_button3.grid(row=2, column=1, padx=4, pady=8)
    skill_player_2_button4.grid(row=2, column=2, padx=4, pady=8)

    show_state_label1.grid(row=3, column=1, pady=2)
    show_active1.grid(row=3, column=2)
    show_state_label2.grid(row=3, column=1)
    show_active2.grid(row=3, column=2)

    skill_player_1_button1.config(command=end_attack_player1)
    skill_player_1_button2.config(command=normal_attack_player1)
    skill_player_1_button3.config(command=defense_player1)
    skill_player_1_button4.config(command=other_player1)

    skill_player_2_button1.config(command=end_attack_player2)
    skill_player_2_button2.config(command=normal_attack_player2)
    skill_player_2_button3.config(command=defense_player2)
    skill_player_2_button4.config(command=other_player2)

    disable_all_button()

    if player_1obj.speed > player_2obj.speed:
        active_player1_button()
    elif player_1obj.speed < player_2obj.speed:
        active_player2_button()
    elif player_1obj.all > player_2obj.all:
        active_player1_button()
    elif player_1obj.all < player_2obj.all:
        active_player2_button()
    else:
        choice = random.choice([1, 2])
        if choice == 1:
            active_player1_button()
        else:
            active_player2_button()


def modify_show():
    while True:
        show_animate_var.set(''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 6)))
        time.sleep(1)


def modify_show_once1():
    disable_all_button()
    show_animate_var.set('-')
    time.sleep(0.5)
    show_animate_var.set('--')
    time.sleep(0.5)
    show_animate_var.set('---')
    time.sleep(0.5)
    show_animate_var.set('----')
    time.sleep(0.5)
    show_animate_var.set('-----')
    time.sleep(0.5)
    show_animate_var.set('------>')
    time.sleep(0.5)
    active_player2_button()


def modify_show_once2():
    disable_all_button()
    show_animate_var.set('-')
    time.sleep(0.5)
    show_animate_var.set('--')
    time.sleep(0.5)
    show_animate_var.set('---')
    time.sleep(0.5)
    show_animate_var.set('----')
    time.sleep(0.5)
    show_animate_var.set('-----')
    time.sleep(0.5)
    show_animate_var.set('<------')
    time.sleep(0.5)
    active_player1_button()


select_elves_button.config(command=select_wizard)


##########################
##########################
def end_attack_player1():
    disable_player1_button()
    active_player2_button()
    global bout
    result = (player_1obj.attack - player_2obj.defense) * 0.3
    if result <= 0:
        temp = ((player_1obj.attack / player_2obj.defense) * 100) * 0.3
        while temp > attack_value_temp['player1_end_attack']:
            temp = temp / 2
        result = temp
    # # 随机增大减少值
    # value = copy.deepcopy(result)
    # present = random.randint(1, 10) * 0.01
    # t_or_f = random.choice([0, 1])
    # if t_or_f == 0:
    #     present = -present
    #     result = value + present * value
    # else:
    #     result = value + present * value
    attack_value_temp['player1_end_attack'] = result
    hp_show_player2['value'] -= result
    monitor_defense()
    bout += 1
    threading.Thread(target=modify_show_once1).start()
    monitor_hp()
    show_player_info()
    show_active1_var.set('产生伤害：{}'.format(round(result, 2)))
    if hp_show_player2['value'] <= 0:
        time.sleep(1)
        disable_all_button()
        messagebox.showinfo(title='提示', message='甲方胜利！')
    return result


def normal_attack_player1():
    disable_player1_button()
    active_player2_button()
    global bout
    result = (player_1obj.attack - player_2obj.defense) * 0.3
    if result <= 0:
        temp = (player_1obj.attack / player_2obj.defense) * 100 * 0.8 * 0.3
        while temp > attack_value_temp['player1_normal_attack']:
            temp = temp / 2
        result = temp
    attack_value_temp['player1_normal_attack'] = result
    hp_show_player2['value'] -= result
    monitor_defense()
    bout += 1
    threading.Thread(target=modify_show_once1).start()
    monitor_hp()
    show_player_info()
    show_active1_var.set('产生伤害：{}'.format(round(result, 2)))
    if hp_show_player2['value'] <= 0:
        time.sleep(1)
        disable_all_button()
        messagebox.showinfo(title='提示', message='甲方胜利！')
    return result


def defense_player1():
    disable_player1_button()
    active_player2_button()
    global bout
    player_1obj.defense = player_1obj.defense + int(player_1obj.defense * 0.15)
    monitor_defense()
    bout += 1
    threading.Thread(target=modify_show_once1).start()
    monitor_hp()
    show_player_info()
    show_active1_var.set('防御值增加\n当前防御值：{}'.format(round(player_1obj.defense, 2)))
    return player_1obj.defense


def other_player1():
    disable_player1_button()
    active_player2_button()
    global bout
    temp = [1, 2, 3, 4, 5]
    num = random.choice(temp)
    hp = player_1obj.other()
    if num == 1:
        result = 15
    else:
        result = 5
    hp_show_player2['value'] -= result
    if hp:
        if 100 - hp_show_player1['value'] > hp:
            hp_show_player1['value'] += hp
            show_active1_var.set('血量增加{}\n造成伤害{}'.format(round(hp, 2), result))
        else:
            hp_show_player1['value'] = 100
            show_active1_var.set('血量回满\n造成伤害{}'.format(result))
    monitor_defense()
    bout += 1
    threading.Thread(target=modify_show_once1).start()
    monitor_hp()
    show_player_info()
    if hp_show_player2['value'] <= 0:
        time.sleep(1)
        disable_all_button()
        messagebox.showinfo(title='提示', message='甲方胜利！')
    return result


#######################
def end_attack_player2():
    disable_player2_button()
    active_player1_button()
    global bout
    result = (player_2obj.attack - player_1obj.defense) * 0.3
    if result <= 0:
        temp = ((player_2obj.attack / player_1obj.defense) * 100) * 0.3
        while temp > attack_value_temp['player2_end_attack']:
            temp = temp / 2
        result = temp
    attack_value_temp['player2_end_attack'] = result
    hp_show_player1['value'] -= result
    bout += 1
    monitor_hp()
    monitor_defense()
    threading.Thread(target=modify_show_once2).start()
    show_player_info()
    show_active2_var.set('产生伤害：{}'.format(round(result, 2)))
    if hp_show_player1['value'] <= 0:
        time.sleep(1)
        disable_all_button()
        messagebox.showinfo(title='提示', message='乙方胜利！')
    return result


def normal_attack_player2():
    disable_player2_button()
    active_player1_button()
    global bout
    result = (player_2obj.attack - player_1obj.defense) * 0.3
    if result <= 0:
        temp = (player_2obj.attack / player_1obj.defense) * 100 * 0.8 * 0.3
        while temp > attack_value_temp['player2_normal_attack']:
            temp = temp / 2
        result = temp
    attack_value_temp['player2_normal_attack'] = result
    hp_show_player1['value'] -= result
    monitor_defense()
    bout += 1
    monitor_hp()
    threading.Thread(target=modify_show_once2).start()
    show_player_info()
    show_active2_var.set('产生伤害：{}'.format(round(result, 2)))
    if hp_show_player1['value'] <= 0:
        time.sleep(1)
        disable_all_button()
        messagebox.showinfo(title='提示', message='乙方胜利！')
    return result


def defense_player2():
    disable_player2_button()
    active_player1_button()
    global bout
    player_2obj.defense = player_2obj.defense + int(player_2obj.defense * 0.15)
    monitor_defense()
    bout += 1
    monitor_hp()
    threading.Thread(target=modify_show_once2).start()
    show_player_info()
    show_active2_var.set('防御值增加\n当前防御值：{}'.format(round(player_2obj.defense, 2)))
    return player_2obj.defense


def other_player2():
    disable_player2_button()
    active_player1_button()
    global bout
    temp = [1, 2, 3, 4, 5]
    num = random.choice(temp)
    hp = player_2obj.other()
    if num == 1:
        result = 15
    else:
        result = 5
    hp_show_player1['value'] -= result
    if hp:
        if 100 - hp_show_player2['value'] > hp:
            hp_show_player2['value'] += hp
            show_active2_var.set('血量增加{}\n造成伤害{}'.format(round(hp, 2), result))
        else:
            hp_show_player2['value'] = 100
            show_active2_var.set('血量回满\n造成伤害{}'.format(result))
    bout += 1
    monitor_hp()
    monitor_defense()
    threading.Thread(target=modify_show_once2).start()
    show_player_info()
    if hp_show_player1['value'] <= 0:
        time.sleep(1)
        disable_all_button()
        messagebox.showinfo(title='提示', message='乙方胜利！')
    return result


#######################
def disable_all_button():
    skill_player_1_button1['state'] = 'disable'
    skill_player_1_button2['state'] = 'disable'
    skill_player_1_button3['state'] = 'disable'
    skill_player_1_button4['state'] = 'disable'
    skill_player_2_button1['state'] = 'disable'
    skill_player_2_button2['state'] = 'disable'
    skill_player_2_button3['state'] = 'disable'
    skill_player_2_button4['state'] = 'disable'


def disable_player1_button():
    skill_player_1_button1['state'] = 'disable'
    skill_player_1_button2['state'] = 'disable'
    skill_player_1_button3['state'] = 'disable'
    skill_player_1_button4['state'] = 'disable'


def disable_player2_button():
    skill_player_2_button1['state'] = 'disable'
    skill_player_2_button2['state'] = 'disable'
    skill_player_2_button3['state'] = 'disable'
    skill_player_2_button4['state'] = 'disable'


def active_all_button():
    skill_player_1_button1['state'] = 'active'
    skill_player_1_button2['state'] = 'active'
    skill_player_1_button3['state'] = 'active'
    skill_player_1_button4['state'] = 'active'
    skill_player_2_button1['state'] = 'active'
    skill_player_2_button2['state'] = 'active'
    skill_player_2_button3['state'] = 'active'
    skill_player_2_button4['state'] = 'active'


def active_player1_button():
    skill_player_1_button1['state'] = 'active'
    skill_player_1_button2['state'] = 'active'
    skill_player_1_button3['state'] = 'active'
    skill_player_1_button4['state'] = 'active'


def active_player2_button():
    skill_player_2_button1['state'] = 'active'
    skill_player_2_button2['state'] = 'active'
    skill_player_2_button3['state'] = 'active'
    skill_player_2_button4['state'] = 'active'


def show_player_info():
    num = bout / 2
    if num <= 1:
        num = 1
    print('第{}回合'.format(int(num)))
    print('玩家一伤害值：', player_1obj.attack, '   ', '玩家二伤害值：', player_2obj.attack)
    print('玩家一血量：', player_1obj.hp, '   ', '玩家二血量：', player_2obj.hp)
    print('玩家一防御值：', player_1obj.defense, '   ', '玩家二防御值：', player_2obj.defense)
    print('-' * 100)
    show_state_label1_var.set('伤害值：{}\n防御值：{}'.format(player_1obj.attack, player_1obj.defense))
    show_state_label2_var.set('伤害值：{}\n防御值：{}'.format(player_2obj.attack, player_2obj.defense))


def monitor_hp():
    if hp_show_player1['value'] > 100:
        hp_show_player1['value'] = 100
    elif hp_show_player2['value'] > 100:
        hp_show_player2['value'] = 100


def monitor_defense():
    if player_1obj.defense >= 300:
        player_1obj.defense = 300
        skill_player_1_button3['state'] = 'disable'
    elif player_2obj.defense >= 300:
        player_2obj.defense = 300
        skill_player_2_button3['state'] = 'disable'


root.mainloop()
