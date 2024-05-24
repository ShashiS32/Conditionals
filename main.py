response = str(input(""))


if "." in response:
    parts = response.split(".", 1)


    if len(parts) > 1:
        result = parts[1]
    else:
        result = ""

    print(f"image/{result}")
