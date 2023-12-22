def new_year_resolution_bot(choice, resolutions):
    
    if choice == 1:
        resolutions.append(("Reduce phone time", "Better eyesight, less headache"))

    elif choice == 2:
        resolutions.append(("Go for a 30-minute walk each day", "Better mood, better health, better memory"))

    elif choice == 3:
        resolutions.append(("Practice gratitude daily", "Improved mental well-being, increased positivity"))

    elif choice == 4:
        resolutions.append(("Learn a new skill or hobby", "Increased creativity, personal growth, sense of accomplishment"))

    elif choice == 5:
        resolutions.append(("Ensure 7-8 hours of sleep each night", "Improved focus, better immune function, overall well-being"))

    elif choice == 6:
        resolutions.append(("Limit social media use", "Reduced stress, improved sleep quality"))

    elif choice == 7:
        resolutions.append(("Eat more fruits and vegetables", "Enhanced nutrition, better digestion, increased energy"))

    elif choice == 8:
        resolutions.append(("Read a book each month", "Mental stimulation, expanded knowledge, stress reduction"))

    elif choice == 9:
        resolutions.append(("Meditate for 10 minutes daily", "Reduced stress, improved focus, enhanced emotional well-being"))

    elif choice == 10:
        resolutions.append(("Volunteer for a cause", "Increased happiness, sense of purpose, social connections"))

    elif choice == 11:
        resolutions.append(("Drink more water", "Improved hydration, better skin health, enhanced metabolism"))

    elif choice == 12:
        resolutions.append(("Connect with friends and family regularly", "Stronger relationships, increased social support"))

    elif choice == 13:
        resolutions.append(("Set and achieve small goals weekly", "Increased motivation, sense of accomplishment"))

    elif choice == 14:
        resolutions.append(("Take breaks and stretch during work", "Improved productivity, reduced physical strain"))

    elif choice == 15:
        resolutions.append(("Learn a new language", "Cognitive benefits, enhanced communication skills"))

    else:
        print("Invalid choice. Please select a valid option.")


# Main loop
chosen_resolutions = []

while True:
    
    print("Welcome to the New Year Resolution Bot!")
    print("Choose a resolution option:\n")
    print("1. Reduce phone time")
    print("2. Go for a 30-minute walk each day")
    print("3. Practice gratitude daily")
    print("4. Learn a new skill or hobby")
    print("5. Ensure 7-8 hours of sleep each night")
    print("6. Limit social media use")
    print("7. Eat more fruits and vegetables")
    print("8. Read a book each month")
    print("9. Meditate for 10 minutes daily")
    print("10. Volunteer for a cause")
    print("11. Drink more water")
    print("12. Connect with friends and family regularly")
    print("13. Set and achieve small goals weekly")
    print("14. Take breaks and stretch during work")
    print("15. Learn a new language")
    

    choice = int(input("\nEnter your choice (1-15), or enter 0 to exit and view your resolutions: "))

    if choice == 0:
        print("\nExiting the New Year Resolution Bot. Here are your chosen resolutions:\n")
        for resolution, benefits in chosen_resolutions:
            print(f"\nResolution: {resolution}")
            print(f"Benefits: {benefits}")
        print("\nGoodbye!")
        break

    new_year_resolution_bot(choice, chosen_resolutions)
