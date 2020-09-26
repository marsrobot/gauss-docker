# Table of Contents
- [Introduction](#introduction)
- [Run](#Run)

# Introduction
Calculate Gaussian sum 
- 1 + 2 + ... + 1000 = 500500,
- 1 + 2 + ... + 999  = 499500 by docker

# Run
Step 1: Fire up service
docker-compose up --build -d --scale app=8

Step 2: Run test
python test/run.py
Result:
sum: 500500

Step 3: Clean up
docker-compose down
