# Week 1.7, Session 1: Task 1

Equivalent classes for `comfort_level()`

| Comfort level | Values |
| --- | --- |
| COLD | 15.0 |
| HOT  | 26.0 |
| OK   | 20.0 |

~~~
def test_cold():
    assert comfort_level(15) == "COLD"
    assert comfort_level(0) == "COLD"
def test_hot():
    assert comfort_level(26) == "HOT"
    assert comfort_level(30) == "HOT"
~~~