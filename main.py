response = str(input("Greetings: "))

if "hello" in response.lower():
    print("0$")

elif response[0].lower()== "h":
    print ("20$")
else:
    print("100$")
