# 🌡️ Temperature Monitoring & Alert System

**Name:** Rajat Gupta
**Roll No:** 202501100700114
**Branch:** ECE-B

---

## 📌 Problem Statement

In environments like industrial plants, server rooms, laboratories, and weather stations, maintaining temperature within a safe range is critical. Continuous monitoring helps prevent system failures, equipment damage, and safety hazards.

This project simulates a **Temperature Monitoring System** that:

* Accepts minimum and maximum temperature limits from the user.
* Continuously generates random temperature readings (simulating a sensor).
* Compares readings against defined limits.
* Displays alerts if temperature goes beyond the safe range.

The program runs continuously to imitate real-time temperature tracking.

---

## ⚙️ How the Program Works

1. The user enters:

   * Minimum temperature limit
   * Maximum temperature limit

2. The system:

   * Generates a random temperature between **0°C and 100°C**.
   * Displays the temperature.
   * Compares it with user-defined limits.

3. Based on comparison:

   * If temperature > maximum limit → **Alert: Temperature is too high**
   * If temperature < minimum limit → **Alert: Temperature is too low**
   * If temperature is within range → **Temperature is within acceptable limit**

4. The program runs in an infinite loop (`while True`) to simulate continuous monitoring.

---

## 🛠️ Technologies Used

* Python 3.x
* `random` module (for generating temperature values)
* `time` module (for delay simulation)

---

## ▶️ How to Run the Program

### Step 1: Install Python

Make sure Python 3.x is installed.

Check installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

### Step 2: Save the Program

Save the file as:

```
temperature_monitor.py
```

---

### Step 3: Run the Program

Open terminal/command prompt in the file directory and run:

```bash
python temperature_monitor.py
```

or

```bash
python3 temperature_monitor.py
```

---

### Step 4: Enter Input

When prompted, enter minimum and maximum temperature separated by space:

```
Enter the min and max limits of temprature respectively: 20 35
```

---

## ⛔ How to Stop the Program

Since the program runs continuously, press:

```
CTRL + C
```

to terminate execution.

---

## ✨ Features

* Simulates real-time temperature monitoring
* High and low temperature alerts
* Animated alert messages
* Continuous execution
* Simple and easy-to-understand logic

---

## ⚠️ Note

* This program uses randomly generated values.
* It does not connect to a real temperature sensor.
* It is built for educational and simulation purposes.

---

## 🚀 Future Enhancements

* Integration with real temperature sensors (IoT)
* Store temperature logs in a file
* Add GUI interface
* Add sound alerts
* Add user menu with exit option

---
