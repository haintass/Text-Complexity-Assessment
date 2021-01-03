import re
from enums.most_common_words import most_common_words


def calculate_text_complexity(text):
    text_without_non_alphabet_chars = _remove_non_alphabet_chars(text)
    sentences = _get_sentences(text)
    total_word_count = _count_all_words(sentences)

    average_sentence_length, average_word_length = _calc_average_length_of_words_and_sentences(
        text_without_non_alphabet_chars, sentences, total_word_count
    )

    flesch_reading_ease_scale = _get_flesch_reading_ease_scale(average_sentence_length, average_word_length)
    common_words_rate = _calc_rate_of_common_words_in_sentences(text_without_non_alphabet_chars, total_word_count)
    text_uniqueness_rating = _get_text_uniqueness_rating(sentences)

    result = (flesch_reading_ease_scale + common_words_rate + text_uniqueness_rating) / 3

    return round(result) if result <= 100 else 100


def _get_flesch_reading_ease_scale(average_sentence_length, average_word_length):
    sentence_length_scale = 112 + (50 if average_sentence_length < 6 else -30) - average_sentence_length
    word_length_scale = 100 - average_word_length

    return (sentence_length_scale + word_length_scale) / 2


def _get_text_uniqueness_rating(sentences):
    frequency_of_repeated_sentences = _calc_frequency_of_repeated_sentences(sentences)

    return frequency_of_repeated_sentences + 90


def _calc_frequency_of_repeated_sentences(sentences):
    number_of_unique_sentences = len(set(sentences))

    return 100 - (number_of_unique_sentences / len(sentences) * 100)


def _calc_rate_of_common_words_in_sentences(text, total_word_count):
    common_word_count = 0
    all_text_words = re.split(' ', text)
    for word in all_text_words:
        if word.lower() in (w.lower() for w in most_common_words):
            common_word_count += 1

    return common_word_count / total_word_count * 100


def _calc_average_length_of_words_and_sentences(text_without_non_alphabet_chars, sentences, total_word_count):
    average_sentence_length = _calc_average_sentence_length(total_word_count, len(sentences))
    average_word_length = _calc_average_word_length(total_word_count, text_without_non_alphabet_chars)

    return average_sentence_length, average_word_length


def _get_sentences(text):
    # delete extra whitespaces
    text = re.sub(' +', ' ', text).strip()

    # split text into sentences
    sentences = re.split('\n|\\.|\\.|\\!|\\?|\\;', text)

    # delete empty sentences
    sentences = [s for s in sentences if len(s) > 0 and not s.isspace()]

    return sentences


def _count_all_words(sentences: list):
    return sum(len(x.split()) for x in sentences)


def _calc_average_sentence_length(total_word_count: int, sentences_count: int):
    return total_word_count / sentences_count


def _calc_average_word_length(total_word_count: int, text_without_non_alphabet_chars: str):
    words = re.split(' ', text_without_non_alphabet_chars)
    return sum(len(w) for w in words) / total_word_count


def _remove_non_alphabet_chars(text):
    return re.sub('[^0-9a-zA-Z]+', ' ', text)
