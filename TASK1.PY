# Функція для відкриття файлу з обробкою помилок
def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print(f"File {file_name} wasn't opened!")
        return None
    else:
        print(f"File {file_name} was opened!")
        return file

# Створення та запис у файл TF1_1
file1_name = "TF1_1.txt"
file2_name = "TF1_2.txt"

file1 = open_file(file1_name, "w")
if file1 is not None:
    file1.write("Hello, world! This is a test file. Let's check how it works.")
    print("Information was successfully added to TF1_1.txt!")
    file1.close()
    print("File TF1_1.txt was closed!")

# Читання TF1_1 і запис слів у TF1_2
file1 = open_file(file1_name, "r")
file2 = open_file(file2_name, "w")

if file1 is not None and file2 is not None:
    import string
    content = file1.read()
    words = content.split()

    # Видалення розділових знаків і запис кожного слова у файл TF1_2
    for word in words:
        word = word.strip(string.punctuation)  # Видалення розділових знаків
        if word:
            file2.write(word + '\n')

    file1.close()
    file2.close()
    print("Files were closed!")

# Читання TF1_2 і вивід його вмісту
file3 = open_file(file2_name, "r")
if file3 is not None:
    for line in file3:
        print(line.strip())  # Друк без зайвих переносів
    file3.close()
    print("File TF1_2.txt was closed!")
