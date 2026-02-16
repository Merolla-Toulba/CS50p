ending = input("File name: ").strip().lower()

try:
    name, extension = ending.split(".")
except ValueError:
    print("application/octet-stream")
else:
    match extension:
        case "jpg" | "gif" | "jpeg" | "png":
            print(f"image/{extension}")
        case "pdf" | "txt" | "zip":
            print(f"application/{extension}")

