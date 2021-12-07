'''create a dictionary'''
class Dict:

    def creating_dict(self):

        dict1={}
        for i in range(3):
            key_ele=input("enter the key elements")
            value_ele=input("enter the value elements")
            dict1[key_ele]=value_ele
        return dict1

obj=Dict()
result=obj.creating_dict()
print("the created dictionary",result)

