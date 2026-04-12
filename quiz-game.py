class Quiz:
    def __init__(self, problem, choices, answer):
        self.problem = problem
        self.choices = choices
        self.answer = answer
    
    def display_problem(self):
        print(self.problem)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
    
    def check_answer(self, user_answer):
        return user_answer == self.answer
    

class QuizGame:
    pass

