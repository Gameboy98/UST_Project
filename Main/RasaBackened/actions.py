from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_your_num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="Hello World!")
        print(tracker.get_slot('num'))
        # dispatcher.utter_template('utter_your_num', tracker, number=details[str(tracker.get_slot('NAME')).lower()])
        return []


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        return "form_info"

    @staticmethod																																													
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["userID", "password"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot('userID')=="pv2012" and tracker.get_slot('password')=="Pass@1334":
        	dispatcher.utter_message(template="utter_help", name=tracker.get_slot('userID'),)
        else:
        	dispatcher.utter_message(template="utter_wrong")
        return []


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "userID": [self.from_entity(entity="userID", intent='userID'),
                     self.from_text()],
            "password": [self.from_entity(entity="password", intent="password"),
                        self.from_text()],
        }

    # @staticmethod
    # def brand_db() -> List[Text]:
    #     return [
    #         {"userID":"pv2012", "password":"password"}
    #     ]

    # def validate_brand(
    #         self,
    #         value: Text,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     print(value)
    #     if value.lower() in self.cuisine_db():
    #         return {"BRAND": value}
    #     else:
    #         print(value)
    #         dispatcher.utter_message(template="utter_wrong_value")
    #         return {"BRAND": None, "password":None}