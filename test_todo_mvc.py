import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

EXECUTE_SLEEP_UNTIL_SUCCEED = 1
SLEEP_IN_END_OF_TEST = 5


def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://todomvc.com/examples/angularjs/#/")
    driver.maximize_window()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    return driver


def test_add_task(task_to_add):
    driver = init_driver()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    element = driver.find_element_by_xpath('/html/body/ng-view/section/header/form/input')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    element.send_keys('Clean my house\n')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    all_tasks = driver.find_element_by_xpath("/html/body/ng-view/section/section/ul").text
    print('add_test failed') if 'Clean my house' not in all_tasks else print('add_test passed')
    time.sleep(SLEEP_IN_END_OF_TEST)


def test_edit_task(activater):
    driver = init_driver()
    actions = ActionChains(driver)

    element = driver.find_element_by_xpath('/html/body/ng-view/section/header/form/input')
    element.send_keys('Wake up\n')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    element2 = driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label')
    actions.double_click(element2).perform()
    task_to_edit = driver.find_element_by_css_selector('input[todo-focus="todo == editedTodo"]')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    task_to_edit.send_keys(Keys.CONTROL, "a")
    task_to_edit.send_keys('Go to sleep\n')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    print("edit_test passed ")
    time.sleep(SLEEP_IN_END_OF_TEST)


def test_delete_task(activater):
    driver = add_task_to_manage()
    actions = ActionChains(driver)
    element2 = driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    actions.double_click(element2).perform()
    task_to_edit = driver.find_element_by_css_selector('input[todo-focus="todo == editedTodo"]')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    task_to_edit.send_keys(Keys.CONTROL, "a")
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    task_to_edit.send_keys(Keys.BACKSPACE + '\n')
    time.sleep(SLEEP_IN_END_OF_TEST)


def test_mark_task_as_completed(activater):
    driver = add_task_to_manage()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/input').click()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[3]/a').click()
    to_check = driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label')
    if 'Wake up' != to_check.text:
        print('ERROR')
    print('mark_task_as_completed test passed')
    time.sleep(SLEEP_IN_END_OF_TEST)
    return driver


def test_mark_task_as_active(activater):
    driver = test_mark_task_as_completed(activater)
    driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/input').click()

    driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[2]/a').click()
    to_check = driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label').text
    if 'Wake up' != to_check:
        print('ERROR')
        return
    print('test mark_task_as_active passed')
    time.sleep(SLEEP_IN_END_OF_TEST)


def test_clear_completed(activaterv):
    driver = add_task_to_manage()
    element = driver.find_element_by_xpath('/html/body/ng-view/section/header/form/input')
    element.send_keys('Clean the house\n')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li[2]/div/input').click()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/footer/button').click()
    time.sleep(SLEEP_IN_END_OF_TEST)


def test_different_views_features(activate):
    driver = add_task_to_manage()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    element = driver.find_element_by_xpath('/html/body/ng-view/section/header/form/input')
    element.send_keys('Clean the house\n')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li[2]/div/input').click()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[1]/a').click()
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[2]/a')
    driver.implicitly_wait(EXECUTE_SLEEP_UNTIL_SUCCEED)
    driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[3]/a')
    time.sleep(SLEEP_IN_END_OF_TEST)


def add_task_to_manage():
    driver = init_driver()
    element = driver.find_element_by_xpath('/html/body/ng-view/section/header/form/input')
    element.send_keys('Wake up\n')
    time.sleep(SLEEP_IN_END_OF_TEST)
    return driver


def main():
    args = sys.argv[1:]
    print(args)
    tasks = {
        '1': 'clean my house',
        '2': 'wake up',
        '3': 'go to sleep',
        '4': 'wake up',
        '5': 'clean the house',
        '6': 'wake up',
        '7': 'activate'
    }

    test_dic = {
        '1': test_add_task,
        '2': test_edit_task,
        '3': test_delete_task,
        '4': test_mark_task_as_completed,
        '5': test_mark_task_as_active,
        '6': test_clear_completed,
        '7': test_different_views_features
    }
    for test_num in args:
        print(test_num)
        print(*tasks[test_num])
        test_dic[test_num](*(tasks[test_num])[0])


if __name__ == "__main__":
    main()
