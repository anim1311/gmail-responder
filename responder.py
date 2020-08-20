from selenium import webdriver
from time import sleep

driver = None
driver = webdriver.Firefox(executable_path= '<path to firefox driver>')

SENDER = "<your name>"
GMAIL_USER = '<your email id>'
GMAIL_PASSWORD = '<your password>'
MESSAGE = 'I will get back to you soon. \n Thanks'



def access_gmail():
    try:
        driver.get('http://gmail.com')
        sleep(1)
        # Go thru messages list
        m = driver.find_elements_by_css_selector('.UI table > tbody > tr')

        for a in m:
            if SENDER.lower() in a.text:
                a.click()
                break

        # take rest
        sleep(1)
        reply = driver.find_element_by_css_selector('.amn > span')
        sleep(1)
        if reply:
            reply.click()
            sleep(1)

            # Access editor to write response
            editable = driver.find_element_by_css_selector('.editable')
            if editable:
                editable.click()
                editable.send_keys(MESSAGE)

            send = driver.find_elements_by_xpath('//div[@role="button"]')
            for s in send:
                if s.text.strip() == 'Send':
                    s.click()

    except Exception as ex:
        print(str(ex))
    finally:
        return True


def login_google():
    is_logged_in = False
    google_login = 'https://accounts.google.com/Login#identifier'

    try:
        driver.get(google_login)
        sleep(1)
        html = driver.page_source.strip()

        # email box
        user_name = driver.find_element_by_xpath('//*[@id="identifierId"]')

        user_name.send_keys(GMAIL_USER)

        next = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span')
        if next:
            next.click()

        # give em rest
        sleep(1)

        # now enter passwd
        user_pass = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')

        user_pass.send_keys(GMAIL_PASSWORD)

        # rest again
        sleep(1)

        sign_in = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')

        sign_in.click()

        # rest again
        sleep(1)
        is_logged_in = True

    except Exception as ex:
        print(str(ex))
        is_logged_in = False
    finally:
        return is_logged_in


if __name__ == '__main__':
    r_log = login_google()
    if r_log:
        print('Yay')
        access_gmail()
    else:
        print('Boo!!!')

    if driver is not None:
        driver.quit()

    print('Done')
