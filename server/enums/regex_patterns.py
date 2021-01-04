class PerfectContinuousTensePatterns:
    # pattern to find all interrogative sentences of present/past/future perfect continuous tense
    all_interrogative_sentences_pattern = '(have|has|had)(.*?)been[\s]+[\w]+ing(.*?)\?'

    # pattern to find affirmative and negative sentences of present perfect continuous tense
    present_and_future_sentences_pattern = '[\w]+([\s]+have|[\W]ve|[\s]+has|[\W]s|[\s]+have[\s]+not|[\s]+haven[\W]t|[\W]ve[\s]+not|[\W]ven[\W]t|[\s]+has[\s]+not|[\s]+hasn[\W]t|[\W]s[\s]+not|[\W]sn[\W]t)[\s]+been[\s]+[\w]+ing.*(?<!\?)$'

    # pattern to find affirmative and negative sentences of past perfect continuous tense
    past_sentences_pattern = '[\w]+([\s]+had|[\s]+had[\s]+not|[\s]+hadn[\W]t)[\s]+been[\s]+[\w]+ing'