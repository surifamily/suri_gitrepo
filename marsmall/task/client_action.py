# coding=utf-8      
def login(self, name, pw):    
        driver = self.driver
        driver.open(self.base_url)
        driver.type("[name=client_cellphone]",name)
        driver.type("[name=client_password]", pw)
        driver.click("[type=checkbox]")
        driver.click("#btn-submit")

def create_goods(self,sn="sn001",name="goods001",cat="SampleCat",price="10000",payment="款到发货",delivery="m买方自提",vas_fee="10",note="blahblah"):        
        driver = self.driver
        driver.wait
        driver.click_text("我的尚云")
        driver.click_text("挂货管理")
        driver.click(".fa-plus")
        driver.type("#prod_sn", sn)
        driver.type("#prod_name", name)
        driver.select("#prod_category", cat, "label")
        driver.type("#prod_price", price)
        driver.select("#prod_payment", payment, "label")
        driver.select("#prod_delivery", delivery, "label")
        driver.type("#prod_vas_fee", vas_fee)
        driver.type("div.note-editable.panel-body",note)
        driver.click("[data-url='/mgr/product/table/add']")