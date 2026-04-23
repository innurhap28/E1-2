## 프로젝트 개요

본 프로젝트는 Python의 객체 지향 프로그래밍을 활용하여 제작된 퀴즈 게임입니다. JSON 파일 입출력을 통해 퀴즈 데이터와 최고 점수 데이터의 영속성을 구현 했으며, 사용자가 직접 새로운 퀴즈를 추가하여 게임을 확장할 수 있도록 설계되었습니다. 

---
## 퀴즈 주제 선정 이유

#### 주제
나(김시현)에 대한 퀴즈

#### 선정 이유
피평가자인 나 자신을 주제로 퀴즈를 구성하여, 동료들이 평가를 하며 흥미를 가지고 참여할 수 있겠다고 생각했으며, 편안한 분위기 속에서 보다 솔직하고 적극적인 피드백이 이루어질 수 있을 것이라고 판단했습니다. 

---
## 실행 방법

1. 파이썬 설치 : Python 3.x 버전이 설치되어 있어야 합니다. 
2. 파일 준비 : 동일한 디렉토리에 `quiz_game.py`와 `main.py`가 있는지 확인합니다.
3. 프로그램 실행 : 터미널 또는 CMD에서 프로젝트 폴더로 이동한 후 아래 명령어를 입력합니다. 
```zsh
python main.py
```
4. 조작 : 화면에 출력되는 숫자 메뉴(1-5)를 입력하여 원하는 기능을 선택합니다. 


---
## 파일 구조

``` 파일 구조
E1-2/
├── quiz_game.py    # Quiz, QuizGame 클래스 정의 및 퀴즈 데이터
├── main.py         # 프로그램 실행 파일 (퀴즈 시작)
├── README.md       # 프로젝트 설명 문서
├── state.json      # 최고 점수 등 상태 저장 파일
├── .gitignore      # Git에서 제외할 파일 목록
└── screenshots/    # 실행 화면 캡쳐 이미지 폴더
```

---
## 데이터 파일 설명

#### 경로 
프로젝트 루트의 `state.json` 파일

#### 역할
프로그램의 상태를 유지하기 위해 사용되는 데이터 파일  
최고 점수 및 퀴즈 데이터를 보관하여 프로그램 종료 후에도 데이터가 유지되도록 합니다

#### 필드 구조 (스키마)
``` json
{
    "best_score": 0,
    "quizzes": [
        {
            "problem": "문제 내용",
            "choices": ["선지 1", "선지 2", "선지 3", "선지 4"],
            "answer": 1
        }
    ]
}
```

- `best_score` : 현재까지 플레이한 기록 중 가장 높은 점수를 저장합니다.
- `quizzes` : 기본 제공 퀴즈와 사용자가 추가한 퀴즈 객체들의 목록을 JSON 배열 형태로 저장합니다.
    - `problem` : 퀴즈의 질문 내용
    - `choices` : 4지선다형 보기 리스트
    - `answer` : 정답 번호 (정수형)

> 파일이 삭제되거나 손상된 경우, 프로그램 내부의 `get_default_quizzes()` 메서드를 통해 자동으로 기본 데이터를 복구합니다.

#### 데이터 구조 설계 이유
프로그램의 상태를 효율적으로 관리하기 위해 `best_score`와 `quizzes`두 필드로 구분하여 설계하였습니다. 

- `best_score` : 단일 값으로 관리되는 데이터로 최상위 필드로 분리
- `quizzes`: 여러 개의 퀴즈 데이터를 저장해야 하므로 리스트 구조로 구성, 각 퀴즈가 문제, 보기, 정답이라는 하나의 의미 단위를 가지므로 이를 하나의 객체로 묶어 배열에 저장하도록 설계

이러한 구조를 통해 데이터의 의미를 명확하게 표현할 수 있으며, 추가 및 확장에도 유연하게 대응할 수 있습니다. 

#### state.json 읽기/쓰기 흐름
프로그램 실행 시 `QuizGame` 객체가 생성되면서 `load_state()` 메서드가 호출됩니다. 이 과정에서 `state.json` 파일을 읽어 퀴즈 데이터와 최고 점수를 메모리에 불러옵니다.  
데이터 변경이 발생할 경우(퀴즈 추가 등), `save_state()` 메서드를 호출하여 현재 상태를 `state.json`파일에 다시 저장합니다.  
또한 파일이 존재하지 않거나 손상된 경우에는 기본 데이터를 생성한 뒤 `save_state()`를 통해 파일을 새로 생성합니다. 

---

## 코드 구조 및 설계

이 프로젝트는 객체 지향 프로그래밍 (OOP)를 기반으로 설계되었으며, 
주요 클래스는 `Quiz`와 `QuizGame`으로 구성되어 있습니다. 

- `Quiz` 클래스 : 하나의 퀴즈 데이터를 표현하는 클래스
- `QuizGame`클래스 : 퀴즈 게임의 전체 흐름과 기능을 관리하는 클래스
  

> 클래스를 사용하는 이유  
함수만으로 프로그램을 구성할 경우, 데이터와 기능이 분리되지 않아 코드 구조가 복잡해질 수 있습니다. 반면 클래스를 사용하면 각 요소의 책임을 명확히 나눌 수 있으며 기능 수정 시 다른 코드에 영향을 최소화 할 수 있도록 설계했습니다.

---
### 1. Quiz 클래스

하나의 퀴즈 데이터를 표현하는 클래스.  
문제, 보기, 정답을 속성으로 가지며, 문제 출력과 정답 판별 기능을 담당합니다. 

