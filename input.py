from browser import document

KEYMAP = {
    "ArrowUp": "move_n",
    "ArrowDown": "move_s",
    "ArrowLeft": "move_w",
    "ArrowRight": "move_e",
    "w":"move_n",
    "s":"move_s",
    "a":"move_w",
    "d":"move_e",
    " ":"wait",
    ".":"wait",

}

class Input:
    def __init__(self,on_action):
        self.on_action = on_action
        document.bind("keydown",self._handle)
    
    def _handle(self, ev):
        action = KEYMAP.get(ev.key)
        if action is None:
            return
        ev.preventDefault()
        self.on_action(action)
