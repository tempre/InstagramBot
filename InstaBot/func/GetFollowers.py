def getFollowers(self):
    self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.um))\
        .click()
    self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\
        .click()
