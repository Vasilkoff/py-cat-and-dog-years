import pytest

from app.main import get_human_age


class TestParseFirstYears:
    @pytest.mark.parametrize(
        "animal_years, result",
        [
            pytest.param(
                [14, 14],
                [0, 0],
                id="test_first_14_years_for_0_year"

            ),
            pytest.param(
                [15, 15],
                [1, 1],
                id="test_first_15_years_for_0_year"
            ),
            pytest.param(
                [24, 24],
                [2, 2],
                id="test_next_9_years_for_1_year"
            ),
            pytest.param(
                [28, 29],
                [3, 3],
                id="test_next_9_years_for_1_year"
            ),
            pytest.param(
                [100, 100],
                [21, 17],
                id="test_big_numbers_calculation"
            ),
        ]
    )
    def test_first_years(
            self,
            animal_years: list[int],
            result: list[int]) -> None:
        assert get_human_age(animal_years[0], animal_years[1]) == result
