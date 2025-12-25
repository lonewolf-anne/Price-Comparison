This project is a Python-based price comparison system built using FastAPI. It was inspired by volunteer work that required manually comparing electronic component prices across multiple shops, which was time-consuming and inefficient. The goal of the project was to automate this process by creating an API that collects shop, item, and price data and determines the shop offering the lowest price for a given item.

The system uses Pydantic models to validate user input and ensure data consistency, while shop and product information is stored in a dictionary to avoid duplication. A comparison algorithm iterates through the stored data to identify the best-priced option. Due to the absence of real APIs from local shops, a fake store API was used to simulate real-world data and demonstrate how the system would function if such APIs were available.

Through this project, I strengthened my understanding of backend development, REST APIs, data validation, and algorithmic problem-solving. I also identified limitations in the current implementation, such as in-memory data storage and early returns in the comparison logic, which I plan to improve in future iterations.

This project was developed with the help of online resources and AI tools for learning and debugging. I ensured full understanding of the logic and implementation.
project report:https://docs.google.com/document/d/1dc73HTdqOI7ViPycGUohF-CG8fKU0Pfti6dqHBdMY7Q/edit?usp=sharing
