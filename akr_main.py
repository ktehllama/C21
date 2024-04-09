# TODO | MARCH 28,2024 12:35 pm
# Make stats box label not go white when hovering 4
# Make average of TC and RC and add color for it (using interpolate) 3
# Add history and last card played on GUI 1
# Add total cards and decks left 2

from tkinter import *
from cyml_utils import *
from method_parse import *

mpr = MethodParser()

DECKS: int = 6
DECK_PENETRATION: float = 0.50
DECK_CARDS = [str(card) for card in list(range(2,11)) + ["J","Q","K","A"]]
shoe = [card for _ in range(DECKS) for card in DECK_CARDS * 4]
total_cards: int = DECKS*52
cards_history: list = []
def append_limit(lst, item, limit=10):
    lst.append(item)
    if len(lst) > limit:
        lst.pop(0)

button_methods_name = ['HILO','OMEGAII','KO','ACEFC']
stor_count = {"running count": {},"true count": {}}
all_methods = mpr.get_return_methods()
for method_idx in range(len(all_methods)):
    starting_count = 0
    if str(all_methods[method_idx]) == 'ko':
        starting_count = 4-(4*DECKS)
    elif str(all_methods[method_idx]) == 'acefivecount':
        pass
    else:
        stor_count['true count'][str(all_methods[method_idx])] = starting_count
    stor_count['running count'][str(all_methods[method_idx])] = starting_count
def rt_count_update(card_value):
    global cm__value
    cm__value = {}
    for method in all_methods:
        cm__value[str(method)] = mpr.get_card_values(str(method))[str(card_value)]
    def count_type(ctype):
        div_decks_left = 1
        if ctype == 'true count':
            div_decks_left = total_cards/52
        for s__method in stor_count[str(ctype)]:
            stor_count[str(ctype)][s__method] += cm__value[s__method]/div_decks_left
    count_type('running count')
    count_type('true count')
    print(msg('info')+"Current {} & {} ({}):\n{}".format(colored('RC','white'),colored('TC','white'),colored('stor_count','green'),stor_count))

