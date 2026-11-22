while True:
    print("===== PYTHON AI TOOLKIT =====")

    print("1. Analyse text")
    print("2. Process data")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
       print("Starting text analysis...")
       text=input("Enter some text:")
       text_length = len(text)
       words = text.split()
       word_count = len(words)
       search_word = input("Which word would you like to search for?")
       word_matches = 0
       for word in words:
          if word.lower().strip(".,!?") == search_word.lower().strip(".,!?"):
            word_matches = word_matches + 1
        
       print(f"{search_word} appears {word_matches} times")


       print(f"Your text has {text_length} charactars")
       print(f"There are {word_count} words")
       


    elif choice =="2":
       print("Starting data analysis...")
       threshold_days = int(input("Enter resolution days:"))
       resolution_days = [3, 8, 5, 12, 4]
       total_complaints = len(resolution_days)
       Total_days = 0

       complaint_matches = 0
       for complaints in resolution_days:
           if complaints > threshold_days:
              complaint_matches = complaint_matches + 1

       for complaints in resolution_days:
          Total_days = Total_days + complaints

       average_days = Total_days/total_complaints

       print(f"the average days for complaint resolution is {average_days}")


            
        
            
              
       print(f"{complaint_matches} complaints took more than {threshold_days} days to resolve")
              


    elif choice =="3":
        print("Goodbye")
        break
     
    else : 
        print("Invalid selection. Please choose from the Menu")