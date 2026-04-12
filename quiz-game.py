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
    
    quiz1 = Quiz("김시현이 좋아하는 색깔은?", ["빨간색", "파란색", "노란색", "초록색"], 3)
    quiz2 = Quiz("김시현이 밴드부에서 맡고 있는 악기는?", ["드럼", "베이스", "기타", "키보드"], 1)
    quiz3 = Quiz("김시현이 가장 좋아하는 동물은?", ["강아지", "고양이", "토끼", "햄스터"], 2)
    quiz4 = Quiz("김시현이 배워본 적 없는 언어는?", ["영어", "일본어", "러시아어", "프랑스어"], 3)
    quiz5 = Quiz("김시현이 대학에서 전공하는 것은?", ["컴퓨터공학", "화학", "심리학", "물리학"], 4)

    quiz_list = [quiz1, quiz2, quiz3, quiz4, quiz5]

class QuizGame:
    pass

