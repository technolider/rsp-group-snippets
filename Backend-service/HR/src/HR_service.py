import sys
sys.path.append("../../temp/src")

from service_template import Service

class HR_service(Service):
    def __init__(self):
        print("Class was consructed!")

obj = HR_service()
