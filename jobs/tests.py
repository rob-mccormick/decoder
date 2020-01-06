from django.test import TestCase

from .funky import text_to_list, number_of_words


class TextToListTests(TestCase):

    def test_all_punctuation_effectively_removed(self):
        """
        returns False for punctuation not removed from text
        """
        text1 = 'THe, quick; (br-own): fox! "jumped" <> - -- [over] the\ /lazy dog.'
        text2 = "He shouted, 'Hello!'"
        textlist = text_to_list(text1) + text_to_list(text2)
        for char in '-.,\;":_*!\n' or "'[]()/":
            if char in textlist:
                return False



#
#
#
# class QuestionModelTests(TestCase):
#
#     def test_was_published_recently_with_future_question(self):
#         """
#         was_published_recently() returns False for questions whose pub_date
#         is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)
