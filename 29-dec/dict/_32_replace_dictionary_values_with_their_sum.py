'''Replace dictionary values with their sum'''
def sum_maths_v_vi_average(lists):
    for d in lists:
        n1=d.pop('v')
        n2=d.pop('vi')
        d['v+vi']=(n1+n2)/2
    return lists
student_details=[
    { 'id':1,'subject':'maths','v':70,'vi':82},
    { 'id':2,'subject':'maths','v':73,'vi':74},
    { 'id':3,'subject':'maths','v':75,'vi':96},

]
print(sum_maths_v_vi_average(student_details))