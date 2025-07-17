# Prompting user for their input about the weather and providing advice based on their response
user_input = input("What's the weather like today?").lower()

if user_input == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_input =="rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_input == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")