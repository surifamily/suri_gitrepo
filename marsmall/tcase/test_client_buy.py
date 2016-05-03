# coding=utf-8
import pyse
import ConfigParser
import task.mgr_login
import task.client_action
import codecs


class TestClientBuy:
    '''test client buy '''
        
    def setup(self):
        #task.mgr_login.MgrLogin.setUp(self)

        cf = ConfigParser.ConfigParser()          
        cf.read("../conf/basic.ini")
        cf.read("../conf/mgr.ini")
        
        self.driver = pyse.Pyse(cf.get("baseconf", "browser"))
        self.driver.wait(30)
        self.driver.max_window()
        
        self.mgr_url ="http://"+cf.get("baseconf", "ipport")+"/mgr/login" 
        self.base_url = "http://"+cf.get("baseconf", "ipport")+"/client/login"       
        self.name=cf.get("mgrconf", "name")
        self.password=cf.get("mgrconf", "password")
        
         
    '''def test_mgr_creat_category(self):
        task.mgr_login.test_login(self)
        self.driver.wait
        text = self.driver.get_text("h1")
        print(text)
        assert "尚云电商平台概况 " in text
        
        driver=self.driver
        
        driver.scroll_into_view("//span[text()='网站信息管理']")
        driver.click_by("//span[text()='网站信息管理']","xpath")
        driver.click_text("货品类别管理")          
        driver.click_text("新增")
        print("create new category")

        driver.type("#mgr-form-prcate_name", "SampleCat")
        driver.type("#mgr-form-prcate_sort","10")
        driver.select("#mgr-form-prcate_is_dynamic_price","0","value")        
        driver.click_by("(//button[@type='button'])[2]","xpath")'''
     
               
    def test_provider_create_goods(self):
        cf1=ConfigParser.ConfigParser()
        print "start reading"
        cf1.readfp(codecs.open("../conf/provider.ini", "r", "utf-8-sig"))
        client_cellphone=cf1.get("regconf", "client_cellphone")
        client_password=cf1.get("regconf", "client_password")
        #print client_cellphone
        #print client_password
        task.client_action.login(self, client_cellphone, client_password)
        task.client_action.create_goods(self)

    '''    
    def test_client_buy_goods(self): 
        cf = ConfigParser.ConfigParser()          
        cf.readfp(codecs.open("../conf/consumer.ini", "r", "utf-8-sig"))
        client_cellphone=cf.get("regconf", "client_cellphone")
        client_password=cf.get("regconf", "client_password")
        task.client_action.login(self, client_cellphone, client_password)    
        driver=self.driver
        driver.click_text("尚云商城")
    '''
        
    def teardown(self):
        self.driver.quit()
       
if __name__ == '__main__':
    test_pro = pyse.TestRunner()
    test_pro.run()

