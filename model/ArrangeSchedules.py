from AdapterForm import AdpterForm

class ArrangeSchedules:
    def __init__(self):
        self.adpDict =AdpterForm("ObjectForm")
        self.adpObject = AdpterForm("DictForm")

    def gen_skd(self,date):
        raise NotImplementedError

    def use(self,chooseStrategy):
        return eval(chooseStrategy)
    
class ContextComposition(ArrangeSchedules):
    def __init__(self,adp:str):
        super.__init__()

    def gen_skd(self,date):
        pass
    
class NoContextComposition(ArrangeSchedules):
    
    def __init__(self,adp:str):
        self.members = super.__init__(adp).adpObject.get_workers()


    def  __worked_on_last_day(self,day):
        pass 

    def gen_skd(self,day):
        
        pass