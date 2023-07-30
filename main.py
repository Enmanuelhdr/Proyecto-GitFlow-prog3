from PIL import Image
import os


downloadsFolder = "C:/Users/ehdel/Downloads/"
picturesFolder = "C:/Users/ehdel/Pictures/"
removeDuplicate = False

if __name__ == '__main__':
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            if removeDuplicate:
                os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "C:/Users/ehdel/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)

        if extension in [".mp4"]:
            musicFolder = "C:/Users/ehdel/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)