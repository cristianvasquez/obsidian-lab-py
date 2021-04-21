import os

class Plugin:

    def __init__(self, *args, **kwargs):                
        self.plugin_name = os.path.basename(__file__)
        super()
        

    def execute(self, args):
        print('request',self.plugin_name,args)

        text = args['text']
        if text is not None:
            return {
                "contents": text.upper()
            }
        else:
            return {
            
        }
