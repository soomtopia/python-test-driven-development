from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("./chromedriver")
        self.browser.implicitly_wait(3)

    def testDown(self):
        self.browser.quit()

    def check_for_row_int_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 사이트 접속
        self.browser.get('http://localhost:8000')
        # title 확인
        self.assertIn('To-Do', self.browser.title)
        # header 확인
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 작업추가
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        # 텍스트 입력
        inputbox.send_keys('공작깃털 사기')

        # 엔터키 입력 시 페이지가 갱신되고 작업목록에 입력한 데이터 추가
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_int_list_table("1: 공잣깃털 사기")
        self.check_for_row_int_list_table("2: 공잣깃털을 이용하여 그물 만들기")



if __name__ == '__main__':
    unittest.main(warnings='ignore')