stor_recommend = {ckey:'' for ckey in all_methods}
def bstats__update(button_list):
    c_types = ['positive','neutral','negative']
    non_tc = ['ko','acefivecount']
    recom_debug = {ckey:None for ckey in all_methods}
    recommendations = {mkey:{ckey: mpr.get_recommendations(mkey, ckey) for ckey in c_types} for mkey in all_methods}
    for method in stor_count["true count"]:
        if stor_count["true count"][method] >= recommendations[method]['positive'][0]:
            stor_recommend[method] = [recommendations[method]['positive'][1],recommendations[method]['positive'][2]]
            recom_debug[method] = ['inc','green']
        elif recommendations[method]['negative'][0] > stor_count["true count"][method]:
            stor_recommend[method] = [recommendations[method]['negative'][1],recommendations[method]['negative'][2]]
            recom_debug[method] = ['neg','red']
        elif stor_count["true count"][method] < recommendations[method]['positive'][0] and stor_count["true count"][method] >= recommendations[method]['negative'][0]:
            stor_recommend[method] = [recommendations[method]['neutral'][0],recommendations[method]['neutral'][1]]
            recom_debug[method] = ['neu','yellow']
    for method in stor_count["running count"]:
        if method in non_tc:
            if method == 'ko':
                def get_ko_pivot(am_decks):
                    pivots = {1:2,2:1,6:-4,8:-6}
                    return pivots[am_decks]
                if stor_count["running count"][method] >= get_ko_pivot(DECKS):
                    stor_recommend[method] = [recommendations[method]['positive'][1],recommendations[method]['positive'][2]]
                    recom_debug[method] = ['inc','green']
                elif recommendations[method]['negative'][0] > get_ko_pivot(DECKS):
                    stor_recommend[method] = [recommendations[method]['negative'][1],recommendations[method]['negative'][2]]
                    recom_debug[method] = ['neg','red']
            else:
                if stor_count["running count"][method] >= recommendations[method]['positive'][0]:
                    stor_recommend[method] = [recommendations[method]['positive'][1],recommendations[method]['positive'][2]]
                    recom_debug[method] = ['inc','green']
                elif recommendations[method]['negative'][0] > stor_count["running count"][method]:
                    stor_recommend[method] = [recommendations[method]['negative'][1],recommendations[method]['negative'][2]]
                    recom_debug[method] = ['neg','red']
                elif stor_count["running count"][method] < recommendations[method]['positive'][0] and stor_count["running count"][method] >= recommendations[method]['negative'][0]:
                    stor_recommend[method] = [recommendations[method]['neutral'][0],recommendations[method]['neutral'][1]]
                    recom_debug[method] = ['neu','yellow']

    print(msg('info')+"Current {} ({}):\n{}\n{}:{} - {}:{} - {}:{} - {}:{}".format(colored('RECOMMENDATIONS','white'),colored('stor_recommend','green'),stor_recommend,colored('HILO','white'),colored(recom_debug['hilo'][0],recom_debug['hilo'][1]),colored('OMEGAII','white'),colored(recom_debug['omegaii'][0],recom_debug['omegaii'][1]),colored('KO','white'),colored(recom_debug['ko'][0],recom_debug['ko'][1]),colored('ACEFC','white'),colored(recom_debug['acefivecount'][0],recom_debug['acefivecount'][1])))         

    mip_tc_inflation = [1,0]
    divide_inflation_ko = {8:11,6:8,2:2.5,1:1}
    idx = 0
    for button in button_list:
        am_idx = all_methods[idx]
        rc = round(stor_count['running count'][am_idx])

        if am_idx in non_tc:
            if am_idx == 'ko':
                button.configure(bg=interpolate((rc+(abs(4-(4*DECKS))))/divide_inflation_ko[DECKS]))
            elif am_idx == 'acefivecount':
                button.configure(bg=interpolate(stor_count['running count'][am_idx]))
            rt_c = f'RC: {rc}'
        else:
            tc = round(stor_count['true count'][am_idx],2)
            button.configure(bg=interpolate(stor_count['true count'][am_idx]+mip_tc_inflation[idx]))
            rt_c = f'RC: {rc}\nTC: {tc}'
        button.configure(text=f"{button_methods_name[idx]}\n{rt_c}\n{stor_recommend[am_idx][0]}")
        idx+=1
    

TK_BACKGROUND: str = "#F0E7E9"
TK_WINSIZE: str = "500x600"
tk_title: str = "Akarvis | Blackjack Card Counter"

BUTTON_RATIO: list = [[5,3],[22,12]]
BUTTON_BG: str = "white"
FONTSTYLE: list = ["Lato", 12, "bold"]
RELIEF_TYPE: str = 'flat'
BORDER_BGT: list = ['black',2]

def interpolate(value):
    if value < 0:
        value = 0
    elif value > 2 or value == 2.0:
        value = 2
    elif value == 1.0:
        value = 1
    def from_rgb(rgb):
        return "#%02x%02x%02x" % rgb
    base_colors = [(225,0,0),(0,0,225),(0,225,0)]
    if type(value) == int:
        return from_rgb(base_colors[value])
    else:
        if value < 1:
            blue = round(value * 225)
            red = 225 - blue
            return from_rgb(tuple([red,0,blue]))
        elif value > 1 and value < 2:
            abs_zero = abs(round(value - int(str(value)[0]),2))
            green = round(abs_zero * 225)
            blue = 225 - green
            return from_rgb(tuple([0,green,blue]))
amount_methods = mpr.get_return_methods('--nmethods')

root = Tk()
root.title(tk_title)
root.geometry(TK_WINSIZE)
root.configure(bg=TK_BACKGROUND)
label_title = Label(root, text="Blackjack Card Counter").pack(pady=10)

mainframe = Frame(root, bg='yellow', bd=2, relief='solid')
mainframe.pack(expand=True)

