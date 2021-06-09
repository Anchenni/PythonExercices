from Question import Question


question_prompt = [
    "1. Which of these U.S. states does NOT border Canada?\n(a) Alaska\n(b) Minnesota\n(c) Maine\n(d) Indiana\n\n",
    "2. Which of these countries was NOT a part of the Soviet Union?\n(a) Belarus\n(b) Poland\n(c) Georgia\n(d) Ukraine\n\n",
    "3. Which of these cities is NOT a national capital?\n(a) Prague\n(b) Cairo\n(c) Bangkok\n(d) Sydney\n\n",
    "4. Which of these cities DOESN'T border the Mediterranean Sea?\n(a) Monaco\n(b) Lisbon\n(c) Alexandria\n(d) Barcelona\n\n",
    "5. Which of these countries was NEVER part of the British Empire?\n(a) Thailand\n(b) Ireland\n(c) Kenya\n(d) New Zealand\n\n",
    "6. Which one of these cities is NOT in the Southern Hemisphere?\n(a) Brisbane\n(b) Colombo\n(c) Brasilia\n(d) Johannesburg\n\n",
    "7. Which one of these countries is NOT in Central America?\n(a) Honduras\n(b) Panama\n(c) Suriname\n(d) Belize\n\n",
    "8. Which of these cities does NOT border the Great Lakes?\n(a) Cleveland\n(b) Toronto\n(c) Chicago\n(d) Pittsburgh\n\n",
    "9. Which of these countries is NOT majority-Muslim?\n(a) Ethiopia\n(b) Indonesia\n(c) Albania\n(d) Morocco\n\n",
    "10. Which of these mountain ranges is NOT in Europe?\n(a) The Alps\n(b) The Pyrenees\n(c) Atlas Mountains\n(d) Carpathian Mountains\n\n"
]

questions = [
    Question(question_prompt[0],"d"),
    Question(question_prompt[1],"b"),
    Question(question_prompt[2],"d"),
    Question(question_prompt[3],"b"),
    Question(question_prompt[4],"a"),
    Question(question_prompt[5],"b"),
    Question(question_prompt[6],"c"),
    Question(question_prompt[7],"d"),
    Question(question_prompt[8],"a"),
    Question(question_prompt[9],"c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "answer: ")
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    for question in questions:
        print(question.prompt)
        print("the answer is: " + question.answer)

run_test(questions)



