AllStateLearning
================


Data fields
------------

* *customer_ID* - A unique identifier for the customer
* *shopping_pt* - Unique identifier for the shopping point of a given customer
* *record_type* - 0=shopping point, 1=purchase point
* *day* - Day of the week (0-6, 0=Monday)
* *time* - Time of day (HH:MM)
* *state* - State where shopping point occurred
* *location* - Location ID where shopping point occurred
* *group_size* - How many people will be covered under the policy (1, 2, 3 or 4)
* *homeowner* - Whether the customer owns a home or not (0=no, 1=yes)
* *car_age* - Age of the customer’s car
* *car_value* - How valuable was the customer’s car when new
* *risk_factor* - An ordinal assessment of how risky the customer is (1, 2, 3, 4)
* *age_oldest* - Age of the oldest person in customer's group
* *age_youngest* - Age of the youngest person in customer’s group
* *married_couple* - Does the customer group contain a married couple (0=no, 1=yes)
* *C_previous* - What the customer formerly had or currently has for product option C (0=nothing, 1, 2, 3,4)
* *duration_previous* -  how long (in years) the customer was covered by their previous issuer

* *A,B,C,D,E,F,G* - the coverage options

* *cost* - cost of the quoted coverage options


Less steps
------------

* reduce the steps, simplify data

userX
    from: 0011001 1133121 1133121 1133121 1133121 1133121 1133121 1133121
    to: 0011001 1133121

userY
    from: 0011001 2032021 2032021 2032021 2032021 2032021 2032021 2032021 2032021
    to: 0011001 2032021 
