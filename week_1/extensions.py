"""
Program that prompts the user for the name of a file and then outputs that file’s media type.
- if the file’s name ends, case-insensitively, in any of these suffixes:
    - .gif
    - .jpg
    - .jpeg
    - .png
    - .pdf
    - .txt
    - .zip
"""

def main():
    prompt = input("File name: ").strip().lower()

            
    if prompt.endswith(".jpg") or prompt.endswith(".jpeg"):
         print("image/jpeg")
    elif prompt.endswith(".gif"):
        print("image/gif")
    elif prompt.endswith(".png"):
        print("image/png")
    elif prompt.endswith(".pdf"):
        print("application/pdf")
    elif prompt.endswith(".txt"):
        print("text/plain")
    elif prompt.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

        

main()