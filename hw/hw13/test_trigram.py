import trigram


def test_read_lines():
    lines = trigram.readLines("sherlock_small.txt")
    assert(len(lines))
