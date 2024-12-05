print ("Hà Mạnh Dũng")
print("235752021610006")
def append_text_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')
def display_file_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Nội dung của tệp:")
        print(content)
filename = input("Nhập tên tệp: ")
text = input("Nhập văn bản muốn nối thêm: ")
append_text_to_file(filename, text)
display_file_content(filename)
