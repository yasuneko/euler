
def answer(chunk, word):
    subchunk = chunk

    while word in subchunk:
        front = subchunk.find(word)
        back = front + len(word)
        smallchunk = subchunk[front:back + len(word) - 1]
        if smallchunk.rfind(word) > front:
            front_tmp = front + smallchunk.rfind(word)
            back_tmp = front_tmp + len(word)
            if (subchunk[:front] + subchunk[back:]) > (subchunk[:front_tmp] + subchunk[back_tmp:]):
                front = front + front_tmp
                back = front + len(word)
        subchunk = subchunk[:front] + subchunk[back:]
    return subchunk

print "answer: ", answer("lololololo", "lol")
print "answer: ", answer("ololololol", "olo")
print "answer: ", answer("lol", "lol")
print "answer: ", answer("goodgooogoogfogoood", "goo")
