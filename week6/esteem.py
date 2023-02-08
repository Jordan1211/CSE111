"""
The Rosenberg self-esteem scale is a self-esteem measure developed by the 
sociologist Morris Rosenberg in 1965. It is still used in social-science 
research today. To complete the measure, a person completes a survey that 
contains the following ten statements.

I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.
I am able to do things as well as most other people.
I feel I do not have much to be proud of.
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.
At times I think I am no good at all.

The person responds to each statement by choosing one of these four options: 
strongly disagree, disagree, agree, or strongly agree. 

The person’s response to each statement is worth 0–3 points, meaning the highest 
possible score is 10 * 3 = 30 points. If a person scores lower than 15 points, 
the person may have a problematic low self-esteem.

Notice that five of the statements (numbers 1, 2, 4, 6, 7) are positive and are 
scored like this:

Choice	Points
Strongly Disagree	0
Disagree	1
Agree	2
Strongly Agree	3

The other five statements (numbers 3, 5, 8, 9, 10) are negative 
and are scored like this:

Choice	Points
Strongly Disagree	3
Disagree	2
Agree	1
Strongly Agree	0

"""

def main():
    #introductory text:
    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')

    #Ask the user to enter in a certain format
    print('D = Strongly Disagree')
    print('d = Disagree')
    print('a = Agree')
    print('A = Strongly Agree')
    print()


    #Ask 10 questions from the self-esteem assment
    one = input('I feel that I am a person of worth, at least on an equal plane with others: ')
    two = input('I feel that I have a number of good qualities: ')
    three = input('All in all, I am inclined to feel that I am a failure: ')
    four = input('I am able to do things as well as most other people: ')
    five = input('I feel I do not have much to be proud of: ')
    six = input('I take a positive attitude toward myself: ')
    seven = input('On the whole, I am satisfied with myself: ')
    eight = input('I wish I could have more respect for myself: ')
    nine = input('I certainly feel useless at times: ')
    ten = input('At times I think I am no good at all: ')


    positive_questions = convert_positive_questions(one, two, four, six, seven)
    negative_questions = convert_negative_questions(three, five, eight, nine, ten)
    score = calculate_score(positive_questions, negative_questions)
    
    print()
    print(f'Your score is: {score}.')
    print(f'**A score below 15 may indicate problematic low self-esteem.**')
    print()


#Convert negative values
def convert_positive_questions(one, two, four, six, seven):
    postive_answers = [one, two, four, six, seven]
    answer = 0

    for i in postive_answers:
        if i == 'D':
            answer += 0
        elif i == 'd':
            answer += 1
        elif i == 'a':
            answer += 2
        elif i == 'A':
            answer += 3

    return answer

#Convert positive values
def convert_negative_questions(three, five, eight, nine, ten):
    negative_answers = [three, five, eight, nine, ten]
    answer = 0

    for i in negative_answers:
        if i == 'D':
            answer += 3
        elif i == 'd':
            answer += 2
        elif i == 'a':
            answer += 1
        elif i == 'A':
            answer += 0

    return answer

#Calculate total score
def calculate_score(positive_questions, negative_questions):
    total = positive_questions + negative_questions
    return total    


# Call main to start this program.
if __name__ == "__main__":
    main()