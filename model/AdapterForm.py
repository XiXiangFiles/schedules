class AdpterForm():
    def adpter(self,classname):
        return eval(classname)
    def get_workers(self, parameter_list):
        raise NotImplementedError

class DictForm(AdpterForm):
    def __init__(self, path):
        self.path = path
        self.members = {}

    def __load_form(self):
        file = open(self.path,'r')
        context = file.read()
        file.close()
        return  context

    def __set_member(self, name,position,numbers):
        for index,num in enumerate(numbers):
            self.members[str(num)] = {'name':name[index] ,'position':position[index],'holidays':[]}
    
    def __set_member_holiday(self,member_num,holiday_num):
        self.members[str(member_num)]['holidays'].append(holiday_num)

    def __set_member_schedule(self,calendar):
        allnum = [num for num in self.members.keys()]
        for  index, day_list in enumerate(calendar):
            day = day_list[0]
            who_work = day_list[2:]
            for index_of_who_wok in range(0,len(who_work)):
                if who_work[index_of_who_wok]:
                    self.__set_member_holiday(allnum[index_of_who_wok],day)

    def get_workers(self):
        def split_form():
            return self.__load_form().split('\n')
        def took_num():
            return schedule[0].split(',')[2:]
        def list_position():
            return schedule[1].split(',')[2:]
        def list_name():
            return schedule[2].split(',')[2:]
        def took_member_workform():
            calendar = schedule[3:]
            return [c.split(',') for c in calendar ]
        schedule = split_form()
        numbers = took_num()
        position = list_position()
        name = list_name()
        self.__set_member(name,position,numbers)
        calendar = took_member_workform()
        self.__set_member_schedule(calendar)
        return self.members

class member:
    def __init__(self):
        self.name = ""
        self.num = ""
        self.workdays = []
        self.holidays = []

class ObjectForm(AdpterForm):
    def __init__(self, path):
        self.path = path
        self.members = []

    def __load_form(self):
        file = open(self.path,'r')
        context = file.read()
        file.close()
        return  context

    def __set_member(self, name,position,numbers):
          for i,num in enumerate(numbers):
            m = member()
            m.num = num
            m.name =name[i]
            m.position = position[i]
            m.workdays = []
            m.holidays = []
            self.members.append(m)

    def __get_member(self, member_num):
        return self.members[member_num]

    def __set_member_holiday(self,member_num,holiday_num):
        member = self.__get_member(member_num)
        member.holidays.append(holiday_num)
        
    def __set_member_schedule(self,calendar):
        for  index, day_list in enumerate(calendar):
            day = day_list[0]
            who_work = day_list[2:]
            for index_of_who_wok in range(0,len(who_work)):
                if who_work[index_of_who_wok]:
                    self.__set_member_holiday(index_of_who_wok,day)

    def get_workers(self):
        def split_form():
            return self.__load_form().split('\n')
        def took_num():
            return schedule[0].split(',')[2:]
        def list_position():
            return schedule[1].split(',')[2:]
        def list_name():
            return schedule[2].split(',')[2:]
        def took_member_workform():
            calendar = schedule[3:]
            return [c.split(',') for c in calendar ]
        schedule = split_form()
        numbers = took_num()
        position = list_position()
        name = list_name()
        calendar = took_member_workform()
        self.__set_member(name,position,numbers)
        self.__set_member_schedule(calendar)
        return self.members
        

# if __name__ == "__main__":
#     test = AdpterForm().adpter("ObjectForm")("./schedules.csv").get_workers()
#     print(test)
#     AdpterForm().adpter("DictForm")("/home/ubuntu/桌面/scheduls/schedules.csv").get_workers()
    
