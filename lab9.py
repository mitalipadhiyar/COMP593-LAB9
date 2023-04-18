from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import poke_api


#creatingthe window
root = Tk()
root.title("Pokemon Information")


#creating the frame
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=3)

frm_btm_left = ttk.Labelframe(root, text='Info')
frm_btm_left.grid(row=1, column=0, sticky=N)

frm_btm_right = ttk.Labelframe(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=0 , pady=(0,25), sticky=N)


#creating the label for upper frame
lable_1 = ttk.Label(frm_top, text='Pokemon name:')
lable_1.grid(row=0, column=0,padx=(70,0), pady=20)

ent_poke_name = ttk.Entry(frm_top)
ent_poke_name.grid(row=0, column=1, padx=(5,0), pady=(15,10))

#defining callback function for button
def button_getinfo_click():
    get_pokemon_name= ent_poke_name.get().strip()
    if get_pokemon_name == '':
        return
    
    poke_info = poke_api.get_pokemon_info(get_pokemon_name)
    
    if poke_info is None:
        error_messg = f"Unable to fetch information for {get_pokemon_name.title()} from the PokeAPI."
        messagebox.showinfo(title='Error', message=error_messg , icon='error')
        return
    

    #populate the info
    lable_height_value['text'] = f"{poke_info['height']} dm"
    lable_weight_value['text'] = f"{poke_info['weight']} hg "
    lable_type_value['text'] = f"{poke_info['types'][0]['type']['name']}"
    

    #populate the stats
    prg_hp['value'] = poke_info['stats'][0]['base_stat']
    prg_attack['value'] = poke_info['stats'][1]['base_stat']
    prg_defense['value'] = poke_info['stats'][2]['base_stat']
    prg_spl_attack['value'] = poke_info['stats'][3]['base_stat']
    prg_spl_defense['value'] = poke_info['stats'][4]['base_stat']
    prg_speed['value'] = poke_info['stats'][5]['base_stat']

    return 
     
#creating button for upper right frame
btn_hello = ttk.Button(frm_top, text='Get Info', command=button_getinfo_click)
btn_hello.grid(row=0, column=2, padx= (15,110), pady=10)

#adding widgets to bottom left
lable_height = ttk.Label(frm_btm_left, text='Height:')
lable_height.grid(row=0, column=0,padx=(20,0), pady=(10,0), sticky=E)
lable_height_value = ttk.Label(frm_btm_left, text='')
lable_height_value.grid(row=0, column=1,padx=(0,30), pady=(10,0))

lable_weight = ttk.Label(frm_btm_left, text='Weight:')
lable_weight.grid(row=1, column=0,padx=(20,0), pady=(10,0),sticky=E)
lable_weight_value = ttk.Label(frm_btm_left, text='')
lable_weight_value.grid(row=1, column=1,padx=(0,30) ,pady=(10,0))

lable_type = ttk.Label(frm_btm_left, text='Type:')
lable_type.grid(row=2, column=0,padx=(20,0),pady=(10,0), sticky=E)
lable_type_value = ttk.Label(frm_btm_left, text='')
lable_type_value.grid(row=2, column=1,padx=(0,30), pady=(10,0))


#adding widgets to bottom right frame
lable_hp = ttk.Label(frm_btm_right, text='HP:')
lable_hp.grid(row=0, column=1,padx=0, pady=(15,0),sticky=E)
prg_hp= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_hp.grid(row=0, column=2,padx=0, pady=(15,0))

lable_attack = ttk.Label(frm_btm_right, text='Attack:')
lable_attack.grid(row=1, column=1,padx=0, pady=(15,0),sticky=E)
prg_attack= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_attack.grid(row=1, column=2,padx=0, pady=(15,0))

lable_defense = ttk.Label(frm_btm_right, text='Defense:')
lable_defense.grid(row=2, column=1,padx=0, pady=(15,0),sticky=E)
prg_defense= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_defense.grid(row=2, column=2,padx=0, pady=(15,0))

lable_spl_attack = ttk.Label(frm_btm_right, text='Special Attack:')
lable_spl_attack.grid(row=3, column=1,padx=0, pady=(15,0),sticky=E)
prg_spl_attack= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_spl_attack.grid(row=3, column=2,padx=0, pady=(15,0))

lable_spl_defense = ttk.Label(frm_btm_right, text='Special Defense:')
lable_spl_defense.grid(row=4, column=1,padx=0, pady=(15,0),sticky=E)
prg_spl_defense= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_spl_defense.grid(row=4, column=2 ,padx=0, pady=(15,0))

lable_speed = ttk.Label(frm_btm_right, text='Speed:')
lable_speed.grid(row=5, column=1,padx=0, pady=(15,0),sticky=E)
prg_speed= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_speed.grid(row=5, column=2,padx=0, pady=(15,0))

root.mainloop()