주요 메서드: 
- `display_problem` : 문제와 보기를 출력
- `check_answer` : 사용자가 입력한 답을 정답과 비교

---

### 2. QuizGame 클래스

전체 퀴즈 게임의 흐름을 관리하는 핵심 클래스.  

``` python
class QuizGame:
    def __init__(self, file_path="state.json"):
        self.file_path = file_path
        self.quiz_list = []
        self.best_score = 0       
        self.load_state()
```

### 2-1. 데이터 저장
``` python
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
```
`best_score`와 `quizzes` 데이터를 `state.json`에 저장합니다.  
퀴즈 객체 리스트를 JSON 형식에 맞게 변환하여 파일에 기록하도록 구현하였습니다. 

> JSON 파일을 사용하는 이유  
데이터를 구조화된 형태로 저장할 수 있어, 퀴즈 데이터와 최고 점수를 파일로 쉽게 관리할 수 있으며, 사람이 읽고 수정하기 쉬운 형식으로 사용자가 직접 데이터를 확인하는 데에도 용이합니다. 또한 리스트와 객체 구조를 표현할 수 있어 복잡한 데이터 저장이 가능합니다. 

### 2-2. 데이터 불러오기
``` python
   def get_default_quizzes(self):
        return [
            Quiz("김시현이 좋아하는 색깔은?", ["빨간색", "파란색", "노란색", "초록색"], 3),
            ... #(중략)
        ]

    def load_state(self):
        if not os.path.exists(self.file_path):
            print("기존 데이터 파일이 없어 새로 생성합니다")
            self.quiz_list = self.get_default_quizzes()
            self.save_state()
            return
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quiz_list = [
                    Quiz(q["problem"], q["choices"], q["answer"])
                    for q in data.get("quizzes", [])
                ]
        ...
```
JSON 파일을 불러와 기존 데이터를 복원합니다.  
기본 퀴즈 데이터는 `get_default_quizzes` 메서드에서 `Quiz` 객체(인스턴스) 형태로 생성됩니다. 
프로젝트 디렉토리에 `state.json`이 없을 경우, 해당 기본 퀴즈 데이터를 JSON 형식에 맞게 변환하여 파일을 자동 생성합니다.  

### 2-3. 게임 진행

- 퀴즈 풀기
    - 최초 실행 시 기본 퀴즈 5개가 제공됩니다. 
    - 퀴즈 추가 기능을 통해 문제가 추가된 경우, 추가된 퀴즈를 포함한 전체 퀴즈를 풀 수 있습니다.
- 퀴즈 추가
    - 사용자가 원하는 퀴즈를 추가할 수 있습니다. 
    - 퀴즈는 문제, 선지(4개), 정답(1-4 사이의 정수)로 이루어져 있습니다. 
    - 정상적으로 추가된 퀴즈는 state.json 파일에 퀴즈 데이터가 추가됩니다. 
- 퀴즈 목록
    - json 파일에 저장된 전체 퀴즈 개수 및 목록을 조회합니다.
- 최고 점수 확인
    - json 파일에 기록된 최고 점수를 확인할 수 있습니다. 
- 종료
    - 메뉴에서 종료 메뉴를 선택하여 프로그램을 종료할 수 있습니다. 
    - 퀴즈 진행 중에는 'q'를 눌러 즉시 종료할 수 있습니다. 


### 2-4 입력 처리(검증)

``` python 
def get_valid_number(prompt, min_val, max_val):
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            print("입력이 비어 있습니다")
            continue

        # 퀴즈 풀기 진행 중 프로그램 종료를 원할 시 'q'를 입력해서 종료
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다")
            exit()

        if not user_input.isdigit():
            print("유효한 숫자를 입력해주세요")
            continue

        user_answer = int(user_input)

        if user_answer < min_val or user_answer > max_val:
            print(f"{min_val}에서 {max_val} 사이의 숫자를 입력해주세요")
            continue

        return user_answer
```
입력 처리를 위해 `get_valid_number` 메서드를 설계하였습니다.  

`.strip()` 을 통해 입력된 값 앞 뒤의 공백을 제거하였으며, 
- 입력이 비어 있는 경우 
- 숫자가 입력되지 않은 경우
- 범위 내의 숫자가 아닌 경우  

위 세 가지 경우를 처리하였습니다. 

> 또한, 퀴즈를 풀고 있는 상황에서 도중에 프로그램을 종료하고 싶을 수 있겠다는 생각이 들어, 해당 메서드에 프로그램 종료를 위한 장치를 추가해 보았습니다. 

### 2-5. 예외 처리

파일 입출력은 외부 환경에 의존하기 때문에, 다양한 오류가 발생할 수 있습니다.  
따라서 프로그램이 예기치 않게 종료되는 것을 방지하기 위해 예외 처리가 필요합니다. 
``` python
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
            self.quiz_list = self.get_default_quizzes()
```

``` python
    try:
        game = QuizGame()
        game.run()
    except (EOFError, KeyboardInterrupt):
        print("\n프로그램을 저장 후 종료합니다")
        game.save_state()
```
- `JSONDecodeError` : JSON 평식이 손상된 경우
- `KeyError` : 필요한 데이터가 누락된 경우
- `EOFError` : 입력 스트림이 종료되었을 경우
- `KeyboardInterrupt` : 키보드 인터럽트가 발생한 경우  

위 4가지 상황에서 try/except를 사용하면 오류 발생 시 프로그램이 중단되지 않고, 대체 동작을 수행하도록 처리할 수 있습니다. 

---

## 커밋 규칙
- init : 프로젝트 초기화
- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : (코드의 수정 없이) 스타일만 변경

