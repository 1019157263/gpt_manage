# -*- coding:utf-8 -*-
"""
@desc: 
"""
import os
import platform

from selenium import webdriver

is_windows = platform.platform().startswith("Windows")
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--safe-mode')
options.add_argument('--window-size=1920,1080')
options.add_argument('--first-startup=false')
options.add_argument('--devtools')
profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
profile.set_preference("dom.webdriver.enabled", False)  # 设置非driver驱动
profile.set_preference('useAutomationExtension', False)  # 关闭自动化提示

profile.update_preferences()  # 更新设置
if is_windows:
    driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
else:
    driver = webdriver.Firefox(firefox_options=options,firefox_profile=profile,firefox_binary="/data/firefox/firefox")

driver.get('http://www.baidu.com')
js="return window.navigator.userAgent"
print(driver.execute_script(js))
driver.quit()