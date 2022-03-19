# API to run python code
An api that anyone can call to execute python code. 

## Why? 
There are quite a few usecases, where you need to run a user's code (online coding classes, no-code apps with custom user inputs, ...) and you might not want to implement this yourself.

## How
**Call the following endpoint with your code in the JSON body**

**POST**: `https://api-run-code.herokuapp.com/execute`

**JSON body:** `{'code': 'my_value = 55*100'}`

You will receive the final value of all the declared variables in response. 

**JSON response:** `{'my_value': 5500}`


## Examples
*coming soon*
