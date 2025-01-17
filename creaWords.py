import json
import random
import os

def is_pangram(word):
    if len(set(list(word))) == 7: return True 
    return False

worddict = dict()
# with open(os.getenv("WEB") + "/spelling_bee/castellano_clean.dict", 'r') as dictfile:
with open(os.getenv("WEB") +"spelling_bee/castellano_clean.dict", 'r', 1,'utf-8') as dictfile:
    pangram_set = set()
    for line in dictfile:
        palabro = line.strip().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n")
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

print(data)

print(os.getcwd())
file = open(os.getenv("WEB") + "spelling_bee/palabras_del_dia.json", "wt")
json.dump(data, file)
#file.write(data)
file.close()