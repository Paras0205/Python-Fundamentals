# Write a function welcome_message that takes two parameters
# When you call this function:
# If both name and city are given → print:
# "Welcome, <name> from <city>!"
# If only name is given → use "Delhi" as default city

def wel_msg(name,city="Delhi"):
    print(f"Welcome,{name} from {city}")

wel_msg("Paras")