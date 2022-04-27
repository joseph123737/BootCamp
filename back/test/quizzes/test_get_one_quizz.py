from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.quizzes import Quizzes, QuizzesRepository


def test_should_return_one_quizz():
    quizzes_repository = QuizzesRepository(temp_file())
    app = create_app(repositories={"quizzes": quizzes_repository})
    client = app.test_client()
    quizz = Quizzes(
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
    quizzes_repository.save_quizz(quizz)
    body = {"id_quizz": "01"}
    response = client.get("api/quizz/01", json=body)
    assert response.status_code == 200
    assert response.json == {
        "id_quizz": "01",
        "quizz_name": "patata",
        "quizzes": [
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
    }
