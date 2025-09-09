# CPU Monitor

## Overview

A Python-based CPU monitoring utility that provides real-time temperature and usage statistics. The application uses system sensors to track CPU temperature and performance metrics, displaying the information in a user-friendly format with visual indicators for temperature levels.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

**Core Application Structure**
The system follows a simple single-file architecture pattern with modular functions for different monitoring capabilities. The main application is built around Python's `psutil` library for system monitoring.

**Temperature Monitoring System**
The temperature detection uses a multi-layered fallback approach:
1. Primary: Searches for CPU-specific sensors using keyword matching
2. Fallback: Uses the first available temperature sensor if no CPU sensor is found
3. Error handling: Gracefully handles cases where temperature sensors are unavailable

**Data Collection Pattern**
The application implements a polling-based monitoring system that collects CPU usage with a 1-second interval to provide accurate readings while avoiding excessive system load.

**User Interface Design**
The output uses a console-based display with:
- Timestamped readings for tracking
- Visual warmth indicators using emoji symbols
- Temperature categorization (Cool 🟢, Warm 🟡, Hot 🔴)
- Formatted output with separators for readability

**Error Handling Strategy**
The system implements defensive programming with try-catch blocks around sensor operations and graceful degradation when hardware sensors are not available.

## External Dependencies

**System Libraries**
- `psutil`: Cross-platform system and process utilities for CPU monitoring and temperature sensors
- `time`: Built-in Python module for timing operations and intervals
- `sys`: Built-in Python module for system-specific parameters
- `datetime`: Built-in Python module for timestamp formatting

**Hardware Dependencies**
- CPU temperature sensors (platform-dependent)
- System performance counters for CPU usage statistics