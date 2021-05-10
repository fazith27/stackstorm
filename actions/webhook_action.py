import json
from st2common.runners.base_action import Action


class MyWebhookAction(Action):
    
    def run(self, payload, **params):
        print(payload)
        print(type(payload))
        payload = json.dumps(payload).encode()
        # payload["name"] = params["name"]
        # payload["type"] = params["type"]
        # payload["base"] = params["base"]
        print(payload)
        print(type(payload))
        print(params["name"])
        print(params["type"])
        print(params["base"])