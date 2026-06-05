# Celery Task Execution

## Description
This code demonstrates how to execute a Celery task asynchronously using `.delay()`.

## What This Code Does
- Imports a Celery task from `addTask.py`  
- Calls the task asynchronously using `delay()`  
- Passes two numbers as arguments (`5` and `5`)  
- Returns a task result object immediately without waiting for execution  

## Execution Flow
1. Import `addTask` module  
2. Call `add.delay(5, 5)`  
3. Celery sends task to the message broker  
4. Worker receives and executes task  
5. Result is stored in the backend  
6. Main program continues without waiting  

## How to Execute
1. Start Redis/RabbitMQ broker  
2. Start Celery worker:
   ```bash
   celery -A addTask worker --loglevel=info
   ```
3. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Background task processing  
- Distributed task execution  
- Asynchronous workloads  

## When to Use
Use when:
- Tasks take a long time to complete  
- Work should run in the background  
- Distributed processing is needed  

Avoid when:
- Immediate results are required  
- Tasks are very small and simple  

## How to Use
1. Define a Celery task  
2. Start a message broker  
3. Start Celery worker  
4. Call task using `.delay()`  
5. Retrieve result if needed  

## Advantages
- Asynchronous execution  
- Scalable and distributed  
- Improves application responsiveness  

## Disadvantages
- Requires broker setup  
- More complex architecture  
- Additional system resources needed  

## One-Line Summary
This program sends a Celery task to execute asynchronously in the background.
