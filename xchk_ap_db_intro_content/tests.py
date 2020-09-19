import unittest
from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock
from xchk_core.templatetags.xchk_instructions import node_instructions_2_ul
from xchk_core.strats import StratInstructions, AT_LEAST_ONE_TEXT, ALL_OF_TEXT
from xchk_ap_db_intro_content.strats import xchk_ap_db_intro_content_create_statement_regex_check, simpele_tekst_regex_compiled

class RegexesTest(TestCase):

    def test_expected_create_statement(self):
        expected = 'CREATE TABLE Boeken(Titel VARCHAR(50), JaarUitgave INT);'
        self.assertTrue(xchk_ap_db_intro_content_create_statement_regex_check.pattern.fullmatch(expected))

    def test_expected_simple_text(self):
        expected = '''
        VARCHAR(200)
        CHAR(7)'''
        self.assertTrue(simpele_tekst_regex_compiled.fullmatch(expected))

if __name__ == '__main__':
    unittest.main()
