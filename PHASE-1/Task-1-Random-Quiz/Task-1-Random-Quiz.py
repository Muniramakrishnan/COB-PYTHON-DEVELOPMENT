import random

# Define a list of 30 questions and their corresponding answers
questions = [
    {"question": "What is the currency of China?", "answer": "Yuan"},
    {"question": "Who is the founder of the Red Cross?", "answer": "Henri Dunant"},
    {"question": "When and where was the Red Cross established?", "answer": "May 21, 1881, Washington, D.C."},
    {"question": "Which is the disease caused by hemoglobin deficiency?", "answer": "Anemia"},
    {"question": "Who started making Qutub Minar?", "answer": "Qutub-ud-din aibak"},
    {"question": "Who was the founder of Banaras Hindu University?", "answer": "Madan Mohan Malviya"},
    {"question": "Who was the author of economics?", "answer": "Chanakya (Kautilya)"},
    {"question": "Where is Vivekananda Memorial located?", "answer": "Kanyakumari"},
    {"question": "Where is the headquarters of SAARC located?", "answer": "Kathmandu, Nepal"},
    {"question": "How many countries are members of SAARC?", "answer": "8 (India, Nepal, Bangladesh, Sri Lanka, Maldives, Bhutan, Pakistan, Afghanistan)"},
    {"question": "Who built the Grant-Trunk Road? ", "answer": "Chandragupta Maurya"},
    {"question": "Which disease is caused by deficiency of Vitamin ‘B’?", "answer": "BeriBeri"},
    {"question": "Which disease is caused by deficiency of Vitamin ‘C’?", "answer": "Scurvy"},
    {"question": "Which disease is caused by deficiency of vitamin ‘D’?", "answer": "Rickets"},
    {"question": "Which vitamin deficiency does not cause blood clotting?", "answer": "Vitamin ‘K’"},
    {"question": "Which disease is caused by deficiency of Vitamin ‘E’?", "answer": "Infertility"},
    {"question": "What is the chemical name of Vitamin ‘C’?", "answer": "Ascorbic acid"},
    {"question": "Which part of eye is donated during eye donation?", "answer": "Cornea"},
    {"question": "In which part of our body are red blood cells formed?", "answer": "Bone Marrow"},
    {"question": "When is National Science Day celebrated?", "answer": "28 February"},
    {"question": "Which instrument is used to measure blood pressure?", "answer": "Sphygmomanometer"},
    {"question": "Who presides over the joint sitting of the two houses of Parliament?", "answer": "Speaker"},
    {"question": "Who was the first Lok Sabha Speaker of India?", "answer": "Shri Ganesh Vasudev Mavalankar"},
    {"question": "Under which article of Indian constitution did Jammu and Kashmir give special status?", "answer": "Article 370"},
    {"question": "Which country is the largest producer of silver in the world?", "answer": "Mexico"},
    {"question": "Which is the smallest country in the world by area?", "answer": "Vatican City"},
    {"question": "Which is the capital of the federal territory of India, Dadra and Nagar Haveli?", "answer": "Silvassa"},
    {"question": "Which is the largest state of India in terms of area?", "answer": "Rajasthan"},
    {"question": "In which state is the Valley of Flowers?", "answer": "Uttarakhand"},
    {"question": "The Hopmen Cup is related to which game?", "answer": "Tennis"}]
def select_a_random_question():
    return random.choice(questions)


# Function to check the user's answer
def check_the_answer(question, user_answer):
    return user_answer.lower() == question["answer"].lower()


# Main quiz loop
def __main__():
    print("Welcome to the Random Quiz!")

    score = 0
    num_questions = 30  # Change this to set the number of questions in the quiz

    for i in range(num_questions):
        question = select_a_random_question()
        print("\nQuestion:", question["question"])
        user_answer = input("Your Answer: ")

        if check_the_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Wrong. The correct answer is:", question["answer"])

    print("\nQuiz Complete!")
    print("Your Score:", score, "/", num_questions)


if __name__ == "__main__":
    __main__()
