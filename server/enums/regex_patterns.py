from enums.common_enums import irregular_verbs_3_forms


class PerfectContinuousTensePatterns:
    # pattern to find all interrogative sentences of the present, past and future perfect continuous tenses
    all_interrogative_sentences_pattern = '(have|has|had)(.*?)been[\s]+[\w]+ing(.*?)\?'
    # pattern to find affirmative and negative sentences of the present, past and future perfect continuous tenses
    all_affirmative_and_negative_sentences_pattern = '[\w]+([\s]+had|[\s]+had[\s]+not|[\s]+hadn[\W]t|[\s]+have|[\W]ve|[\s]+has|[\W]s|[\s]+have[\s]+not|[\s]+haven[\W]t|[\W]ve[\s]+not|[\W]ven[\W]t|[\s]+has[\s]+not|[\s]+hasn[\W]t|[\W]s[\s]+not|[\W]sn[\W]t)[\s]+been[\s]+[\w]+ing.*(?<!\?)$'


class PerfectTensePatterns:
    # pattern to find all interrogative sentences of the present, past and future perfect tenses
    all_interrogative_sentences_pattern = f'[\w]*[\s]*[\w]*[\s]*([\s]+have|[\s]+has|[\s]+had|[\s]+have[\s]+not|[\s]+has[\s]+not|[\s]+had[\s]+not|[\s]+haven[\W]t|[\s]+hasn[\W]+t|[\s]+hadn[\W]+t)[\s]*[\w]*[\s]*([\w]+ed|{irregular_verbs_3_forms})(.*?)\?'
    # pattern to find all affirmative and negative sentences of the present, past and future perfect tenses
    all_affirmative_and_negative_sentences_pattern = f'[\w]+([\s]+have|[\s]+has|[\s]+had|[\s]+have[\s]+not|[\s]+has[\s]+not|[\s]+had[\s]+not|[\s]+haven[\W]t|[\s]+hasn[\W]+t|[\s]+hadn[\W]+t)[\s]+([\w]+ed|{irregular_verbs_3_forms}).*(?<!\?)$'
