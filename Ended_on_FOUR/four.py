def main():
    
    name = input("Enter Anything in String : ")
    length = len(name)

    num_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten"
    }
    print(f"{name} has {num_words[length]} Characters")
    while length != 4:
        word = num_words.get(length, "")
        if word:
            print(f"{word} has {len(word)} characters.")
            length = len(word)
        else:
            print("Length should be under 10 char.")
            main()
    if length == 4:
        print("four has 4 characters.  That means Everything Ended on FOUR")

main()
