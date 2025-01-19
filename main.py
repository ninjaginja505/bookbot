def count_words(book):
    return len(book.split())

def letter_count(book):
    letter_dict = {}
    letter_dict["a"] = book.lower().count("a")
    letter_dict["b"] = book.lower().count("b")
    letter_dict["c"] = book.lower().count("c")
    letter_dict["d"] = book.lower().count("d")
    letter_dict["e"] = book.lower().count("e")
    letter_dict["f"] = book.lower().count("f")
    letter_dict["g"] = book.lower().count("g")
    letter_dict["h"] = book.lower().count("h")
    letter_dict["i"] = book.lower().count("i")
    letter_dict["j"] = book.lower().count("j")
    letter_dict["k"] = book.lower().count("k")
    letter_dict["l"] = book.lower().count("l")
    letter_dict["m"] = book.lower().count("m")
    letter_dict["n"] = book.lower().count("n")
    letter_dict["o"] = book.lower().count("o")
    letter_dict["p"] = book.lower().count("p")
    letter_dict["q"] = book.lower().count("q")
    letter_dict["r"] = book.lower().count("r")
    letter_dict["s"] = book.lower().count("s")
    letter_dict["t"] = book.lower().count("t")
    letter_dict["u"] = book.lower().count("u")
    letter_dict["v"] = book.lower().count("v")
    letter_dict["w"] = book.lower().count("w")
    letter_dict["x"] = book.lower().count("x")
    letter_dict["y"] = book.lower().count("y")
    letter_dict["z"] = book.lower().count("z")
    letter_dict[" "] = book.lower().count(" ")
    return letter_dict

def sort_letters(dictionary):
    letters = []
    for letter, number in dictionary.items():
        if letter != " ":
            letters.append({"letter": letter, "number": number})
    letters.sort(reverse=True, key=sort_key)
    return letters

def sort_key(dict):
    return dict["number"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document")
        print("")
        for dict in sort_letters(letter_count(file_contents)):
            letter = dict["letter"]
            number = dict["number"]
            print(f"The '{letter}' character was found {number} times")
        print("--- End report ---")

main()