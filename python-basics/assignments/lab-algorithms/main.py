

from datetime import date, timedelta


#############################################################################################
####### This section contains the in-memory datastores used by the main functionalities #####
#############################################################################################

GOAL_ALERT_THRESHOLD = 3 # days

savings_goals_db = {} 
user_db = []
todays_date = date.today()

def advance_date():
    global todays_date
    td = todays_date
    todays_date = td + timedelta(days=1)

next_user_id = 1
def get_user_id():
    global next_user_id
    id = next_user_id
    next_user_id+=1
    return id

next_savings_goal_id = 1
def get_savings_goal_id():
    global next_savings_goal_id
    id = next_savings_goal_id 
    next_savings_goal_id+=1
    return id

#############################################################################################
##### This section contains the required code that implements each main functionality #######
#############################################################################################

class SavingsGoal:
    def __init__(self, user_id, target_amount, target_date):
        self.goal_id = get_savings_goal_id()
        self.user_id = user_id
        self.target_amount = target_amount
        self.target_date = target_date
        self.current_saved = 0
    
def create_savings_goal(user_id, target_amount, target_date):
    sg = SavingsGoal(user_id, target_amount, target_date)
    savings_goals_db[sg.goal_id] = sg
    return sg.goal_id
    

def update_savings_goal(user_id, savings_goal_id, savings_amount):
    sg = savings_goals_db[savings_goal_id]
    if user_id != sg.user_id:
        raise PermissionError("This goal does not belong to the specified user.") 
    
    sg.current_saved += savings_amount
    savings_goals_db[savings_goal_id] = sg
    return sg

def get_savings_goal_status(user_id, savings_goal_id):
    sg = savings_goals_db[savings_goal_id]
    if user_id != sg.user_id:
        raise PermissionError("This goal does not belong to the specified user.") 
    print(f"savings goal target date = {sg.target_date}\n") 
    daysLeft = (sg.target_date - todays_date).days
    return f"User{user_id}'s Savings Goal {savings_goal_id}: Have saved ${sg.current_saved} out of ${sg.target_amount}. ${sg.target_amount - sg.current_saved} left to save and {daysLeft} days remaining"
    

def notify_due_savings_goal(user_id, savings_goal_id):
    sg = savings_goals_db[savings_goal_id]
    if user_id != sg.user_id:
        raise PermissionError("This goal does not belong to the specified user.") 
    
    diff = (sg.target_date-todays_date).days
    if  diff < GOAL_ALERT_THRESHOLD:
        notification = f"User{sg.user_id}'s Savings Goal {sg.goal_id} is due in {diff} days. ${sg.current_saved} out of ${sg.target_amount} - ${sg.target_amount - sg.current_saved} left.\n"
        return send_notification(notification)

# this should be implemented as sending an email, but for scope of assignment 
# we just send the notification to be printed later.
def send_notification(notification):
    return notification 
    
    
#############################################################################################
####### This section contains code that is used to Demo the main functionality using ########
####### the command line to retrieve user input. Start by adding a user to allow     ########
####### more menu options to appear to test the main functionality. Use the "Go to   ########
####### next day" option to advance the day, potentially triggering any notifications########
#############################################################################################

def confirm_to_continue(msg):
    print(msg + ". Press 'enter to continue.")
    input()
    
class SystemDemo:
    def __init__(self):
        self.menu_options = {
            "0": exit,
            "1": advance_date,
            "2": self.add_user,
            "3": self.create_savings_goal_option,
            "4": self.update_savings_goal_option,
            "5": self.get_savings_goal_status_option
        }
        
    def run(self):
        while True:
            user_input = self.display_prompt()
            if user_input in self.menu_options:
                self.menu_options[user_input]()
            else:
                confirm_to_continue("Invalid menu option")
                

    def add_user(self):
        user_db.append(get_user_id())
    
    def create_savings_goal_option(self):
        prompt = f"== Create Savings Goal Menu ==\n\n"
        prompt += f"Available Users: [{", ".join([str(id) for id in user_db])}]\n"
        print(prompt)
        i = input("Example for user '5' to save $200 by Jan 2 2026 -> `5,1,2,2026,200`\nEnter a new goal: ")
        inputs = i.split(",")
        if len(inputs) != 5:
            confirm_to_continue("Requires 5 arguments separated by commas")
            return  
        
        userID, month, day, year, target_amount = int(inputs[0]),int(inputs[1]),int(inputs[2]), int(inputs[3]), int(inputs[4])
        if userID not in user_db:
            confirm_to_continue("User ID not found in database")
            return
        
        try:
            target_date = date(year, month, day)
        except ValueError:
            confirm_to_continue("Invalid date entered")
            return
        savings_goal_id = create_savings_goal(userID, target_amount, target_date)
        confirm_to_continue(f"Created savings with id '{savings_goal_id}'")
        
    def update_savings_goal_option(self):
        prompt = f"== Update Savings Goal Menu ==\n\n"
        prompt += f"Available Goals to update: [{", ".join([str(id) for id in savings_goals_db])}]"
        print(prompt)
        goal_id = int(input("Enter an id from Available Goals to update: "))
        if goal_id not in savings_goals_db:
            confirm_to_continue("That id is not in the Available Goals")
            return
        sg = savings_goals_db[goal_id]
        amount_saved = int(input(f"Enter the amount you saved towards goal {sg.goal_id}: "))
        sg = update_savings_goal(sg.user_id, sg.goal_id, amount_saved)
        confirm_to_continue(f"Updated goal {sg.goal_id}. Saved ${sg.current_saved} out of ${sg.target_amount}") 
        return
    
    def get_savings_goal_status_option(self):
        prompt = f"== Get Savings Goal Status Menu ==\n\n"
        prompt += f"Available Goals to view: [{", ".join([str(id) for id in savings_goals_db])}]"
        print(prompt)
        goal_id = int(input("Enter an id from Available Goals to view the status of: "))
        if goal_id not in savings_goals_db:
            confirm_to_continue("That id is not in the Available Goals")
            return
        sg = savings_goals_db[goal_id]
        status = get_savings_goal_status(sg.user_id, goal_id)
        confirm_to_continue(status)
        return
        
        
    def display_prompt(self):
        prompt = f"\n== {todays_date} Welcome to the Savings Goal Tracker ==\n\n"
        for goal_id in savings_goals_db:
            sg = savings_goals_db[goal_id]
            notification = notify_due_savings_goal(sg.user_id, sg.goal_id)
            if notification:
                prompt += notification
            
        prompt += "\n0 - Exit program\n"
        prompt += "1 - Go to next day\n"
        prompt += f"2 - Add new User\n"
        if user_db:
            prompt += f"3 - Create Savings Goal\n"
        if savings_goals_db:
            prompt += f"4 - Update a Savings Goal\n"
            prompt += f"5 - Get Savings Goal Status\n"
        print(prompt)
        return input("Select an option from the above menu: ") 

sd = SystemDemo()
sd.run()