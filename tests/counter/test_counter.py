from src.pre_built.counter import count_ocurrences


def test_counter():
    file_path = "data/jobs.csv"
    word_py = "Python"
    word_js = "JavaScript"
    result_py = count_ocurrences(file_path, word_py)
    result_js = count_ocurrences(file_path, word_js)
    assert result_py == 47
    assert result_js == 44
