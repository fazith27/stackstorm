import json
from st2common.runners.base_action import Action


class MyWebhookAction(Action):
    
    def run(self, payload, **params):
        payload = json.dumps(payload).encode()
        # payload["name"] = params["name"]
        # payload["type"] = params["type"]
        # payload["base"] = params["base"]
        print(payload)