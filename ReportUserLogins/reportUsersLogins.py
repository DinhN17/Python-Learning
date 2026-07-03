# This program will report all currently logged in to the machine
import os

# Function to get the machines and the currently logged in users.
# It receives the list of events and returns the dictionary of machines
# and currently logged in users.
def get_current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in machines[event.machine]:
      machines[event.machine].remove(event.user)
  return machines 

# Function to generate the report of the machines and users currently logged in
# It receives the dictionary with keys of machines and values of currently logged in users
# and prints the report to the standard output.
def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

# Function to get date of the event: receiving the event as a parameter and
# returning the date as a string.
def get_event_date(event):
  return event.date

# Class of Event: event_date, event_type, user, machine_name
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user