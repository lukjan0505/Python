import  os
import datetime
def main():
    # 1 sposób
    # try:
    #     sciezka_do_pliku = r"C:\Users\lukas\PycharmProjects\Python\KursPodstawyPythona\przyklad.txt"
    #     f = open(sciezka_do_pliku)
    #     print(2/0)
    #     print(f.read())
    # except ZeroDivisionError as e:
    #     print(e)
    # finally:
    #     f.close()
    #     print(f.closed)

    # 2 sposób
    sciezka_do_pliku = r"C:\Users\lukas\PycharmProjects\Python\KursPodstawyPythona\przyklad.txt"
    with open(sciezka_do_pliku, "w") as f: # r - read, w - write, a - append (dodawanie)
        f.writelines(["Piąty wiersz\n", "Szósty wiersz\n"])
        f.write("Sódmy wiersz\n")
    print(f.closed)

    # print(os.path.exists(sciezka_do_pliku))
    print(os.listdir(r"C:\Users\lukas\PycharmProjects\Python\KursPodstawyPythona\tekstowe"))
    print(os.path.join("Przykład1", "Przykład2", "Przykład3"))

    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(sciezka_do_pliku)
    data_modyfikacji = datetime.datetime.fromtimestamp(mtime) # 2023-04-11 14:41:50
    print(data_modyfikacji)

if __name__ == "__main__":
    main()