from os import path

def wordcount(path, file):
    file = open(path + file, "r")
    lines = file.readlines()  #.replace("\n", " ")
    line_count = len(lines)
    character_count = 0
    word_count = 0
    for line in lines:
        print("line", len(line), line)
        character_count += len(line)

        words = line.split()
        print("words", len(words), words)
        word_count += len(words)

    file.close()

    return line_count, word_count, character_count


def lettercount(path, file):
    line_count = 0
    character_count = 0
    word_count = 0
    with open(path + file, "r") as file:
        lines = file.readlines()
        line_count = len(lines)

        for line in lines:
            word_count += len(line.split())
            character_count += len(line)

    return line_count, word_count, character_count


if __name__ == '__main__':
    basepath = path.dirname(__file__)
    print(basepath)

    generic_resource_path = path.abspath(path.join(basepath, '..', '..', '..', 'resources')) + "/"
    print(generic_resource_path)

    file_name = "wordCountText"

    line_count, word_count, character_count = wordcount(generic_resource_path, file_name)
    print("wordcount", line_count, word_count, character_count)

    line_count1, word_count1, character_count1 = lettercount(generic_resource_path, file_name)
    print("lettercount", line_count1, word_count1, character_count1)