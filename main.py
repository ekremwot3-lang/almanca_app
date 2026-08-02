import json
import os
import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder

MOOD_LABELS = {
    'indikatif': 'İndikatif',
    'konjunktiv_I': 'Konjunktiv I',
    'konjunktiv_II': 'Konjunktiv II',
}

TENSE_LABELS = {
    'simdiki_zaman': 'Präsens (Şimdiki Zaman)',
    'praeteritum': 'Präteritum (Geçmiş Zaman)',
    'perfekt': 'Perfekt',
    'plusquamperfekt': 'Plusquamperfekt',
    'gelecek_I': 'Futur I (Gelecek Zaman)',
    'gelecek_II': 'Futur II',
}

PRONOUN_LABELS = {
    'ich': 'ich',
    'du': 'du',
    'er_sie_es': 'er / sie / es',
    'wir': 'wir',
    'ihr': 'ihr',
    'sie_Sie': 'sie / Sie',
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'fiiller_duzeltilmis.json')
KV_PATH = os.path.join(BASE_DIR, 'quiz.kv')


def load_verbs():
    with open(DATA_PATH, encoding='utf-8') as f:
        return json.load(f)


class QuizRoot(BoxLayout):
    verb_text = StringProperty('')
    mood_tense_text = StringProperty('')
    pronoun_text = StringProperty('')
    feedback_text = StringProperty('')
    feedback_color = ListProperty([0.2, 0.2, 0.2, 1])
    score_text = StringProperty('Doğru: 0   Yanlış: 0')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.verbs = load_verbs()
        self.verb_keys = list(self.verbs.keys())
        self.correct_count = 0
        self.wrong_count = 0
        self.current = None
        self.next_question()

    def pick_question(self):
        for _ in range(50):
            verb_key = random.choice(self.verb_keys)
            entry = self.verbs[verb_key]
            cekimler = entry.get('cekimler', {})
            moods = [m for m in cekimler if cekimler[m]]
            if not moods:
                continue
            mood = random.choice(moods)
            tenses = [t for t in cekimler[mood] if cekimler[mood][t]]
            if not tenses:
                continue
            tense = random.choice(tenses)
            pronouns = list(cekimler[mood][tense].keys())
            if not pronouns:
                continue
            pronoun = random.choice(pronouns)
            answer = cekimler[mood][tense][pronoun]
            if not answer:
                continue
            return {
                'verb': verb_key,
                'anlam': entry.get('anlam', ''),
                'mood': mood,
                'tense': tense,
                'pronoun': pronoun,
                'answer': answer,
            }
        return None

    def next_question(self):
        q = self.pick_question()
        if not q:
            self.feedback_text = 'Soru üretilemedi, tekrar deneyin.'
            return
        self.current = q
        self.verb_text = '{}  ({})'.format(q['verb'], q['anlam'])
        self.mood_tense_text = '{} \u2013 {}'.format(
            MOOD_LABELS.get(q['mood'], q['mood']),
            TENSE_LABELS.get(q['tense'], q['tense']),
        )
        self.pronoun_text = PRONOUN_LABELS.get(q['pronoun'], q['pronoun'])
        self.feedback_text = ''
        self.feedback_color = [0.2, 0.2, 0.2, 1]
        if 'answer_input' in self.ids:
            self.ids.answer_input.text = ''
            self.ids.answer_input.focus = True

    @staticmethod
    def _norm(s):
        return ' '.join(s.strip().lower().split())

    def check_answer(self):
        if not self.current:
            return
        user = self.ids.answer_input.text if 'answer_input' in self.ids else ''
        correct = self.current['answer']
        if self._norm(user) == self._norm(correct):
            self.correct_count += 1
            self.feedback_text = 'Doğru! \u2713'
            self.feedback_color = [0.05, 0.5, 0.05, 1]
        else:
            self.wrong_count += 1
            self.feedback_text = 'Yanlış. Doğru cevap: {}'.format(correct)
            self.feedback_color = [0.6, 0.05, 0.05, 1]
        self.score_text = 'Doğru: {}   Yanlış: {}'.format(self.correct_count, self.wrong_count)

    def show_hint(self):
        if not self.current:
            return
        self.feedback_text = 'İpucu \u2192 doğru cevap: {}'.format(self.current['answer'])
        self.feedback_color = [0.1, 0.1, 0.5, 1]


class AlmancaCekimApp(App):
    def build(self):
        Builder.load_file(KV_PATH)
        return QuizRoot()


if __name__ == '__main__':
    AlmancaCekimApp().run()
