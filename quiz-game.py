import json
import os

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
    def __init__(self, file_path="state.json"):
        self.file_path = file_path
        self.quiz_list = []
        self.best_score = 0       

        self.load_state()

    def load_state(self):
        if not os.path.exists(self.file_path):
            print("기존 데이터 파일이 없어 새로 생성합니다")
            return
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)

                self.quiz_list = [
                    Quiz(q["problem"], q["choices"], q["answer"])
                    for q in data.get("quizzes", [])
                ]
        except (json.JSONDecodeError, KeyError):
            print("데이터 파일 읽기 오류. 파일을 초기화합니다")

    def save_state(self):
        data = {
            "best_score": self.best_score,
            "quizzes": [
                {
                    "problem": q.problem,
                    "choices": q.choices,
                    "answer": q.answer
                } for q in self.quiz_list
            ]
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def solve_quiz(self):

        if not self.quiz_list:
            print("퀴즈가 없습니다.")
            return
        
        score = 0
        
        for quiz in self.quiz_list:
            quiz.display_problem()
            user_answer = get_valid_number("정답 번호를 입력하세요: ", 1, len(quiz.choices))
            if quiz.check_answer(user_answer):
                print("정답입니다!\n")
                score += 1
            else:
                print("틀렸습니다.\n")

        print(f"당신의 점수는 {score}/{len(self.quiz_list)}입니다.")

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
        else:
            print(f"최고 점수는 {self.best_score}입니다.")

        self.save_state()

    def add_quiz(self):
        print("새로운 퀴즈 추가하기")

        while True:
            problem = input("문제를 입력하세요: ").strip()
            if problem:
                break
            print("문제는 비어 있을 수 없습니다")

        choices = []
        print("보기를 입력하세요")
        while len(choices) < 4:
            choice = input(f"{len(choices) + 1}번 보기: ").strip()
            if not choice : 
                print("보기는 공백일 수 없습니다")
                continue
            choices.append(choice)

        answer = get_valid_number(f"정답 번호를 입력하세요: ", 1, 4)

        new_quiz = Quiz(problem, choices, answer)
        self.quiz_list.append(new_quiz)

        self.save_state()
    
    def load_quizzes(self):
        if not self.quiz_list:
            print("퀴즈가 없습니다.")
            return
        
        print(f"저장된 퀴즈 목록 (총 {len(self.quiz_list)}개): ")
        for i, quiz in enumerate(self.quiz_list, 1):
            print(f"{i}. {quiz.problem}")

    def score_board(self):
        if self.best_score == 0:
            print("아직 최고 점수가 없습니다.")
            return
        
        print(f"현재 최고 점수: {self.best_score}")

quiz1 = Quiz("김시현이 좋아하는 색깔은?", ["빨간색", "파란색", "노란색", "초록색"], 3)
quiz2 = Quiz("김시현이 밴드부에서 맡고 있는 악기는?", ["드럼", "베이스", "기타", "키보드"], 1)
quiz3 = Quiz("김시현이 가장 좋아하는 동물은?", ["강아지", "고양이", "토끼", "햄스터"], 2)
quiz4 = Quiz("김시현이 배워본 적 없는 언어는?", ["영어", "일본어", "러시아어", "프랑스어"], 3)
quiz5 = Quiz("김시현이 대학에서 전공하는 것은?", ["컴퓨터공학", "화학", "심리학", "물리학"], 4)

quiz_list = [quiz1, quiz2, quiz3, quiz4, quiz5]

def get_valid_number(prompt, min_val, max_val):
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            print("입력이 비어 있습니다. 다시 입력해주세요.")
            continue

        if not user_input.isdigit():
            print("유효한 숫자를 입력해주세요.")
            continue

        user_answer = int(user_input)

        if user_answer < min_val or user_answer > max_val:
            print(f"{min_val}에서 {max_val} 사이의 숫자를 입력해주세요.")
            continue

        return user_answer