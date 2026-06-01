def chatbot ():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi! ")

        elif user == "how are you":
            print("Chatbot: I am fine. Thank you!")
            
        elif user == "what is your name ?" :
            print ("Chatbot: My name is Harshni AI")
            
        elif user == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()