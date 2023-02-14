# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return 'action_hello_world'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text='Hello World!')

        return []


class ActionFindCategory(Action):
    def name(self) -> Text:
        return 'action_find_category'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category = tracker.get_slot('category')

        # TODO: call API
        list_product = [
            {
                'name': 'Product 1',
            }
        ]

        if len(list_product) > 0:
            dispatcher.utter_template('utter_list_product', tracker)
            dispatcher.utter_message(json_message={
                'payload': 'list_product',
                'data': {
                    'list_product': list_product,
                    'type': 'list_product'
                }
            })
        else:
            dispatcher.utter_template('utter_sorry', tracker)

        return []


class ActionFindSize(Action):
    def name(self) -> Text:
        return 'action_find_size'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        size = tracker.get_slot('size')

        # TODO: call API
        list_product = [
            {
                'name': 'Product 1',
            }
        ]

        if len(list_product) > 0:
            dispatcher.utter_template('utter_list_product', tracker)
            dispatcher.utter_message(json_message={
                'payload': 'list_product',
                'data': {
                    'list_product': list_product,
                    'type': 'list_product'
                }
            })
        else:
            dispatcher.utter_template('utter_sorry', tracker)

        return []


class ActionFindColor(Action):
    def name(self) -> Text:
        return 'action_find_color'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        color = tracker.get_slot('color')

        # TODO: call API
        list_product = [
            {
                'name': 'Product 1',
            }
        ]

        if len(list_product) > 0:
            dispatcher.utter_template('utter_list_product', tracker)
            dispatcher.utter_message(json_message={
                'payload': 'list_product',
                'data': {
                    'list_product': list_product,
                    'type': 'list_product'
                }
            })
        else:
            dispatcher.utter_template('utter_sorry', tracker)

        return []
