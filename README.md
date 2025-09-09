# CPU Warmth Monitor 🌡️

A Python-based CPU monitoring utility that provides real-time temperature and usage statistics. The application continuously tracks your computer's CPU performance and displays the information in a user-friendly format with visual indicators.

## What It Does

The CPU Warmth Monitor continuously watches your computer's CPU (the main processing chip) and reports two key metrics:

- **Temperature** - How hot the CPU is getting (in Celsius)
- **Usage** - How hard the CPU is working (as a percentage)

## Features

### Real-Time Monitoring
- Updates every 5 seconds automatically
- Timestamped readings for tracking performance over time
- Continuous monitoring until manually stopped

### Visual Indicators
The monitor uses color-coded emoji indicators for easy understanding:

**Temperature Levels:**
- 🟢 **Cool** (under 40°C) - CPU running at safe, low temperatures
- 🟡 **Warm** (40-60°C) - Normal operating temperature range
- 🟠 **Hot** (60-80°C) - Higher temperatures, monitor for sustained periods
- 🔴 **Very Hot** (over 80°C) - High temperatures that may need attention

**Usage Levels:**
- **Low** (0-20%) - Light system load
- **Moderate** (20-50%) - Normal everyday usage
- **High** (50-80%) - Heavy processing tasks
- **Very High** (80-100%) - Maximum system utilization

### Smart Temperature Detection
The system uses a multi-layered approach to find temperature sensors:
1. **Primary**: Searches for CPU-specific sensors using keyword matching ("CPU", "Core", "Processor")
2. **Fallback**: Uses the first available temperature sensor if no CPU sensor is found
3. **Graceful Handling**: Shows "Not available" when temperature sensors can't be accessed

## How to Use

### Running the Monitor
The monitor is set up to run automatically in the background. You'll see live updates in the console showing:

```
[13:08:31] CPU Status:
========================================
Temperature: 45.2°C (Warm 🟡)
CPU Usage: 68.2%
Usage Level: High
========================================
```

### Stopping the Monitor
To stop the monitor, you can restart the workflow or interrupt the process.

## Technical Details

### How It Was Built

**Step 1: Foundation Setup**
- Installed Python 3.11 as the programming language
- Added `psutil` library for system hardware monitoring capabilities

**Step 2: Core Architecture**
Created a single-file application (`cpu_monitor.py`) with modular functions:
- `get_cpu_temperature()` - Reads temperature sensors from system hardware
- `get_cpu_usage()` - Measures CPU utilization with 1-second sampling
- `display_cpu_warmth()` - Formats and presents data in user-friendly format
- `main()` - Runs the continuous monitoring loop

**Step 3: Smart Sensor Detection**
Implemented intelligent temperature sensor discovery:
```python
# Searches for CPU-specific sensors first
if any(keyword in name.lower() for keyword in ['cpu', 'core', 'proc']):
    # Use CPU-specific sensor data
    
# Falls back to any available temperature sensor
# Handles cases where sensors aren't accessible
```

**Step 4: User Experience Design**
- Clean, readable output with consistent formatting
- Emoji indicators for quick visual understanding
- Descriptive categories instead of raw numbers
- Error handling that doesn't break the user experience

**Step 5: Automation Setup**
Configured as a background workflow that starts automatically and provides continuous monitoring.

### Dependencies

**Python Libraries:**
- `psutil` (v7.0.0) - Cross-platform system and process utilities
- `time` - Built-in Python module for timing operations
- `sys` - Built-in Python module for system parameters
- `datetime` - Built-in Python module for timestamp formatting

**System Requirements:**
- Python 3.11+
- Access to system performance counters
- Optional: CPU temperature sensors (platform-dependent)

### File Structure
```
.
├── cpu_monitor.py    # Main monitoring application
├── README.md         # This documentation file
├── replit.md         # Project configuration and preferences
└── pyproject.toml    # Python project dependencies
```

## Why Temperature Might Show "Not Available"

In some environments, you might see "Temperature: Not available on this system". This happens because:

1. **Virtualized Environments** - Cloud servers and virtual machines often don't expose temperature sensors for security reasons
2. **Hardware Limitations** - Some systems don't have accessible temperature monitoring hardware
3. **Security Restrictions** - Operating system policies might block access to low-level hardware sensors

**Note:** Even without temperature readings, CPU usage monitoring still provides valuable insights into your system's performance!

## Understanding the Output

### Sample Reading Breakdown
```
[13:08:31] CPU Status:           # Timestamp of the reading
========================================
Temperature: 45.2°C (Warm 🟡)   # Temperature with visual indicator
CPU Usage: 68.2%                # Percentage of CPU being used
Usage Level: High                # Descriptive usage category
========================================
```

### What Different Usage Levels Mean
- **Low (0-20%)**: System is mostly idle, running basic background processes
- **Moderate (20-50%)**: Normal web browsing, document editing, light multitasking
- **High (50-80%)**: Video calls, photo editing, compiling code, gaming
- **Very High (80-100%)**: Intensive tasks like video rendering, large file compression, or running multiple demanding applications

## Troubleshooting

**Monitor Not Starting:**
- Check that Python is properly installed
- Verify `psutil` library is available
- Restart the workflow if needed

**High CPU Usage Consistently:**
- Check for background applications using system resources
- Consider closing unnecessary programs
- Monitor for runaway processes

**No Temperature Data:**
- This is normal in many virtualized environments
- CPU usage data will still be accurate and useful
- Physical machines typically have better sensor access

---

*Built with Python and love for system monitoring! 🐍❤️*