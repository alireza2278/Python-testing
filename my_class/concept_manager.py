# کانسپت منیجر برای انجام کاری قبل از دستورات با انتر و بعد اجرای دستورات با اگزیت
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("The file was opened!")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("The file was closed!")
        self.file.close()


with FileManager("text.txt", "w") as f:
    f.write("hello word!")
