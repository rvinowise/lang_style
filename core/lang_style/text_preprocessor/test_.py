import pytest

from . import text_preprocessor



@pytest.mark.parametrize("given_text, out_text", [
    ('My text   with        spaces		tabs 	 ',
     'My text with spaces tabs'),
    ('   ! @ # $%^&*()_+  ',
     '! @ # $%^&*()_+')
])
def test_text_is_cleaned_from_spaces(given_text, out_text):
    assert text_preprocessor.process(given_text) == out_text