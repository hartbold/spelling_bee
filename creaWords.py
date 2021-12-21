import json
import random
import os

def is_pangram(word):
    return len(word) == 7; # número de letras de la colmena       

worddict = dict()
# with open(os.getenv("WEB") + "/spelling_bee/castellano_clean.dict", 'r') as dictfile:
with open(os.getenv("WEB") +"spelling_bee/castellano_clean.dict", 'r') as dictfile:
    pangram_set = set()
    for line in dictfile:
        palabro = line.strip()
        worddict[palabro] = True;
        if is_pangram(palabro):
            letterset = frozenset(palabro)
            pangram_set.add(letterset)

res = [] 

# @todo Comprobar que la palabra usada no sea la misma que ayer


while(len(res) < 15):
    res = []
    todays_letters = list(random.choice(list(pangram_set)))
    score = 0
    center_letter = todays_letters[3]
    pangram = ''
    for w in worddict: 
        flag = True
        for c in w: 
            if c not in todays_letters: 
                flag = False 
        if center_letter not in w: 
            flag = False 
        if flag == True:
            res.append(w)
            if len(w) == 3: score +=1
            elif is_pangram(w): 
                score +=17
                pangram = w
            elif len(w) > 4: score += len(w)

data = {'letters':todays_letters, 'pangram': pangram, 'possible_words':res, 'center_letter': center_letter, 'maxscore': score}

# escribimos la data en un fichero que se leerá desde le programa para recuperar las letras

print(os.getcwd())
file = open(os.getenv("WEB") + "spelling_bee/palabras_del_dia.json", "wt")
json.dump(data, file)
#file.write(data)
file.close()