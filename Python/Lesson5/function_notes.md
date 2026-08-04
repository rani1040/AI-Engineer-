# Functions in Python - Notes

## 1. What is a Function?

* A function is a reusable block of code that performs a specific task.
* Functions help avoid repeating the same code multiple times.
* A function executes only when it is called.

---

# 2. Function Declaration

* Function declaration means creating a function.
* It defines:

  * Function name
  * Parameters
  * Instructions that the function will perform

### Syntax Structure:

**def → function keyword**
**Function name → identifies the function**
**Parameters → values the function receives**
**Function body → instructions to execute**

---

# 3. Function Calling

* Function calling means executing a function.
* When a function is called:

  1. Python creates a new execution space.
  2. Required values are passed.
  3. Function instructions are executed.
  4. Execution space is removed after completion.

---

# 4. How Functions Work in Memory

### Step 1: Function Declaration

* When Python reads a function declaration:

  * It creates a function object in memory.
  * The function code is stored.
  * The code is not executed immediately.

### Step 2: Function Call

* When the function is called:

  * A new function execution space is created.
  * Parameters receive values.
  * Function body executes.

### Step 3: Function Completion

* After execution:

  * Returned value is sent back (if available).
  * Function memory is removed.

---

# 5. Parameters

* Parameters are variables written while creating a function.
* They act as placeholders for values.
* Parameters receive values when the function is called.

Example concept:

Function expects a value → Parameter receives that value.

---

# 6. Arguments

* Arguments are actual values passed during a function call.
* They provide data to the parameters.

### Difference:

**Parameter**

* Present during function creation.
* Receives values.

**Argument**

* Present during function calling.
* Provides values.

---

# 7. Types of Arguments

## Positional Arguments

* Values are assigned according to their position.
* Order matters.

## Keyword Arguments

* Values are assigned using parameter names.
* Order does not matter.

## Default Arguments

* A parameter already has a default value.
* If no value is provided, the default value is used.

---

# 8. Return Statement

* The return statement sends a value back from a function.
* It allows the result of a function to be stored and used later.
* After return executes, the function stops immediately.

---

# 9. Print vs Return

## Print

* Only displays output.
* Does not send a value back.
* Cannot be reused for further calculations.

## Return

* Sends a value back to the caller.
* The returned value can be stored.
* Used when we need a result from a function.

---

# 10. Function Without Return

* A function performs an action but does not give back a result.
* It is mainly used for displaying or performing tasks.

---

# 11. Function With Return

* A function calculates something and sends the result back.
* The returned value can be stored or used in another operation.

---

# 12. Multiple Return Values

* A function can return more than one value.
* Multiple results can be received separately.

---

# 13. Recursion

* Recursion is when a function calls itself.
* It solves a problem by breaking it into smaller versions of the same problem.

---

# 14. Parts of Recursion

## Base Condition

* The stopping condition of recursion.
* Prevents the function from calling itself forever.

## Recursive Call

* The function calls itself.
* Each call should move closer to the base condition.

---

# 15. Recursion Memory Flow

* Every recursive call creates a new function execution space.
* Each call is stored in memory (call stack).
* When the base condition is reached:

  * Calls start returning one by one.
  * Memory is released in reverse order.

---

# 16. Function Execution Flow

1. Function is declared.
2. Function is stored in memory.
3. Function is called.
4. Arguments are passed.
5. Parameters receive values.
6. Function executes.
7. Return value is produced (if any).
8. Function memory is removed.

---

# Quick Revision

| Concept        | Meaning                            |
| -------------- | ---------------------------------- |
| Function       | Reusable block of code             |
| Declaration    | Creating a function                |
| Calling        | Executing a function               |
| Parameter      | Variable that receives value       |
| Argument       | Value passed to function           |
| Return         | Sends value back                   |
| Recursion      | Function calling itself            |
| Base Condition | Stops recursion                    |
| Call Stack     | Memory area storing function calls |
