import csv

import class_character_template

def print_character_class_details(character_class, body):
  top_spacer = ""
  bottom_spacer = ""
  
  for x in range(len(character_class) + 2):
    top_spacer += "_" 
    bottom_spacer += "-" 
  print("  " + top_spacer + "\n**|" + character_class.upper() + "|**\n  " + bottom_spacer + "\n" + body)

def character_summary(class_type):
    with open('character_classes_descriptions.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        class_info = None

        for row in csv_reader:
          if row["class"] == class_type:
            class_info = row

    if class_info is None:
      print("Invalid")
    else:
      print_character_class_details(class_info["class"], class_info["description"])


character_summary("archer")
            
            
        
        
