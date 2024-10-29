import pythonbible as bible
import numpy as np
import random

BOOK_ABBREVIATIONS = {
    'gen': bible.Book.GENESIS,
    'exod': bible.Book.EXODUS, 'exo': bible.Book.EXODUS,
    'lev': bible.Book.LEVITICUS,
    'num': bible.Book.NUMBERS,
    'deut': bible.Book.DEUTERONOMY, 'deu': bible.Book.DEUTERONOMY,
    'josh': bible.Book.JOSHUA, 'jos': bible.Book.JOSHUA, 'jsh': bible.Book.JOSHUA,
    'judg': bible.Book.JUDGES, 'jdgs': bible.Book.JUDGES, 'jdg': bible.Book.JUDGES,
    'rut': bible.Book.RUTH, 'rth': bible.Book.RUTH,
    '1sam': bible.Book.SAMUEL_1, 'i samuel': bible.Book.SAMUEL_1, '1st samuel': bible.Book.SAMUEL_1,
    'first samuel': bible.Book.SAMUEL_1,
    '2sam': bible.Book.SAMUEL_2, 'ii samuel': bible.Book.SAMUEL_2, '2nd samuel': bible.Book.SAMUEL_2,
    'second samuel': bible.Book.SAMUEL_2,
    '1kgs': bible.Book.KINGS_1, '1kin': bible.Book.KINGS_1, '1ki': bible.Book.KINGS_1,
    '2kgs': bible.Book.KINGS_2, '2kin': bible.Book.KINGS_2, '2ki': bible.Book.KINGS_2,
    '1chron': bible.Book.CHRONICLES_1, 'i chronicles': bible.Book.CHRONICLES_1,
    '1st chronicles': bible.Book.CHRONICLES_1, 'first chronicles': bible.Book.CHRONICLES_1,
    '2chron': bible.Book.CHRONICLES_2, 'ii chronicles': bible.Book.CHRONICLES_2,
    '2nd chronicles': bible.Book.CHRONICLES_2, 'second chronicles': bible.Book.CHRONICLES_2,
    'ezr': bible.Book.EZRA,
    'neh': bible.Book.NEHEMIAH,
    'esth': bible.Book.ESTHER, 'est': bible.Book.ESTHER,
    'job': bible.Book.JOB,
    'ps': bible.Book.PSALMS, 'psalm': bible.Book.PSALMS, 'pslm': bible.Book.PSALMS, 'psa': bible.Book.PSALMS,
    'psm': bible.Book.PSALMS, 'pss': bible.Book.PSALMS,
    'prov': bible.Book.PROVERBS, 'pro': bible.Book.PROVERBS, 'prv': bible.Book.PROVERBS,
    'eccle': bible.Book.ECCLESIASTES, 'eccl': bible.Book.ECCLESIASTES, 'ecc': bible.Book.ECCLESIASTES,
    'ec': bible.Book.ECCLESIASTES, 'qoh': bible.Book.ECCLESIASTES,
    'isa': bible.Book.ISAIAH,
    'jer': bible.Book.JEREMIAH,
    'lam': bible.Book.LAMENTATIONS,
    'ezek': bible.Book.EZEKIEL, 'eze': bible.Book.EZEKIEL, 'ezk': bible.Book.EZEKIEL,
    'dan': bible.Book.DANIEL,
    'hos': bible.Book.HOSEA,
    'joe': bible.Book.JOEL,
    'amo': bible.Book.AMOS,
    'obad': bible.Book.OBADIAH, 'oba': bible.Book.OBADIAH,
    'jon': bible.Book.JONAH, 'jnh': bible.Book.JONAH,
    'mic': bible.Book.MICAH,
    'nah': bible.Book.NAHUM,
    'hab': bible.Book.HABAKKUK,
    'zeph': bible.Book.ZEPHANIAH, 'zep': bible.Book.ZEPHANIAH,
    'hag': bible.Book.HAGGAI,
    'zech': bible.Book.ZECHARIAH, 'zec': bible.Book.ZECHARIAH,
    'mal': bible.Book.MALACHI,
    'matt': bible.Book.MATTHEW, 'mat': bible.Book.MATTHEW,
    'mar': bible.Book.MARK, 'mrk': bible.Book.MARK,
    'luk': bible.Book.LUKE,
    'joh': bible.Book.JOHN, 'jhn': bible.Book.JOHN, 'jo': bible.Book.JOHN, 'jn': bible.Book.JOHN,
    'rom': bible.Book.ROMANS,
    '1cor': bible.Book.CORINTHIANS_1, 'i corinthians': bible.Book.CORINTHIANS_1,
    '1st corinthians': bible.Book.CORINTHIANS_1, 'first corinthians': bible.Book.CORINTHIANS_1,
    '2cor': bible.Book.CORINTHIANS_2, 'ii corinthians': bible.Book.CORINTHIANS_2,
    '2nd corinthians': bible.Book.CORINTHIANS_2, 'second corinthians': bible.Book.CORINTHIANS_2,
    'gal': bible.Book.GALATIANS,
    'ephes': bible.Book.EPHESIANS, 'eph': bible.Book.EPHESIANS,
    'phil': bible.Book.PHILIPPIANS, 'php': bible.Book.PHILIPPIANS,
    'col': bible.Book.COLOSSIANS,
    '1thess': bible.Book.THESSALONIANS_1, '1 thes': bible.Book.THESSALONIANS_1, '1 ths': bible.Book.THESSALONIANS_1,
    '2thess': bible.Book.THESSALONIANS_2, '2 thes': bible.Book.THESSALONIANS_2, '2 ths': bible.Book.THESSALONIANS_2,
    '1tim': bible.Book.TIMOTHY_1, 'i timothy': bible.Book.TIMOTHY_1, '1st timothy': bible.Book.TIMOTHY_1,
    '2tim': bible.Book.TIMOTHY_2, 'ii timothy': bible.Book.TIMOTHY_2, '2nd timothy': bible.Book.TIMOTHY_2,
    'tit': bible.Book.TITUS,
    'philem': bible.Book.PHILEMON, 'phile': bible.Book.PHILEMON, 'phlm': bible.Book.PHILEMON,
    'phi': bible.Book.PHILEMON, 'phm': bible.Book.PHILEMON,
    'heb': bible.Book.HEBREWS,
    'jas': bible.Book.JAMES,
    '1pet': bible.Book.PETER_1, 'i peter': bible.Book.PETER_1, '1st peter': bible.Book.PETER_1,
    '2pet': bible.Book.PETER_2, 'ii peter': bible.Book.PETER_2, '2nd peter': bible.Book.PETER_2,
    '1john': bible.Book.JOHN_1, '1jhn': bible.Book.JOHN_1, '1jo': bible.Book.JOHN_1, '1jn': bible.Book.JOHN_1,
    '2john': bible.Book.JOHN_2, '2jhn': bible.Book.JOHN_2, '2jo': bible.Book.JOHN_2, '2jn': bible.Book.JOHN_2,
    '3john': bible.Book.JOHN_3, '3jhn': bible.Book.JOHN_3, '3jo': bible.Book.JOHN_3, '3jn': bible.Book.JOHN_3,
    'jud': bible.Book.JUDE,
    'rev': bible.Book.REVELATION
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
    book_name = book_name.lower()
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