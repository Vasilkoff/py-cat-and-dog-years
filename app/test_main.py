from app.main import get_human_age

def test_first_15_years_for_1_year():
    first = get_human_age(14, 14)
    second = get_human_age(15, 15)
    assert first == [0, 0] and second == [1, 1]

def test_next_9_years_for_1_year():
    first = get_human_age(23, 23)
    second = get_human_age(24, 24)
    assert first == [1, 1] and second == [2, 2]

def test_every_4_cat_years_for_1_year():
    cat = get_human_age(28, 1)

    assert cat[0] == 3

def test_every_5_dog_years_for_1_year():
    dog = get_human_age(0, 29)

    assert dog[1] == 3

def test_big_numbers_calculation():
    assert get_human_age(100, 100) == [21, 17]
# write your code here
