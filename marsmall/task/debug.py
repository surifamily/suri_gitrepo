# coding=utf-8
import pyse
import unittest
import codecs
import ConfigParser
from time import sleep
import task.client_action

class Register(unittest.TestCase):    
    def setUp(self):        
        cf = ConfigParser.ConfigParser()  
        #cf.readfp(codecs.open("../conf/testdata.ini", "r", "utf-8-sig"))  
        cf.read("../conf/basic.ini")
        
        self.driver = pyse.Pyse(cf.get("baseconf", "browser"))
        self.base_url ="http://"+cf.get("baseconf", "ipport")+"/client/goods/table/add"
        
        
    
    def test_debug(self):    
        driver = self.driver
        driver.open(self.base_url)
        driver.max_window()
        task.client_action.login(self,"13693339536","123456")
        driver.wait
        driver.click_text("我的尚云")
        driver.click_text("挂货管理")
        driver.click(".fa-plus")
        text = driver.get_text("[data-url='/mgr/product/table/add']")
        print text
    
    def teardown(self):
        self.driver.quit()
    
if __name__ == '__main__':
#    now = time.strftime("%Y-%m-%d_%H_%M_%S")
#    test_report = "nosetests ./test_login.py --with-html --html-report=./\\report\\"+now+"report.html --html-report-template=C:\\Python27\\lib\\site-packages\\pyse\\html_reporting\\templates\\report2.jinja2"
#    print test_report
#    os.system(test_report)
    unittest.main()