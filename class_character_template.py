
    
def character_stats(class_type):
        
        
    if class_type == "knight":
            
            
        health = 20
        attack = 15
        defence = 15
        evasion = 3
        sneak = 2
        persuasion = 7
        magic = 1
        intelligence = 10
            
        
    elif class_type == "mage":
        
        health = 15
        attack = 5
        defence = 5
        evasion = 10
        sneak = 7
        persuasion = 10
        magic = 20
        intelligence = 15
        
    elif class_type == "theif":
        
        health = 10
        attack = 10
        defence = 5
        evasion = 20
        sneak = 20
        persuasion = 10
        magic = 5
        intelligence = 5
            
    elif class_type == "minstrel":
            
        health = 5
        attack = 5
        defence = 5
        evasion = 15
        sneak = 12
        persuasion = 30
        magic = 5
        intelligence = 12
            
    elif class_type == "archer":
        
        health = 10
        attack = 15
        defence = 5
        evasion = 15
        sneak = 15
        persuasion = 5
        magic = 1
        intelligence = 5
        
    print("Hp", health, "\nAtk", attack,"\nDef", defence,"\nEvasion", evasion,\
        "\nSneak", sneak,"\nPersuasion", persuasion, "\nmagic", magic,"\nIntelligence", intelligence)
        
    return health, attack, defence, evasion, sneak, persuasion, magic, intelligence
    
    
        
        

            
       
