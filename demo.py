
b = True
while b:
    prompt = input("Enter a prompt: ")
    if(len(prompt) < 7):
        print(f"{prompt} is too short")
        continue
    else:
        print(f"{prompt} is ok")
        b = False
else:
    print("Goodbye")

