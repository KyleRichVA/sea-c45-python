import trigram


def test_read_lines():
    lines = trigram.readLines("sherlock_small.txt")
    assert(len(lines))


def test_get_words():
    lines = ["hey everyone\n", "these are words"]
    expected = ["hey", "everyone", "these", "are", "words"]
    words = trigram.getWords(lines)
    assert words == expected


def test_create_trigram():
    words = ['these', 'are', 'some', 'words']
    expected = {('these', 'are'): ['some'], ('are', 'some'): ['words']}
    tri = trigram.createTrigram(words)
    assert tri == expected
