import pythonbible as bible
import numpy as np
import random

BOOK_ABBREVIATIONS = {
    'GENESIS': bible.Book.GENESIS,
    'EXODUS': bible.Book.EXODUS,
    'LEVITICUS': bible.Book.LEVITICUS,
    'NUMBERS': bible.Book.NUMBERS,
    'DEUTERONOMY': bible.Book.DEUTERONOMY,
    'JOSHUA': bible.Book.JOSHUA,
    'JUDGES': bible.Book.JUDGES,
    'RUTH': bible.Book.RUTH,
    '1 SAMUEL': bible.Book.SAMUEL_1,
    '2 SAMUEL': bible.Book.SAMUEL_2,
    '1 KINGS ': bible.Book.KINGS_1,
    '2 KINGS ': bible.Book.KINGS_2,
    '1 CHRONICLES ': bible.Book.CHRONICLES_1,
    '2 CHRONICLES ': bible.Book.CHRONICLES_2,
    'EZRA': bible.Book.EZRA,
    'NEHEMIAH': bible.Book.NEHEMIAH,
    'ESTHER': bible.Book.ESTHER,
    'JOB': bible.Book.JOB,
    'PSALMS': bible.Book.PSALMS,
    'PROVERBS': bible.Book.PROVERBS,
    'ECCLESIASTES': bible.Book.ECCLESIASTES,
    'ISAIAH': bible.Book.ISAIAH,
    'JEREMIAH': bible.Book.JEREMIAH,
    'LAMENTATIONS': bible.Book.LAMENTATIONS,
    'EZEKIEL': bible.Book.EZEKIEL,
    'DANIEL': bible.Book.DANIEL,
    'HOSEA': bible.Book.HOSEA,
    'JOEL': bible.Book.JOEL,
    'AMOS': bible.Book.AMOS,
    'OBADIAH': bible.Book.OBADIAH,
    'JONAH': bible.Book.JONAH,
    'MICAH': bible.Book.MICAH,
    'NAHUM': bible.Book.NAHUM,
    'HABAKKUK': bible.Book.HABAKKUK,
    'ZEPHANIAH': bible.Book.ZEPHANIAH,
    'HAGGAI': bible.Book.HAGGAI,
    'ZECHARIAH': bible.Book.ZECHARIAH,
    'MALACHI': bible.Book.MALACHI,
    'MATTHEW': bible.Book.MATTHEW,
    'MARK': bible.Book.MARK,
    'LUKE': bible.Book.LUKE,
    'JOHN': bible.Book.JOHN,
    'ROMANS': bible.Book.ROMANS,
    '1 CORINTHIANS': bible.Book.CORINTHIANS_1,
    '2 CORINTHIANS': bible.Book.CORINTHIANS_2,
    'GALATIANS': bible.Book.GALATIANS,
    'EPHESIANS': bible.Book.EPHESIANS,
    'PHILIPPIANS': bible.Book.PHILIPPIANS,
    'COLOSSIANS': bible.Book.COLOSSIANS,
    '1 THESSALONIANS': bible.Book.THESSALONIANS_1,
    '2 THESSALONIANS': bible.Book.THESSALONIANS_2,
    '1 TIMOTHY': bible.Book.TIMOTHY_1,
    '2 TIMOTHY': bible.Book.TIMOTHY_2,
    'TITUS': bible.Book.TITUS,
    'PHILEMON': bible.Book.PHILEMON,
    'PHILEMON': bible.Book.PHILEMON,
    'HEBREWS': bible.Book.HEBREWS,
    'JAMES': bible.Book.JAMES,
    '1 PETER': bible.Book.PETER_1,
    '2 PETER': bible.Book.PETER_2,
    '1 JOHN': bible.Book.JOHN_1,
    '2 JOHN': bible.Book.JOHN_2,
    '3 JOHN': bible.Book.JOHN_3,
    'JUDE': bible.Book.JUDE,
    'REVELATION': bible.Book.REVELATION
}


def get_random_verse():
    # Select a random book number (1 to 66 for the books of the Bible)
    book_nbr = random.randint(1, 66)

    # Get the book corresponding to the book number
    book = bible.get_book_chapter_verse(int(f"{book_nbr:02}001001"))[0]

    # Get the number of chapters in the selected book
    total_chapters = bible.get_number_of_chapters(book)

    # Select a random chapter number
    chapter_nbr = random.randint(1, total_chapters)

    # Get the number of verses in the selected chapter
    total_verses = bible.get_number_of_verses(book, chapter_nbr)

    # Select a random verse number
    verse_nbr = random.randint(1, total_verses)

    # Get the verse ID for the random verse
    rand_verse_id = bible.get_verse_id(book, chapter_nbr, verse_nbr)
    return rand_verse_id


