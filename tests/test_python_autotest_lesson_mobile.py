import allure
from python_autotest_lesson_mobile.components import search_in_wikipedia, verify_content_found


@allure.tag("Android")
@allure.label("owner", "JuliaMur")
@allure.story("Поиск в Википедии")
def test_search_in_wikipedia():

    search_in_wikipedia('Pytest')

    verify_content_found()


