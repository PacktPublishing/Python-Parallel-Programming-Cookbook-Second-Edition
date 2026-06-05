# Creating a Celery Task

## Description
This code demonstrates how to create a simple Celery task that performs addition asynchronously.

## What This Code Does
- Creates a Celery application  
- Connects to RabbitMQ using a broker URL  
- Defines a task named `add()`  
- Accepts two numbers as input  
- Returns the sum of the numbers  

## Execution Flow
1. Import `Celery`  
2. Create Celery application instance  
3. Connect to RabbitMQ broker  
4. Define task using `@app.task` decorator  
5. Task waits for execution requests  
6. Worker executes task when called  

## How to Execute
1. Install Celery:
   ```bash
   pip install celery
   ```

2. Install and start RabbitMQ

3. Start Celery worker:
   ```bash
   celery -A addTask worker --loglevel=info
   ```

4. Run task from another Python file:
   ```python
   import addTask
   result = addTask.add.delay(5, 5)
   ```

## End Use
Used for:
- Background processing  
- Distributed task execution  
- Asynchronous operations  

## When to Use
Use when:
- Tasks take time to execute  
- Background processing is needed  
- Workload should be distributed  

Avoid when:
- Immediate results are required  
- Simple synchronous execution is enough  

## How to Use
1. Create Celery app  
2. Configure broker connection  
3. Define task with `@app.task`  
4. Start worker process  
5. Call task using `.delay()` or `.apply_async()`  

## Advantages
- Asynchronous task execution  
- Scalable architecture  
- Supports distributed workers  

## Disadvantages
- Requires RabbitMQ or Redis  
- Additional setup and configuration  
- More complex than normal functions  

## One-Line Summary
This code creates a Celery task that adds two numbers and can be executed asynchronously by a worker.
