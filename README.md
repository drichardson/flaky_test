# Flaky tests runners in python

[Google Testing Blog](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html)
discusses their approach to flaky tests. One aspect was running flakies and
only considering them failed if they fail 3 times in a row. This repo
implements that in Python with pytest.

