user_val = raw_input("Enter number: ")
user_limit = raw_input("Enter limit: ")
val = int(user_val)
limit = int(user_limit)
if val > limit:
    raise Exception("Value is large")
else:
    raise Exception("Value is small")