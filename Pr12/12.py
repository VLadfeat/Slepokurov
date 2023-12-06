import requests
import json
import tkinter as tk

def get_rep_inf():
    reposit_name = entr.get()
    ssilka = f'https://api.github.com/repos/{reposit_name}'
    response = requests.get(ssilka)
    inf = response.json()

    itog = {'company': inf.get('company', 'net_infi'),
        'created_at': inf.get('created_at', 'net_infi'),
        'email': inf.get('email', 'net_infi'),
        'id': inf.get('id', 'net_infi'),
        'name': inf.get('name', 'net_infi'),
        'url': inf.get('url', 'net_infi')
    }
    with open('rep_itog.json', 'w') as file:
        json.dump(itog, file)

win = tk.Tk()
win.title('Слепокуров Владислав Сергеевич')
win.geometry('500x500')
entr = tk.Entry(win)
entr.pack()

but = tk.Button(win, text='Жми', command=get_rep_inf)
but.pack()
win.mainloop()