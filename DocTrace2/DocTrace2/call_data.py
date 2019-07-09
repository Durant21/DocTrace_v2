from DocTrace2.BLL.Groups import BLL_Groups


def test_call():

   r = BLL_Groups.get_groups()
   return r

print(test_call())