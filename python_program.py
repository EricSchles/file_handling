import time

start = time.time()
end = time.time()
while end - start < 3:
    with open("thing.txt", "w") as f:
        f.write("hello")
    end = time.time()
print("done")
