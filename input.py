from browser import document

class Input:
    def __init__(self):
        document.bind("keydown",self._handle)
    
    def _handle(self, ev):
        print("key: ", repr(ev.key))