from datetime import datetime


def show_help():
    print("\nYou can ask me:")
    print("- Hello / Hi")
    print("- How are you")
    print("- What is your name")
    print("- What can you do")
    print("- Tell me the time")
    print("- Tell me the date")
    print("- Calculate")
    print("- Thank you")
    print("- Bye\n")


def calculate():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Chatbot: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Chatbot: Invalid operator.")
            return

        print(f"Chatbot: The result is {result}")

    except ValueError:
        print("Chatbot: Please enter valid numbers.")


def chatbot():
    print("=" * 40)
    print("          BASIC CHATBOT")
    print("=" * 40)
    print("Chatbot: Hello! I am your virtual assistant.")
    print("Chatbot: Type 'help' to see what I can do.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Chatbot: I'm doing well. Thanks for asking!")

        elif user_input == "what is your name":
            print("Chatbot: I am a simple Python chatbot.")

        elif user_input == "what can you do":
            print("Chatbot: I can answer basic questions, show date and time, and perform calculations.")

        elif user_input in ["help", "menu"]:
            show_help()

        elif user_input in ["time", "tell me the time"]:
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: The current time is {current_time}.")

        elif user_input in ["date", "tell me the date"]:
            current_date = datetime.now().strftime("%d %B %Y")
            print(f"Chatbot: Today's date is {current_date}.")

        elif user_input in ["calculate", "calculator"]:
            calculate()

        elif user_input in ["thank you", "thanks"]:
            print("Chatbot: You're welcome!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that. Type 'help' to see available commands.")


chatbot()