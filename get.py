# Developed By : Venkatesh E
# Reference No : 21003352
with open("text.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
