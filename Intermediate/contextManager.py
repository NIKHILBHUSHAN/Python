from contextlib import contextmanager

with open("test.txt","w") as f:
    f.write("Hello World")

class ManagedFile:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):
        print("Entering context: Opening file...")
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.file:
            self.file.close()
        print("Exiting context: Closed file.")
        if exc_type is not None:
            print(f"Handled exception: {exc_val}")
        return True

with ManagedFile("notes.txt","w") as f:
    f.write("Custom context manager content")

@contextmanager
def open_managed_file(filename,mode):
    f=open(filename,mode)
    try:
        print("Generator Context: Opening file...")
        yield f
    finally:
        f.close()
        print("Generator Context: File closed.")

with open_managed_file("gen_notes.txt","w") as f:
    f.write("Generator context manager content")