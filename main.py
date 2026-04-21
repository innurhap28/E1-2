from quiz_game import QuizGame

if __name__ == "__main__":
    try:
        game = QuizGame()
        game.run()
    except (EOFError, KeyboardInterrupt):
        print("\n프로그램을 저장 후 종료합니다")
        game.save_state()