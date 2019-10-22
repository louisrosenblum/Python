sentence = input(": ")

a_ = 0
e_ = 0
i_ = 0
o_ = 0
u_ = 0

for i in range(len(sentence)):
        if "a" == sentence[i]:
            a_ = a_ + 1
        elif "e" == sentence[i]:
            e_ = e_ + 1
        elif "i" == sentence[i]:
            i_ = i_ + 1
        elif "o" == sentence[i]:
            o_ = o_ + 1
        elif "p" == sentence[i]:
            u_ = u_ + 1
        else:
            continue
        

print(a_ + e_ + i_ + o_ + u_)
