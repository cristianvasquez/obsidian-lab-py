import os

class Plugin:

    def __init__(self, *args, **kwargs):                
        self.plugin_name = os.path.basename(__file__)
        super()
        

    def execute(self, args):
        print('request',self.plugin_name,args)

        if "text" in args:
            return {
                "contents": args['text'].upper()
            }
        else:
            return {
                "contents": ''
            }