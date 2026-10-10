import time
import random

def mistake(random_sentence, user_sentence):
    error = 0
    for i in range(len(random_sentence)):
        try:
            if random_sentence[i] != user_sentence[i]:
                error += 1
        except IndexError:
            error += 1

    if len(user_sentence) > len(random_sentence):
        error += len(user_sentence) - len(random_sentence)

    return error


def speed_time(start_time, end_time, user_sentence):
    time_delay = end_time - start_time

    if time_delay <= 0:
        return 0

    speed = (len(user_sentence) / 5) / (time_delay / 60)
    return round(speed, 2)


def accuracy(random_sentence, user_sentence):
    total_chars = max(len(random_sentence), len(user_sentence))

    if total_chars == 0:
        return 100.0

    errors = mistake(random_sentence, user_sentence)

    accuracy_percentage = (
                                  (total_chars - errors) / total_chars
                          ) * 100

    return round(accuracy_percentage, 2)


if __name__ == '__main__':
    english_sentence = [
        "The quick brown fox jumps over the lazy dog",
        "Pack my box with five dozen liquor jugs.",
        "A bird in the hand is worth two in the bush.",
        "Caught between a rock and a hard place."
    ]
    german_sentence = [
        "A aa Apfel(apple), B bay Banane(banana), C tsay Couch(couch), D day Deutschland(germany), E ey Elefant(elephant), F eff Fisch(fish), G gay Gitarre(guitar), H ha Haus(house), I e Igel(hedgehog), J yott Joghurt(yoghurt), K ka Kaffee(coffee), L ell Liebe(love), M emm Mann(man), N en Nagel(nail), O o Orange(orange), P pay Pinguin(penguin), Q ku Quiz(quiz), R err Rot(red), S ess Sonne(sun), T tay Tee(tea), U uu Uhr(clock), V fau Vogel(bird), W way Wolke(cloud), X iks Xylofon(xylophone), Y upsilon Yak(yak), Z tset Zebra(Zebra), Ä eyyy Bär(Bear), Ö eyo Öl(Oil), Ü eyu fünf(five), ß ess-tset Fuß(foot)",
        "Hallo, Guten Morgen, Guten Tag, Guten Abend, Gute Nacht, Tschüss, Auf Wiedersehen, Bis bald, Bis morgen, Willkommen",
        "Danke, Vielen Dank, Bitte, Entschuldigung, Es tut mir leid, Ja, Nein, Vielleicht, Natürlich, Kein Problem",
        "Wie geht es Ihnen?,  Wie geht's?, Mir geht es gut., Sehr gut, Nicht so gut, Ich verstehe., Ich verstehe nicht., Noch einmal, bitte., Langsam, bitte., Sprechen Sie Englisch?"
    ]

    while True:
        check_user = input("\nReady to test: yes / no: ").strip().lower()
        enter_language = input("\nEnter the language en(English) / de(German): ").strip().lower()

        if check_user == 'yes':

            random_sentence = random.choice(english_sentence)
            if enter_language == 'en':
                random_sentence = random.choice(english_sentence)
            elif enter_language == 'de':
                random_sentence = random.choice(german_sentence)
            else:
                print("\nWe support only two language for now!")

            print("\n***** Typing Test *****")
            print("Type the following sentence:")
            print(random_sentence)
            print()

            start_time = time.perf_counter()
            user_sentence = input("Enter: ")
            end_time = time.perf_counter()
            total_time = round(end_time - start_time, 2)

            print("\n****** Test Results ******")
            print("Time Taken: ", total_time, "seconds")
            print('Speed: ', speed_time(start_time, end_time, user_sentence), 'WPM')
            print('Error: ', mistake(random_sentence, user_sentence))
            print("Accuracy:", accuracy(random_sentence, user_sentence), "%")

        elif check_user == 'no':
            print("\nThank you for using Python Typing Master!")
            break

        else:
            print("\nInvalid input! Please enter yes or no.")
