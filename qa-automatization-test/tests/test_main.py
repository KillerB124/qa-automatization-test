import pytest
from src.main import get_max_height

@pytest.mark.parametrize(
    ("gender", "occupation", "expected"), 
    [
        ("Male", True, ('Galactus', '876 cm')),
        ("Male", False, ('Fin Fang Foom', '975 cm')),
        ("Female", True, ('Wolfsbane', '366 cm')),
        ("Female", False, ('Ardina', '193 cm')),
        ("-", True, ('Living Brain', '198 cm')),
        ("male", True, ('Galactus', '876 cm')),
        ("FEMALE", True, ('Wolfsbane', '366 cm')),
        ("Unknown", True, "Нет героя с заданными параметрами"),
        ("", True, "Нет героя с заданными параметрами"),
    ],
)
def test_get_max_height(gender, occupation, expected):
    result = get_max_height(gender, occupation)
    assert result == expected

@pytest.mark.parametrize("gender", [None, [], {}])
def test_gender(gender):
     with pytest.raises(TypeError):
        get_max_height(gender, True)

@pytest.mark.parametrize("occupation", [1, 0, "True", "False", "", None, [], {}])
def test_occupation(occupation):
     with pytest.raises(TypeError):
        get_max_height("Male", occupation)