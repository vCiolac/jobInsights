from src.pre_built.counter import count_ocurrences


def test_counter():
    file_path = "data/jobs.csv"
    word_py = "Python"
    word_py_upper = "PYTHON"
    word_js = "JavaScript"
    word_js_upper = "JAVASCRIPT"
    result_py = count_ocurrences(file_path, word_py)
    result_js = count_ocurrences(file_path, word_js)
    result_py_upper = count_ocurrences(file_path, word_py_upper)
    result_js_upper = count_ocurrences(file_path, word_js_upper)
    assert result_py == 1639
    assert result_js == 122
    assert result_py_upper == 1639
    assert result_js_upper == 122
