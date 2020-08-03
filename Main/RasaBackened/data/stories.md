## say hello
* greet
  - utter_greet
  - form_info
  - form{"name": "form_info"}
  - form{"name":"null"}

## New Story

* greet
    - utter_greet
    - form_info
    - form{"name":"form_info"}
    - slot{"requested_slot":"userID"}
* userID{"userID":"pv2012"}
    - slot{"userID":"pv2012"}
    - form_info
    - slot{"userID":"pv2012"}
    - slot{"requested_slot":"password"}
* password{"password":"password"}
    - slot{"password":"password"}
    - form_info
    - slot{"password":"password"}
    - form{"name":null}
    - slot{"requested_slot":null}
* emergency
    - utter_emergency

## New Story

* greet
    - utter_greet
    - form_info
    - form{"name":"form_info"}
    - slot{"requested_slot":"userID"}
* userID{"userID":"pv2012"}
    - slot{"userID":"pv2012"}
    - form_info
    - slot{"userID":"pv2012"}
    - slot{"requested_slot":"password"}
* password{"password":"password"}
    - slot{"password":"password"}
    - form_info
    - slot{"password":"password"}
    - form{"name":null}
    - slot{"requested_slot":null}
* timetable
    - utter_timetable
* attendence
    - utter_attendece

## Story from conversation with ecfe665b8d60403a9a4c56eb6057c87f on May 18th 2020

* greet
    - utter_greet
    - form_info
    - form{"name":"form_info"}
    - slot{"requested_slot":"userID"}
* userID{"userID":"pv2012"}
    - slot{"userID":"pv2012"}
    - slot{"userID":"pv2012"}
    - form_info
