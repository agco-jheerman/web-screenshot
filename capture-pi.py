from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def capture_screen(url, screenshot_path):
    logger.debug('prepping chromedriver')

    """ 
    Note: the path to the chromedriver must be added to the system PATH: export PATH:=$PATH:${pwd} 
    Download the chromedriver from: https://sites.google.com/a/chromium.org/chromedriver/
    """
    DRIVER = 'chromedriver-pi'
    driver = webdriver.Chrome(DRIVER)
    logger.debug('requesting url')
    driver.get(url)
    logger.debug('saving screenshot')
    screenshot = driver.save_screenshot(screenshot_path)
    logger.debug('done')
    driver.quit()

if __name__ == "__main__":
    url = 'https://www.google.com'
    screenshot_path = 'google_homepage.png'
    logger.debug(f"Requesting page {url} and saving {screenshot_path}")
    capture_screen(url, screenshot_path)
