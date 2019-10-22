def create_file(file_name, n):
    x = open(file_name, "w")
    for i in range(n):
        x.write(str(i+1)+str("\n"))
    x.close()

create_file("jbd.txt", 5)