def get_book_from_abbrv(book_name: str):
    book_name = book_name.upper()
    if book_name in BOOK_ABBREVIATIONS:
        return BOOK_ABBREVIATIONS[book_name]
    raise ValueError(f"'{book_name}' is not a valid book name or abbreviation.")


def total_verses_in_bible():
    total_verses = 0
    for book in bible.Book:
        for chapter in range(1, bible.get_number_of_chapters(book) + 1):
            total_verses += bible.get_number_of_verses(book, chapter)
    return total_verses


def total_verses_in_book(book_name):
    try:
        total_verses = 0
        for chapter in range(1, bible.get_number_of_chapters(book_name) + 1):
            total_verses += bible.get_number_of_verses(book_name, chapter)
        return total_verses

    except bible.InvalidBookError:
        return f"{book_name} is not a valid book name."


def get_points(verses_away, max_dist):
    k = np.log(5000) / max_dist
    return np.ceil(5000 * np.exp((-k * verses_away)))


def find_dist_away(real_verse_id, guessed_verse_id):
    # Extract book, chapter, and verse for both the real and guessed verse
    real_book, real_chapter, real_verse = bible.get_book_chapter_verse(real_verse_id)
    guessed_book, guessed_chapter, guessed_verse = bible.get_book_chapter_verse(guessed_verse_id)

    # Initialize total distance
    total_verses_away = 0

    # Case 1: If both verses are in the same book
    if real_book == guessed_book:
        # Same chapter
        if real_chapter == guessed_chapter:
            total_verses_away = abs(real_verse - guessed_verse)
        else:
            # Different chapters, calculate across chapters in the same book
            if real_chapter > guessed_chapter:
                total_verses_away += bible.get_number_of_verses(guessed_book, guessed_chapter) - guessed_verse
                total_verses_away += sum(
                    bible.get_number_of_verses(guessed_book, ch) for ch in range(guessed_chapter + 1, real_chapter))
                total_verses_away += real_verse
            else:
                total_verses_away += bible.get_number_of_verses(real_book, real_chapter) - real_verse
                total_verses_away += sum(
                    bible.get_number_of_verses(real_book, ch) for ch in range(real_chapter + 1, guessed_chapter))
                total_verses_away += guessed_verse

    # Case 2: Verses are in different books
    else:
        # Ensure guessed_book is always the earlier one in order
        if real_book.value < guessed_book.value:
            real_book, guessed_book = guessed_book, real_book
            real_chapter, guessed_chapter = guessed_chapter, real_chapter
            real_verse, guessed_verse = guessed_verse, real_verse

        # Calculate verses from the guessed verse to the end of its book
        total_verses_away += bible.get_number_of_verses(guessed_book, guessed_chapter) - guessed_verse
        total_verses_away += sum(bible.get_number_of_verses(guessed_book, ch) for ch in
                                 range(guessed_chapter + 1, bible.get_number_of_chapters(guessed_book) + 1))

        # Calculate verses from the start of the real book to the real verse
        total_verses_away += real_verse
        total_verses_away += sum(bible.get_number_of_verses(real_book, ch) for ch in range(1, real_chapter))

        # Calculate all verses in between the books
        for book_value in range(guessed_book.value + 1, real_book.value):
            book = bible.Book(book_value)
            total_verses_away += sum(
                bible.get_number_of_verses(book, ch) for ch in range(1, bible.get_number_of_chapters(book) + 1))

    return total_verses_away

# for _ in range(1,10):
#     random_verse = get_random_verse()
#     guess_verse = get_random_verse()
#     version = bible.Version("KJV")
#     print(f'Real Verse ID: {random_verse}')
#     print(f'Guessed Verse ID: {guess_verse}')
#     print(f'Real Verse text: {bible.get_verse_text(random_verse, version=version)}')
#     print(f'Guessed Verse text: {bible.get_verse_text(guess_verse, version=version)}')
#     print(f'Real Verse address is {bible.get_book_chapter_verse(random_verse)}')
#     print(f'Guessed Verse address is {bible.get_book_chapter_verse(guess_verse)}')
#     distance = find_dist_away(random_verse, guess_verse)
#     print(f"Total verses away: {distance}")
#     print(f"Final score = {get_points(distance, total_verses_in_bible())}")
#     print("====="*10)

# real_verse_id = 40002017  # 2 Thessalonians 2:12
# guessed_verse_id = 40003016  # Matthew 3:16
# distance = find_dist_away(real_verse_id, guessed_verse_id)
#
# print(f"Total verses away: {distance}")
# print(f"Final score = {get_points(distance, total_verses_in_bible())}")
# print("====="*10)

book = get_book_from_abbrv('2 JOHN')
print(total_verses_in_book(book))