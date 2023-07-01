import os

def clear_cloud():
    lst = os.listdir("static/cloud")
    for i in lst:
        if "ignore.ignore" == i:
            pass
        else:os.remove("static/cloud/"+i)

def clear_temp():
    lst = os.listdir("static/temp")
    for i in lst:
        if "ignore.ignore" == i:
            pass
        else:os.remove("static/temp/"+i)