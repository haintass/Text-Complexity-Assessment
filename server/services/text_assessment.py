import math
import re
from enums.common_enums import most_common_words
from enums.regex_patterns import PerfectContinuousTensePatterns, PerfectTensePatterns
from data.assessment_model import AssessmentModel


def calculate_text_complexity(text):
    text_without_non_alphabet_chars = _remove_non_alphabet_chars(text)
    sentences = _split_text_into_sentences(text)
    sentences_count = len(sentences)
    total_word_count = _count_all_words(sentences)

    average_sentence_length = _calc_average_sentence_length(total_word_count, sentences_count)
    average_word_length = _calc_average_word_length(total_word_count, text_without_non_alphabet_chars)

    flesch_reading_ease_scale = _get_flesch_reading_ease_scale(average_sentence_length, average_word_length)

    common_words_percent = _get_occurrence_of_common_words_percent(text_without_non_alphabet_chars, total_word_count)
    text_repeatability_percent = _get_text_repeatability_percent(sentences, sentences_count)

    perfect_continuous_sentences_percent = _calc_perfect_continuous_sentences_percent(text, sentences_count)
    perfect_sentences_percent = _calc_perfect_sentences_percent(text, sentences_count)

    assessment_model = AssessmentModel(average_sentence_length, average_word_length, flesch_reading_ease_scale,
                                       common_words_percent, text_repeatability_percent,
                                       perfect_continuous_sentences_percent, perfect_sentences_percent)

    return assessment_model


def _calc_perfect_continuous_sentences_percent(text, sentences_count):
    # all interrogative sentences of the present, past and future perfect continuous tenses
    all_interrogative_sentences = re.findall(
        pattern=PerfectContinuousTensePatterns.all_interrogative_sentences_pattern,
        string=text,
        flags=re.I | re.M)

    # all affirmative and negative sentences of present perfect continuous tense
    all_affirmative_and_negative_sentences = re.findall(
        pattern=PerfectContinuousTensePatterns.all_affirmative_and_negative_sentences_pattern,
        string=text,
        flags=re.I | re.M
    )

    perfect_continuous_sentences_count = len(all_interrogative_sentences) + len(all_affirmative_and_negative_sentences)
    perfect_continuous_sentences_percent = perfect_continuous_sentences_count / sentences_count * 100

    return perfect_continuous_sentences_percent


def _calc_perfect_sentences_percent(text, sentences_count):
    # all interrogative sentences of the present, past and future perfect tenses
    all_interrogative_sentences = re.findall(
        pattern=PerfectTensePatterns.all_interrogative_sentences_pattern,
        string=text,
        flags=re.I | re.M
    )

    # all affirmative and negative sentences of present perfect tense
    all_affirmative_and_negative_sentences = re.findall(
        pattern=PerfectTensePatterns.all_affirmative_and_negative_sentences_pattern,
        string=text,
        flags=re.I | re.M
    )

    perfect_sentences_count = len(all_interrogative_sentences) + len(all_affirmative_and_negative_sentences)
    perfect_sentences_percent = perfect_sentences_count / sentences_count * 100

    return perfect_sentences_percent


def _get_flesch_reading_ease_scale(average_sentence_length, average_word_length):
    """
    calculates the Flesch reading ease scale to indicate how difficult a text in English is to understand
    :param average_sentence_length:
    :param average_word_length:
    :return: a number indicating the difficulty of reading English text.
     The larger the number, the easier it is to read the text.
    """
    sentence_length_scale = 120 - (math.log(math.pow(average_sentence_length, 5)) * 7)
    word_length_scale = 105 - math.pow(average_word_length, 2)

    return (
                   sentence_length_scale + word_length_scale -
                   (
                       (0 if average_word_length < 7 else math.log2(average_word_length) * 10) +
                       (0 if average_sentence_length < 15 else math.log2(average_sentence_length) * 8)
                   )
           ) / math.log2(average_word_length)


def _get_text_repeatability_percent(sentences, sentences_count):
    # calculates the percentage of duplicate sentences
    number_of_unique_sentences = len(set(sentences))
    return 100 - (number_of_unique_sentences / sentences_count * 100)


def _get_occurrence_of_common_words_percent(text, total_word_count):
    """
    calculates the percentage of the most common English words in the text
    :param text:
    :param total_word_count:
    :return: a number between 0 and 100
    """
    common_word_count = 0
    all_text_words = re.split(' ', text)
    for word in all_text_words:
        if word.lower() in (w.lower() for w in most_common_words):
            common_word_count += 1

    return common_word_count / total_word_count * 100


def _split_text_into_sentences(text):
    # delete extra whitespaces
    text = re.sub(' +', ' ', text).strip()

    # split text into sentences
    sentences = re.split('\n|\\.|\\!|\\?|\\;', text)

    # remove empty sentences and sentences containing only numbers
    sentences = [s for s in sentences if len(s) > 0 and not s.isspace() and not re.match('^[\d.]+$', s)]

    return sentences


def _count_all_words(sentences: list):
    return sum(len(x.split()) for x in sentences)


def _calc_average_sentence_length(total_word_count: int, sentences_count: int):
    return total_word_count / sentences_count


def _calc_average_word_length(total_word_count: int, text_without_non_alphabet_chars: str):
    words = re.split(' ', text_without_non_alphabet_chars)
    return sum(len(w) for w in words) / total_word_count


def _remove_non_alphabet_chars(text):
    # replaces all non-numeric and non-alphabetic characters with spaces
    return re.sub('[^0-9a-zA-Z]+', ' ', text)
