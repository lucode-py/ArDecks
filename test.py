
action_map = 

data = "S1"
if data in action_map:
    action_info = self.action_map[data]
    action_type = action_info.get("action")
    value = action_info.get("value")
    
    if action_type in self.action_handlers:
        handler = self.action_handlers[action_type]
        if value:
            handler(value)
        else:
            handler()
    else:
        print(f"Action non reconnue: {action_type}")
else:
    print(f"Clé non reconnue: {data}")
