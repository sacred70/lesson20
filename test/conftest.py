import pytest
from setup_db import db
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO
from dao.model.genre import Genre
from dao.genre import GenreDAO


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


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name="Genre 1")
    genre_2 = Genre(id=2, name="Genre 2")
    genre_3 = Genre(id=3, name="Genre 3")

    genres = {1: genre_1, 2: genre_2, 3: genre_3}

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao

