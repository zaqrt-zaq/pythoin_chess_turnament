from tabulate import tabulate
from random import randint
from operator import itemgetter
from os import system

def wypisz(list,text):
  system('clear')
  print(tabulate(list, headers='firstrow', tablefmt='fancy_grid'))
  print(text)

def make_list():
  zawodnicy.insert(0,table_header)
  
def sort_id():
  zawodnicy.pop(0)
  zawodnicy.sort(key=itemgetter(0))
  make_list()

def sort_score():
  zawodnicy.pop(0)
  zawodnicy.sort(key=itemgetter(2),reverse=True)
  make_list()

def select_pass():
  if number_players%2!=0:
    global pas
    pas=randint(0,number_players-1)
    zawodnicy[pas].append('pass')
    zawodnicy[pas][2]+=1
    zawodnicy[pas][3]+=1
  a=zawodnicy.pop(pas)
  zawodnicy.append(a)


number_rounds=int(input("Number of rounds: "))
number_players=int(input("Number of players: "))
table_header=['ID','Name', 'points', 'W', 'D', 'L', 'color']
if number_players%2!=0:
    table_header.append('pass')
zawodnicy = []

for i in range(number_players):
  list =[i+1,0,0,0,0,0,'black']
  list[1]=input("podaj imie: ")
  zawodnicy.append(list)

pas = number_players-1
zawodnicy[pas].append('pass')
zawodnicy[pas][2]+=1
zawodnicy[pas][3]+=1
make_list()

for round in range(number_rounds):
  for i in range(number_players):
    zawodnicy[i+1][0]=i+1
    if i%2==0:
      zawodnicy[i+1][6]='white'
    else:
      zawodnicy[i+1][6]='black'

  a=1
  while a!=0:
    wypisz(zawodnicy,'co chesz zrobić:\nzakończ rundę:0\nwypisz:1\ndodaj wyniki:2')
    a=int(input(">>"))
    if a==2:
      wypisz(zawodnicy,'write id to modify')
      b = int(input('>>'))
      temp_table=[table_header,zawodnicy[b]]
      wypisz(temp_table,'jaki wynik:\npomyłka:0\nwygrana:1\nprzegrana:2\nremis:3')
      c = int(input(">>"))
      if c==1:
        zawodnicy[b][3]+=1
        zawodnicy[b][2]+=1
        if b%2==0:
          zawodnicy[b-1][5]+=1
        else:
          zawodnicy[b+1][5]+=1
      elif c==2:
        zawodnicy[b][5]+=1
        if b%2==0:
          zawodnicy[b-1][3]+=1
          zawodnicy[b-1][2]+=1
        else:
          zawodnicy[b+1][3]+=1
          zawodnicy[b+1][2]+=1
      elif c==3:
        zawodnicy[b][2]+=0.5
        zawodnicy[b][4]+=1
        if b%2==0:
          zawodnicy[b-1][2]+=0.5
          zawodnicy[b-1][4]+=1
        else:
          zawodnicy[b+1][2]+=0.5
          zawodnicy[b+1][4]+=1
      wypisz(zawodnicy,' ')
    
  zawodnicy.pop(0)
  zawodnicy.sort(key=itemgetter(0))
  zawodnicy[pas].remove('pass')
  zawodnicy.sort(key=itemgetter(2),reverse=True)
  select_pass()
  make_list()
