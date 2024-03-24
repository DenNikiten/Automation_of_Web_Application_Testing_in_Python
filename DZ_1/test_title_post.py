import pytest
from auth_file import title_for_posts_owner_not_me


def test_1(text_post, auth_by_address):
    assert text_post in title_for_posts_owner_not_me(auth_by_address)


if __name__ == '__main__':
    pytest.main(['-vv'])
