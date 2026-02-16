def shutdown(user_input):
    if user_input == "Yes":
        print("Shutting down")
    elif user_input == "No":
        print("Abort shut down")
    else: 
        print ("Sorry")
user_input = input("Do you want to shutdown?(Yes/No): ")
shutdown(user_input)