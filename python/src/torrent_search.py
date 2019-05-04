#!/usr/bin/env python
from tkinter import *
from tkinter import messagebox
import requests, webbrowser, tkinter.font as tkFont
from lxml import html
from bs4 import BeautifulSoup

def search():
    initial_url = "https://piratebay-proxylist.se"
    try:
        page = requests.get(initial_url)
    except:
        messagebox.showinfo("Internet not available", "Please check your internet connection!")
        return

    movie_name = search_entry.get().strip()
    movie_name = movie_name.split()
    movie_name = "+".join(movie_name)
    if len(movie_name) == 0:
        messagebox.showinfo("Invalid search", "Please enter valid search")
        return

    soup = BeautifulSoup(page.text, 'html.parser')
    url_tag = soup.find('span', attrs={'class': 'domain'})
    url = "https://" + url_tag.text.strip() + "/s/?q=" + movie_name + "&page=0&orderby=99"
    webbrowser.open(url, new=2)

root = Tk()
root.title("Torrent Search")
root.geometry("600x150+350+150")
root.configure(background='black')

font_search = tkFont.Font(family="Candara bold", size=15)

search_entry = Entry(root, font=font_search)
search_entry.configure(fg="#ff0000")
search_entry.place(x=75, y=50, width=325, height=35)
search_entry.focus()

button_search = Button(root, text="Search", font=font_search, command=search)
button_search.place(x=425, y=50, width=100, height=35)

root.mainloop()