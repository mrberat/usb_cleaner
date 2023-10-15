import os
import shutil
import zipfile

def usb_cleaner():
    dizin = input("dizin yolunuzu giriniz")
    os.chdir("{}".format(dizin))
    liste = os.listdir("{}".format(dizin))
    print(liste)
    zip_dosyasi = zipfile.ZipFile("zip_dosyası.zip","w")


    for i in liste:
        zip_dosyasi.write("{}".format(i))
    print("the files have been successfully zip formatted.")

    for i in liste:
        if i.endswith(".zip"):
            print("there are no files to delete...")
        else:
            pass
    shutil.rmtree("{}".format(dizin))
    print("files have been deleted successfully...")

    print("completed...")

usb_cleaner()


