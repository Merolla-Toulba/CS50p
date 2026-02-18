ending = input("File name: ").strip().lower()

if ending.endswith((".gif", ".png")):
    words = ending.split(".")
    print(f"image/{words[len(words) - 1]}")

elif ending.endswith((".jpeg", ".jpg")):
    print("image/jpeg")

elif ending.endswith((".pdf", ".zip")):
    words = ending.split(".")
    print(f"application/{words[len(words) - 1]}")

elif ending.endswith(".txt"):
    print("text/plain")

else:
    print("application/octet-stream")
