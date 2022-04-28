from app.application import Application
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    #context.driver = webdriver.Chrome()
    # context.driver = webdriver.PhantomJS()
    #context.driver = webdriver.Firefox()
    #executable_path = "C:\Users\trand\PycharmProjects\AutomationInternship\geckodriver.exe"

    ## HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(chrome_options=options)

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    #context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    ### for browerstack ###
    # desired_cap = {
    #     'browser': 'Safari',
    #     'os_version': 'Big Sur',
    #     'os': 'OS X',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()