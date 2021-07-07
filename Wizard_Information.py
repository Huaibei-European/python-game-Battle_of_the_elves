# 辛迪拉
class CinDiLa:
    def __init__(self):
        self.hp = 169
        self.attack = 136
        self.defense = 100
        self.S_attack = 70
        self.S_defense = 100
        self.speed = 130
        self.all = self.hp + self.attack + self.defense + self.S_attack + self.S_defense + self.speed
        self.skill = ['片叶断山海', '幽径无影击', '保护姿态', '绿叶强袭']

    def end_attack(self):
        return

    def normal_attack(self):
        pass

    def defense(self):
        pass

    def other(self):
        self.attack += 30
        self.defense += 30


# 风沁
class WindBlow:
    def __init__(self):
        self.hp = 170
        self.attack = 70
        self.defense = 114
        self.S_attack = 134
        self.S_defense = 114
        self.speed = 133
        self.all = self.hp + self.attack + self.defense + self.S_attack + self.S_defense + self.speed
        self.skill = ['风过叶飘零', '枫叶落满地', '回避意识', '辉光灵谕']

    def end_attack(self):
        pass

    def normal_attack(self):
        pass

    def defense(self):
        pass

    def other(self):
        hp = 20
        self.attack += 40
        self.defense += 10
        return hp


# 玛格
class Mag:
    def __init__(self):
        self.hp = 155
        self.attack = 128
        self.defense = 99
        self.S_attack = 70
        self.S_defense = 99
        self.speed = 129
        self.all = self.hp + self.attack + self.defense + self.S_attack + self.S_defense + self.speed
        self.skill = ['太古聚灵阵', '破损古墓', '独自守护', '灵附魂归']

    def end_attack(self):
        pass

    def normal_attack(self):
        pass

    def defense(self):
        pass

    def other(self):
        hp = 35
        self.attack += 10
        self.defense += 20
        return hp


# 金轮赤乌
class JinLunChiWu:
    def __init__(self):
        self.hp = 170
        self.attack = 135
        self.defense = 104
        self.S_attack = 70
        self.S_defense = 107
        self.speed = 134
        self.all = self.hp + self.attack + self.defense + self.S_attack + self.S_defense + self.speed
        self.skill = ['金乌焚世诀', '十阳照世阵', '翅膀包围', '神鸟扑击']

    def end_attack(self):
        pass

    def normal_attack(self):
        pass

    def defense(self):
        pass

    def other(self):
        hp = 10
        self.attack += 25
        self.defense += 10
        return hp


# 学神
class XueShen:
    def __init__(self):
        self.hp = 159
        self.attack = 70
        self.defense = 103
        self.S_attack = 134
        self.S_defense = 103
        self.speed = 132
        self.all = self.hp + self.attack + self.defense + self.S_attack + self.S_defense + self.speed
        self.skill = ['学神的祝福', '不及格射线', '标准答案', '劳逸结合']

    def end_attack(self):
        pass

    def normal_attack(self):
        pass

    def defense(self):
        pass

    def other(self):
        hp = 35
        self.defense += 45
        self.attack -= 15
        if self.attack <= 0:
            self.attack = 10
        return hp


proxy = {
    'CinDiLa': CinDiLa,
    'WindBlow': WindBlow,
    'Mag': Mag,
    'JinLunChiWu': JinLunChiWu,
    'XueShen': XueShen,
}
