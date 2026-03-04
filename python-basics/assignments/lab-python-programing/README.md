# Python Fundamentals - Lab: Python Programming
This lab asked me to create a Python script that calculates the total cost of a pizza order based on various factors:

Pizza sizes and base prices:
- Small pizza: $8
- Large pizza: $12

Toppings: $1 for each additional topping

Delivery Fee:
- $2 for the first 5 miles
- $1 for each additional mile

## Program Scope

The problem says to calculate the total cost of "a" pizza. I can assume that we will only be taking orders for a single pizza. 

The program should get order details from the user for a single pizza, process the details, and returns the total cost of the order to the user. Once the program displays this result it can exit.

The instructions state that the user should input every specific detail (number of toppings, delivery distance in miles). I am also assuming miles can be a whole integer to simplify a bit more.

The delivery fee is $2 for the first 5 miles, so I am assuming any amount less than 5 miles will still cost $2. Since a house can technically be less than half a mile from a pizza store, I am assuming that a delivery distance of 0 miles is possible and will still cost $2.

## Program Flow

1. Initialize a pizza order with cost of $0

2. Prompt user for desired size and adjust cost

3. Prompt user for number of toppings and adjust cost

4. Prompt user for delivery distance (in miles) and adjust cost

5. Display final total cost to user

6. Exits

## Pseudocode

<!-- This class holds the high level logic of the program -->
class PizzaOrderTaker {
    run()
        order = PizzaOrderBuilder()
            .addSize()
            .addToppings()
            .addDeliveryDistance()
            .build()
        
        order.display()
}

<!-- This is a data class to hold the raw data of a pizza order -->
class PizzaOrder {
    size string // "Small" or "Large"
    numToppings integer
    deliveryDist integer // miles
    total_cost float // $

    display()
        order_str = "Your {size} pizza with {numToppings} topping(s) will travel {deliveryDist} mile(s) to be delivered to you for a total cost of {total_cost}".
        print order_str to user
}

<!-- This class uses the builder pattern to construct a pizza order -->
class PizzaOrderBuilder {
    order PizzaOrder

    addSize()
        size = receive input from user
        while size is not valid
            handle error of invalid size 
            size = receive input from user again
        order.size = size
        order.cost += price for size
    
    addToppings()
        numToppings = receive input from user
        while numToppings is less than 0
            handle error of invalid numToppings
            numToppings = receive input from user
        order.numToppings = numToppings
        order.cost += numToppings * costPerTopping

    addDeliveryDistance()
        deliveryDist = receive input from user
        while deliveryDist is less than 0
            handle error of invalid deliveryDist
            deliveryDist = recieve input from user
        order.deliveryDist = deliveryDist
        order.total_cost += firstFiveMileCost
        remainingMiles = deliveryDist - 5
        if remainingMiles greater than 0
            order.total_cost += remainingMile
        
    build()
        return order
}

## Running
