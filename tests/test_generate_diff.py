from pathlib import Path

from gendiff.engine import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff():
    file1 = get_test_data_path("file1.json")
    file2 = get_test_data_path("file2.json")
    actual = generate_diff(file1, file2)
    expected = read_file("generate_diff_result.txt")
    assert actual == expected