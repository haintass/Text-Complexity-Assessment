import math
import re
from enums.most_common_words import most_common_words
from enums.regex_patterns import PerfectContinuousTensePatterns


def calculate_text_complexity(text):
    text_without_non_alphabet_chars = _remove_non_alphabet_chars(text)
    sentences = _get_sentences(text)
    sentences_count = len(sentences)
    total_word_count = _count_all_words(sentences)

    average_sentence_length, average_word_length = _calc_average_length_of_words_and_sentences(
        text_without_non_alphabet_chars, sentences_count, total_word_count
    )

    flesch_reading_ease_scale = _get_flesch_reading_ease_scale(average_sentence_length, average_word_length, sentences_count)
    common_words_rate = _calc_rate_of_common_words_in_sentences(text_without_non_alphabet_chars, total_word_count)
    text_uniqueness_rating = _get_text_uniqueness_rating(sentences, sentences_count)

    perfect_continuous_sentences_rating = _calc_occurrence_of_perfect_continuous_sentences(text, sentences_count)

    result = (flesch_reading_ease_scale + common_words_rate + text_uniqueness_rating + perfect_continuous_sentences_rating) / 4

    return round(result) if result <= 100 else 100


def _calc_occurrence_of_perfect_continuous_sentences(text, sentences_count):
    # the number of all interrogative sentences of present / past / future perfect continuous tense
    all_interrogative_sentences = re.findall(PerfectContinuousTensePatterns.all_interrogative_sentences_pattern, text, flags=re.I | re.M)
    # the number of all affirmative and negative sentences of present perfect continuous tense
    present_sentences = re.findall(PerfectContinuousTensePatterns.present_and_future_sentences_pattern, text, flags=re.I | re.M)
    # the number of all affirmative and negative sentences of past perfect continuous tense
    past_sentences = re.findall(PerfectContinuousTensePatterns.past_sentences_pattern, text, flags=re.I | re.M)

    perfect_continuous_sentences_count = len(all_interrogative_sentences) + len(present_sentences) + len(past_sentences)
    perfect_continuous_sentences_percent = perfect_continuous_sentences_count / sentences_count * 100

    return 100 - (perfect_continuous_sentences_percent * 5)


def _get_flesch_reading_ease_scale(average_sentence_length, average_word_length, sentences_count):
    sentence_length_scale = 112 + (50 - average_sentence_length) - (average_sentence_length * 5)
    word_length_scale = 100 - (average_word_length * 3)

    return (sentence_length_scale + word_length_scale - (math.log2(sentences_count) * 10)) / 3


def _get_text_uniqueness_rating(sentences, sentences_count):
    frequency_of_repeated_sentences = _calc_frequency_of_repeated_sentences(sentences, sentences_count)

    return frequency_of_repeated_sentences + 50


def _calc_frequency_of_repeated_sentences(sentences, sentences_count):
    number_of_unique_sentences = len(set(sentences))

    return 100 - (number_of_unique_sentences / sentences_count * 100)


def _calc_rate_of_common_words_in_sentences(text, total_word_count):
    common_word_count = 0
    all_text_words = re.split(' ', text)
    for word in all_text_words:
        if word.lower() in (w.lower() for w in most_common_words):
            common_word_count += 1

    return common_word_count / total_word_count * 100


def _calc_average_length_of_words_and_sentences(text_without_non_alphabet_chars, sentences_count, total_word_count):
    average_sentence_length = _calc_average_sentence_length(total_word_count, sentences_count)
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
