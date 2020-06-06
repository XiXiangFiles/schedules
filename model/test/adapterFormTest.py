import sys
sys.path.append("../")
from AdapterForm import AdpterForm
from unittest import TestCase, main
class AdapterFormTest(TestCase):
    def test_DictForm_num(self):
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase.csv").get_workers()
        self.assertEqual(['A', '1', '2', '3', '4', 'B', '5', '6', '7', '13', '8', '9', '10', '11', '14', '12', '15'],[x for x in testcase_allworkers.keys()],"test the member num with case1")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase2.csv").get_workers()
        self.assertEqual(['A','1','2','3','4','B','5','6','7','8','10','11','12','15'],[x for x in testcase_allworkers.keys()],"test the member num with case2")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase3.csv").get_workers()
        self.assertEqual(['A','1','2','3','4','B','5','6','7','13','8','9','10','11','14'],[x for x in testcase_allworkers.keys()],"test the member num with case3")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase4.csv").get_workers()
        self.assertEqual(['A','1','2','3','4','5','6','7','13','8','9','10','11','14'],[x for x in testcase_allworkers.keys()],"test the member num with case4")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase5.csv").get_workers()
        self.assertEqual(['A','1','2','4','5','6','7','8','9','10','11'],[x for x in testcase_allworkers.keys()],"test the member num with case5")

    def test_DictForm_name(self):
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','藍慶淵','劉志堅','林耿立','林文軒','林郁凱','簡呈軒','江仁傑','林育生','馬紹武','陳麒仲','汪子翔','簡佑勳'],[testcase_allworkers[key]['name'] for key in testcase_allworkers.keys()],"test the member name with case1")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase2.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','藍慶淵','劉志堅','林耿立','林文軒','簡呈軒','林育生','馬紹武','汪子翔','簡佑勳'],[testcase_allworkers[key]['name'] for key in testcase_allworkers.keys()],"test the member name with case2")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase3.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','藍慶淵','劉志堅','林耿立','林文軒','林郁凱','簡呈軒','江仁傑','林育生','馬紹武','陳麒仲'],[testcase_allworkers[key]['name'] for key in testcase_allworkers.keys()],"test the member name with case3")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase4.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','劉志堅','林耿立','林文軒','林郁凱','簡呈軒','江仁傑','林育生','馬紹武','陳麒仲'],[testcase_allworkers[key]['name'] for key in testcase_allworkers.keys()],"test the member name with case4")
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase5.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','蔡菖桀','劉志堅','林耿立','林文軒','簡呈軒','江仁傑','林育生','馬紹武'],[testcase_allworkers[key]['name'] for key in testcase_allworkers.keys()],"test the member name with case5")
    
    def test_DictForm_holidays(self):
        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase.csv").get_workers()
        case1_ans = [['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],
        ['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],['3','6','9','12','15','18','21','24','27','30'],
        ['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],
        ['4','7','10','13','16','19','22','25','28','31'],['4','7','10','13','16','19','22','25','28','31'],['4','7','10','13','16','19','22','25','28','31'], ['4','7','10','13','16','19','22','25','28','31'],
        ['4','7','10','13','16','19','22','25','28','31'],['2','6','12','13','14','15','21','25','29'],['3','7','8','16','19','20','24','27','28']]
        case1_compare = [testcase_allworkers[key]['holidays'] for key in testcase_allworkers.keys()]
        for index, mem in enumerate(case1_compare):
            self.assertEqual(case1_ans[index],case1_compare[index],"test the member holidays with case1")

        testcase_allworkers = AdpterForm().adpter("DictForm")("./testcase/testcase2.csv").get_workers()
        case2_ans = [['2','5','8','11','14','17','20','23','26','29'],
        ['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],
        ['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],
        ['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],
        ['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],
        ['4','7','10','13','16','19','22','25','28','31'],['4','7','10','13','16','19','22','25','28','31'],
        ['4','7','10','13','16','19','22','25','28','31'],['2','6','12','13','14','15','21','25','29'],
        ['3','7','8','16','19','20','24','27','28']]
        case2_compare = [testcase_allworkers[key]['holidays'] for key in testcase_allworkers.keys()]
        for index, mem in enumerate(testcase_allworkers):
            self.assertEqual(case2_ans[index],case2_compare[index],"test the member holidays with case2")
        
    
    def test_ObjectForm_num(self):
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase.csv").get_workers()
        self.assertEqual(['A', '1', '2', '3', '4', 'B', '5', '6', '7', '13', '8', '9', '10', '11', '14', '12', '15'],[x.num for x in testcase_allworkers],"test the member num with case1")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase2.csv").get_workers()
        self.assertEqual(['A','1','2','3','4','B','5','6','7','8','10','11','12','15'],[x.num for x in testcase_allworkers],"test the member num with case2")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase3.csv").get_workers()
        self.assertEqual(['A','1','2','3','4','B','5','6','7','13','8','9','10','11','14'],[x.num for x in testcase_allworkers],"test the member num with case3")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase4.csv").get_workers()
        self.assertEqual(['A','1','2','3','4','5','6','7','13','8','9','10','11','14'],[x.num for x in testcase_allworkers],"test the member num with case4")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase5.csv").get_workers()
        self.assertEqual(['A','1','2','4','5','6','7','8','9','10','11'],[x.num for x in testcase_allworkers],"test the member num with case5")
    
    def test_ObjectForm_name(self):
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','藍慶淵','劉志堅','林耿立','林文軒','林郁凱','簡呈軒','江仁傑','林育生','馬紹武','陳麒仲','汪子翔','簡佑勳'],[x.name for x in testcase_allworkers],"test the member name with case1")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase2.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','藍慶淵','劉志堅','林耿立','林文軒','簡呈軒','林育生','馬紹武','汪子翔','簡佑勳'],[x.name for x in testcase_allworkers],"test the member name with case2")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase3.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','藍慶淵','劉志堅','林耿立','林文軒','林郁凱','簡呈軒','江仁傑','林育生','馬紹武','陳麒仲'],[x.name for x in testcase_allworkers],"test the member name with case3")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase4.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','王哲毓','蔡菖桀','劉志堅','林耿立','林文軒','林郁凱','簡呈軒','江仁傑','林育生','馬紹武','陳麒仲'],[x.name for x in testcase_allworkers],"test the member name with case4")
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase5.csv").get_workers()
        self.assertEqual(['吳嘉慶','簡淳宇','徐國泰','蔡菖桀','劉志堅','林耿立','林文軒','簡呈軒','江仁傑','林育生','馬紹武'],[x.name for x in testcase_allworkers],"test the member name with case5")
    
    def test_ObjectForm_holidays(self):
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase.csv").get_workers()
        case1_ans = [['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],
        ['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],['3','6','9','12','15','18','21','24','27','30'],
        ['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],
        ['4','7','10','13','16','19','22','25','28','31'],['4','7','10','13','16','19','22','25','28','31'],['4','7','10','13','16','19','22','25','28','31'], ['4','7','10','13','16','19','22','25','28','31'],
        ['4','7','10','13','16','19','22','25','28','31'],['2','6','12','13','14','15','21','25','29'],['3','7','8','16','19','20','24','27','28']]
        for index, mem in enumerate(testcase_allworkers):
            self.assertEqual(case1_ans[index],mem.holidays ,"test the member holidays with case1")
        
        testcase_allworkers = AdpterForm().adpter("ObjectForm")("./testcase/testcase2.csv").get_workers()
        case2_ans = [['2','5','8','11','14','17','20','23','26','29'],
        ['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],
        ['2','5','8','11','14','17','20','23','26','29'],['2','5','8','11','14','17','20','23','26','29'],
        ['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],
        ['3','6','9','12','15','18','21','24','27','30'],['3','6','9','12','15','18','21','24','27','30'],
        ['4','7','10','13','16','19','22','25','28','31'],['4','7','10','13','16','19','22','25','28','31'],
        ['4','7','10','13','16','19','22','25','28','31'],['2','6','12','13','14','15','21','25','29'],
        ['3','7','8','16','19','20','24','27','28']]
        for index, mem in enumerate(testcase_allworkers):
            self.assertEqual(case2_ans[index],mem.holidays ,"test the member holidays with case2")
        

if __name__ == "__main__":
    main()
