from flask import jsonify


class AssessmentModel:
    def __init__(self,
                 average_sentence_length,
                 average_word_length,
                 flesch_reading_ease_scale,
                 common_words_percent,
                 text_repeatability_percent,
                 perfect_continuous_sentences_percent,
                 perfect_sentences_percent):
        self.average_sentence_length = round(average_sentence_length)
        self.average_word_length = round(average_word_length)

        self.flesch_reading_ease_scale = round(flesch_reading_ease_scale)
        self.common_words_percent = round(common_words_percent)
        self.text_repeatability_percent = round(text_repeatability_percent)

        self.perfect_continuous_sentences_percent = round(perfect_continuous_sentences_percent)
        self.perfect_sentences_percent = round(perfect_sentences_percent)
        self.perfect_continuous_sentences_rating = 100 - (perfect_continuous_sentences_percent * 5)
        self.perfect_sentences_rating = 100 - (perfect_sentences_percent * 3)

        result = (flesch_reading_ease_scale + common_words_percent + text_repeatability_percent +
                  (self.perfect_continuous_sentences_rating + self.perfect_sentences_rating) * 0.5) / 4

        # the total rating should be between 0 and 100
        self.total_rating = round(result) if 0 < result < 100 else 0 if result < 0 else 100

    def serialize(self):
        return {
            "totalRating": self.total_rating,
            "averageSentenceLength": self.average_sentence_length,
            "averageWordLength": self.average_word_length,
            "commonWordsPercent": self.common_words_percent,
            "fleschReadingEaseScale": self.flesch_reading_ease_scale,
            "textRepeatabilityPercent": self.text_repeatability_percent,
            "perfectContinuousSentencesPercent": self.perfect_continuous_sentences_percent,
            "perfectSentencesPercent": self.perfect_sentences_percent,
        }

    def to_json(self):
        return jsonify(self.serialize()).json
