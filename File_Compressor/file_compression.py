__author__ = 'Pratik_Munot'

from tkinter import *
import tkinter.filedialog
import zlib,os,sys
loc = []
def browse():
    txt_file = tkinter.filedialog.askopenfilename(parent=window,initialdir='D:\\')
    loc.append(txt_file)
    print("File Selected Successfully - "+loc[-1])

    print("\nSelect level of File Compession(0-9)")

def compressfile():
    if len(loc)>0:
        level = print_item_values()
        print("Level of file compression -",level)
        print("Compression Started.....")
        str_object1 = open(loc[-1], 'rb').read()
        str_object2 = zlib.compress(str_object1, 9)
        f = open('compressed_file', 'wb')
        f.write(str_object2)
        f.close()
        if 'compressed_file' in os.listdir():
            print("File compresssed successfully\nFile Stats - \n")
            text = open(loc[-1], 'r').read()
            size = sys.getsizeof(text) / 1000
            print(f"Raw size of file : {round(size, 2)} KB")

            size1 = list(os.stat(loc[-1]))[6] / 1000
            print(f"Actual size of file on disk: {round(size1, 2)} KB")

            size2 = sys.getsizeof(str_object2) / 1000
            print(f"Size of file after compression : {round(size2, 2)} KB")
            print("Compression ratio - ",round((size1-size2)/size1*100,2),"%")
            print("------------------------------------------------")
            print("Compressed file successfully saved at current working directory besides the program")
        else:
            print("Compression failed")
    else:
        print("File not selected")


def decompressfile():
    if 'compressed_file' in os.listdir():
        str_object1 = open('compressed_file', 'rb').read()
        str_object2 = zlib.decompress(str_object1)
        loc2 = loc[-1]
        loc2 = loc2.split('/')
        loc2 = loc2[-1]
        loc2 = loc2.split('.')
        extn = loc2[-1]
        filename = "decompressed." + extn

        f = open(filename, 'wb')
        f.write(str_object2)
        f.close()
        if filename in os.listdir():
            print("Decompressed file at current working directory - ", filename)
        print()


# ----------------------   GUI  -----------------------------------
window = Tk()
window.title("Pratik's zlib Compression")
window.geometry("360x445")
print("Pythons zlib compressor works best on text file and other similar formats ")
print("So choose text file although you can still choose video or image or music file")
print("\n==================================================")
print("Please Select a large file - Click Browse Button")

lb1 = Label(window, text="Welcome to Pythons zlib Compressor", font=('arial', 13)).grid(row=0, columnspan=2, sticky=W, padx=5, pady=5)
lb1 = Label(window, text="_____________________________________", font=('arial', 12)).grid(row=1, columnspan=2, sticky=W, padx=5, pady=5)

lb2 = Label(window, text="Select file or Compression(.txt)", font=('arial', 11)).grid(row=2, column=0, sticky=W, padx=5, pady=5)
btn = Button(window, text="Browse file", width=15,command=browse)
btn.grid(row=2, column=1, sticky=W, padx=5, pady=5)

lb1 = Label(window, text="_____________________________________", font=('arial', 12)).grid(row=3, columnspan=2, sticky=W, padx=5, pady=5)
lb3 = Label(window, text="Select Compression level", font=('arial', 11)).grid(row=4, column=0, sticky=W, padx=5, pady=5)
lb3 = Label(window, text="0 = No compression \n 1 = least compression \n 9 = most amount of compression possible", font=('arial', 8)).grid(row=5, columnspan=2, sticky=W, padx=5, pady=5)


item_1 = IntVar()

def print_item_values():
    a = item_1.get()
    return a
item_1 = Spinbox(window, from_ = 0, to=9, width=15)
item_1.grid(row=4, column=1, sticky=W, padx=5, pady=5)

lb1 = Label(window, text="_____________________________________", font=('arial', 12)).grid(row=6, columnspan=2, sticky=W, padx=5, pady=5)

lb2 = Label(window, text="Start Compression", font=('arial', 11)).grid(row=7, column=0, sticky=W, padx=5, pady=5)
btn = Button(window, text="Compress", width=15,command=compressfile)
btn.grid(row=7, column=1, sticky=W, padx=5, pady=5)

lb1 = Label(window, text="_____________________________________", font=('arial', 12)).grid(row=8, columnspan=2, sticky=W, padx=5, pady=5)

lb2 = Label(window, text="Start Decompression", font=('arial', 11)).grid(row=9, column=0, sticky=W, padx=5, pady=5)
btn = Button(window, text="Decompress", width=15,command=decompressfile)
btn.grid(row=9, column=1, sticky=W, padx=5, pady=5)

lb1 = Label(window, text="_____________________________________", font=('arial', 12)).grid(row=10, columnspan=2, sticky=W, padx=5, pady=5)

def quit_program():
    window.quit()

btn = Button(window, text="Quit",width=15, command=quit_program)
btn.grid(row=11, column=0, sticky=W, padx=55, pady=5)

window.mainloop()
