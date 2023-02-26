import pytest
from setup_db import db
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name="Director 1")
    director_2 = Director(id=2, name="Director 2")
    director_3 = Director(id=3, name="Director 3")

    directors = {1: director_1, 2: director_2, 3: director_3}

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao
