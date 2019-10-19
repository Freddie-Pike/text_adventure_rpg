import class_character_template


def character_summary(class_type):
    
    template_dictionary = {"knight":"  ________\n**|KNIGHT|**\n  --------"\
                           "\nHigh health, attack, and defence with reasonable persuasion and intelligence;"\
                           "Knights are well rounded characters"\
                           "\nAlthough, be careful retreating from battle and don't expect to sneak by many enemys",
                           
                           "archer":"  ________\n**|ARCHER|**\n  --------",
                           "minstrel":"  __________\n**|MINSTREL|**\n  ----------",
                           "theif":"  ________\n**|THEIF|**\n  --------",
                           "mage":"  _______\n**|MAGE|**\n  -------",
                           }
    
    while(True):
        if class_type in template_dictionary :
            print(template_dictionary[class_type])
            break
        
        else:
            print("invalid")
            
            
        
        