def rc(l,a,c):
    s_rc: list = [0,0]
    for i in range(a):
        if s_rc[1] == c:
            s_rc[1] = 0
            s_rc[0] += 1
        l[i].grid(row=s_rc[0], column=s_rc[1], sticky='ew')
        s_rc[1] += 1

def make_expandable(frame,r,c):
    for i in range(int(r)):
        frame.grid_rowconfigure(i, weight=1)
    for i in range(int(c)):
        frame.grid_columnconfigure(i, weight=1)

stats_frame = Frame(mainframe, bg='white')
stats_frame.pack(expand=True, fill='x')
make_expandable(stats_frame,2,2)
stats_b_list: list = [Button(stats_frame, text="{}".format(button_methods_name[i]), width=BUTTON_RATIO[1][0], height=BUTTON_RATIO[1][1], font=["Lato", 9, "bold"], fg='#e9edf0', bg=BUTTON_BG, relief=RELIEF_TYPE, highlightbackground=BORDER_BGT[0],highlightthickness=BORDER_BGT[1],command=lambda text_value=str(i+2): print(text_value)) for i in range(amount_methods)]
rc(stats_b_list, 4, 2)

SIDEBAR_COLOR: str = 'white'
history_sidebar_frame = Frame(stats_frame, bg=SIDEBAR_COLOR,bd=2,relief='solid')
history_sidebar_frame.grid(row=0,column=2, rowspan=2, sticky='nsew')

# h_sidebar = Label(history_sidebar_frame, text='a\n1\n2\n3', font=['Lato',9,'bold'], padx=6, bg=SIDEBAR_COLOR)
# h_sidebar.pack(side='left')
# TODO: MAKE LAST ITEM COLORED IN HISTORY
sbr = Text(history_sidebar_frame, font=['Lato',9,'bold'], padx=6, bg=SIDEBAR_COLOR, height=10)

def history_sidebar_update(sidebar_list):
    pass
    # h_sidebar.configure(text="{}\n{}\n{}".format('mocha','\n\n'.join(str(idx) for idx in reversed(sidebar_list)),'loca'))
   
buttons_frame = Frame(mainframe, bg='grey')
buttons_frame.pack(expand=True, fill='x')
make_expandable(buttons_frame,2,5)

def button_listener(i_card):
    global total_cards
    total_cards -= 1
    append_limit(cards_history, str(i_card))
    decks_left = total_cards/52
    played_card = cards_history[-1]

    rt_count_update(i_card)
    bstats__update(stats_b_list)
    history_sidebar_update(cards_history)

    print(msg('notice')+f"Total Cards: {total_cards}\nHistory: {cards_history}\nDecks Left: {decks_left}\nPlayed card: {played_card}")

buttons_list: list = [Button(buttons_frame, text=str(i+2), width=BUTTON_RATIO[0][0], height=BUTTON_RATIO[0][1], font=FONTSTYLE, bg=BUTTON_BG, relief=RELIEF_TYPE, highlightbackground=BORDER_BGT[0],highlightthickness=BORDER_BGT[1], command=lambda text_value=str(i+2): button_listener(text_value)) for i in range(8)]
rc(buttons_list, 8, 4)
button_10 = Button(buttons_frame, text="10 J Q K", width=BUTTON_RATIO[0][0], height=BUTTON_RATIO[0][1], font=FONTSTYLE, bg=BUTTON_BG, relief=RELIEF_TYPE, highlightbackground=BORDER_BGT[0],highlightthickness=BORDER_BGT[1], command=lambda text_value=str("10"): button_listener(text_value)).grid(row=0, column=4, sticky='ew')
button_A = Button(buttons_frame, text="A", width=BUTTON_RATIO[0][0], height=BUTTON_RATIO[0][1], font=FONTSTYLE, bg=BUTTON_BG, relief=RELIEF_TYPE, highlightbackground=BORDER_BGT[0],highlightthickness=BORDER_BGT[1], command=lambda text_value=str("A"): button_listener(text_value)).grid(row=1, column=4, sticky='ew')

root.mainloop()