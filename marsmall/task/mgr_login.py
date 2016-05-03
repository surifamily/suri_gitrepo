# coding=utf-8
      
def test_login(self):    
        driver = self.driver
        driver.open(self.mgr_url)
        driver.type("[name=name]",self.name)
        driver.type("[name=password]", self.password)        
        driver.click("[type=submit]")
        print("mgr login ")
