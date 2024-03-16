def test_assert_always_true():
    x = 5
    y = 10
    # 错误地使用了逗号，形成了一个元组
    assert (x != y, "x and y should not be equal")
