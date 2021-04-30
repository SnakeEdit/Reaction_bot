import json
# import pyodbc

def check_string_in_reaction(msg):
    with open('Snake.json', 'r', encoding='utf-8') as array_react: 
        
        reactus = json.load(array_react)
        
        for react_word in reactus:
            for word in react_word['react_words']:
                if word == msg:
                    return react_word['react_id']

    return None

def id_reaction(index_id):
    with open('Snake.json', 'r', encoding='utf-8') as reaction_id:
        
        id_reaction_desu = json.load(reaction_id)
        id_immortal = index_id

        for id_react in id_reaction_desu:
            
            if id_immortal == id_react['react_id']:
                
                return (id_react['react_answer'])