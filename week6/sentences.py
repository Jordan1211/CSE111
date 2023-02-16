import random

# Create a list of strings and assign
# the list to a variable named words.
words_example = ["boy", "girl", "cat", "dog", "bird", "house"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
word_example = random.choice(words_example)

# This could be any word from any source.
cap_word_example = "horse"

# Call the capitalize method which will
# capitalize the first letter of the word.
cap_word = cap_word_example.capitalize()

def main():
# attempting to work through loop
    quantity_list = [1,1,1,2,2,2]
    tense_list = ["past", "present", "future", "past", "present", "future"]
    sentence = create_sentence(quantity_list, tense_list)

def create_sentence(quantity_list, tense_list):
    for (quantity,tense) in zip(quantity_list, tense_list):
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense)
        prep_phrase1 = get_prepositional_phrase(quantity)
        prep_phrase2 = get_prepositional_phrase(quantity)
        adverb = get_adverb()
        adjective = get_adjective()
        if quantity == 1:
            quantity = "single"
        else:
            quantity = "plural"
        
        print(f'{quantity}, {tense}: {determiner.capitalize()} {adjective} {noun} {prep_phrase1} {adverb} {verb} {prep_phrase2}.')

# # a.	single	past
#     quantity = 1
#     tense = "past"
#     determiner = get_determiner(quantity)
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)
#     print(f'Single Past Tense: {determiner.capitalize()} {noun} {verb}.')

# # b.	single	present
#     tense = "present"
#     determiner = get_determiner(quantity)
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)
#     print(f'Single Present Tense: {determiner.capitalize()} {noun} {verb}.')

# # c.	single	future
#     tense = "future"
#     determiner = get_determiner(quantity)
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)
#     print(f'Single Future Tense: {determiner.capitalize()} {noun} {verb}.')

# # d.	plural	past
#     quantity = 2
#     tense = "past"
#     determiner = get_determiner(quantity)
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)
#     print(f'Plural Past Tense: {determiner.capitalize()} {noun} {verb}.')

# # e.	plural	present
#     tense = "present"
#     determiner = get_determiner(quantity)
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)
#     print(f'Plural Present Tense: {determiner.capitalize()} {noun} {verb}.')

# # f.	plural	future
#     tense = "future"
#     determiner = get_determiner(quantity)
#     noun = get_noun(quantity)
#     verb = get_verb(quantity, tense)
#     print(f'Plural Future Tense: {determiner.capitalize()} {noun} {verb}.')

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """    
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    # else:
        # words = Error

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_preposition()
    phrase = f"{preposition} {determiner} {noun}"
    return phrase

# exceeding requirements if time permits:
def get_adjective():
    """Return a randomly chosen adjectives
    from this list of adjectives:
        "amused", "delighted", "glad", "pleased", "charmed", 
        "grateful", "enthusiastic", "loving", "marvelous", "annoyed", 
        "livid", "bitter", "determined", "inspired", "creative", 
        "healthy", "renewed", "vibrant", "strengthened", "motivated", 
        "focused", "invigorated", "refreshed"
    Return: a randomly chosen adjective.
    """
    words = ["amused", "delighted", "glad", "pleased", "charmed", 
        "grateful", "enthusiastic", "loving", "marvelous", "annoyed", 
        "livid", "bitter", "determined", "inspired", "creative", 
        "healthy", "renewed", "vibrant", "strengthened", "motivated", 
        "focused", "invigorated", "refreshed"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
        "boldly", "bravely", "brightly", "cheerfully", "deftly", 
        "devotedly", "eagerly", "elegantly", "faithfully", "fortunately", 
        "gleefully", "gracefully", "happily", "honestly", "innocently", 
        "kindly", "merrily", "obediently", "perfectly", "politely"
    Return: a randomly chosen adverb.
    """
    words = ["boldly", "bravely", "brightly", "cheerfully", "deftly", 
        "devotedly", "eagerly", "elegantly", "faithfully", "fortunately", 
        "gleefully", "gracefully", "happily", "honestly", "innocently", 
        "kindly", "merrily", "obediently", "perfectly", "politely"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()