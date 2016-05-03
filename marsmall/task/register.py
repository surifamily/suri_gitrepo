# coding=utf-8
import pyse
import unittest
import codecs
import ConfigParser
from time import sleep

class Register(unittest.TestCase):    
    def setUp(self):        
        cf = ConfigParser.ConfigParser()  
        cf.readfp(codecs.open("../conf/testdata.ini", "r", "utf-8-sig"))  
        cf.read("../conf/basic.ini")
        
        self.driver = pyse.Pyse(cf.get("baseconf", "browser"))
        self.base_url ="http://"+cf.get("baseconf", "ipport")+"/client/register"
        
        #cf.read("../conf/user1.ini")
        self.cellphone = cf.get("regconf", "cellphone") 
        self.vcode = cf.get("regconf", "vcode")
        self.client_password = cf.get("regconf", "client_password")
        self.pay_password = cf.get("regconf", "pay_password")
        self.comp_name = cf.get("regconf", "comp_name")
        self.client_name = cf.get("regconf", "client_name")
        self.comp_district = cf.get("regconf", "comp_district")
    
    def test_register(self):    
        driver = self.driver
        driver.open(self.base_url)
        driver.max_window()
        driver.type("[name=client_cellphone]",self.cellphone)
        driver.type("[name=client_password]", self.vcode)
        driver.type("[name=vcode]", self.vcode)
        driver.type("[name=client_password]", self.client_password)
        driver.type("[name=comp_pay_password]", self.pay_password)
        driver.type("[name=comp_name]", self.comp_name)
        driver.type("[name=client_name]", self.client_name)
        driver.type("[name=comp_district]", self.comp_district)
        sleep(3)
        driver.click("[type=checkbox]")
        driver.click("#btn-submit")
        sleep(3)
        driver.accept_alert()
    
    def teardown(self):
        self.driver.quit()
    
if __name__ == '__main__':
#    now = time.strftime("%Y-%m-%d_%H_%M_%S")
#    test_report = "nosetests ./test_login.py --with-html --html-report=./\\report\\"+now+"report.html --html-report-template=C:\\Python27\\lib\\site-packages\\pyse\\html_reporting\\templates\\report2.jinja2"
#    print test_report
#    os.system(test_report)
    unittest.main()