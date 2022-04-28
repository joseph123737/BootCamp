import sys

sys.path.insert(0, "")
from src.domain.login_users import Users, UsersRepository

from src.domain.quizzes import Quizzes, QuizzesRepository


def main():

    database_path = "data/database.db"

    users_repository = UsersRepository(database_path)

    users_repository.save(Users("01", "mata_bebes", "Valentina"))

    quizzes_repository = QuizzesRepository(database_path)

    quizzes_repository.save_quizz(
        Quizzes(
            id_quizz="01",
            quizz_name="patata",
            quizzes=[
                {
                    "id": 1,
                    "question_quizz": "que hace la siguiente list comprehension :  [( i) for i in range (5) ]",
                    "answer_01": {
                        "title": "hace un for del 1 al 5",
                        "is_correct": True,
                        "id_button": "1",
                    },
                    "answer_02": {
                        "title": "la verdad que no se",
                        "is_correct": False,
                        "id_button": "2",
                    },
                    "answer_03": {
                        "title": "print los nombre de una lista",
                        "is_correct": False,
                        "id_button": "3",
                    },
                    "answer_04": {
                        "title": "splitea una string",
                        "is_correct": False,
                        "id_button": "4",
                    },
                }
            ],
        )
    )


if __name__ == "__main__":
    main()
