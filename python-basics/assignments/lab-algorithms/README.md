# Lab: Algorithms
The assignment in this lab was to create a savings goal tracking system. This included defining the main features, the data needed to define the system, and writing pseudocode for the main functionalities.

## Main Functionality Explanation

1. Savings Goal
The savings goal should be set by a user and should specify a target date and target amount for the amount of money they would like to have saved by the target date.

2. Savings Progress
Users should be able to update their savings progress.

3. Savings Goal Status
Users should be able to view the statuses of their goals. This should inform the user of their current amount saved and a summary of their goal(s).

4. Savings Goal Notification
When a user logs in for the day, notifications should arrive if they have an approaching goal that they have not yet met.


## Main Functionality Pseudocode 

function createSavingsGoal(userID, targetAmount, targetDate) {
    create SavingsGoal{userID, targetAmount, targetDate} with 0 amountSaved
    store SavingsGoal in database, retrieving newly created ID
    return SavingsGoalID
}

function updateSavingsGoal(userID, savingsGoalID, savingsAmount) {
    retrieve SavingsGoal from database using userID, savingsGoalID
    update SavingsGoal, adding savingsAmount to existing amountSaved
    store updated SavingsGoal in database
    return SavingsGoal with updated amountSaved
}

function getSavingsGoalStatus(userID, savingsGoalID) {
    retrieve SavingsGoal from database using userID, savingsGoalID
    compose a status message with amount left, days remaining
    display status message
}

'X' days will be a configurable constant value
function notifyDueSavingsGoal(userID, savingsGoalID) {
    retrieve SavingsGoal from database using userID, savingsGoalID
    if SavingsGoal.TargetDate is within X days and SavingsGoal.AmountSaved < SavingsGoal.TargetAmount {
        compose a notification with amountSaved, targetAmount, days remaining
        send notification to user
    }
}

## Program Notes
I have divided the program in `main.py` into a few sections to help split up the file into more digestible chunks. The second section contains the implementation of the main functionality pseudocode from above.

Run the program `python main.py` and follow the prompts to test main functionalities. The program starts with today's date and allows you to advance the date in order to test the notification functionality.