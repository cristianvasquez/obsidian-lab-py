class Plugin:

    def __init__(self, *args, **kwargs):
        super()

    def execute(self, note_path, text):
        

        if text is not None:
            return {
                "contents": text.upper()
            }
        else:
            return {

        }
