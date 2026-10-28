def get_choices():
   player_choice="blue"
   computer_choice='orange'
   choices={"player":player_choice,"computer":computer_choice} 
   return choices
choices=get_choices()
dict={"name":"Nikhil","color":choices}
print(dict)