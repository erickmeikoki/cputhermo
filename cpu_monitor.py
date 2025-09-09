#!/usr/bin/env python3
import psutil
import time
import sys
from datetime import datetime

def get_cpu_temperature():
    """Get CPU temperature using psutil sensors_temperatures()"""
    try:
        temps = psutil.sensors_temperatures()
        if not temps:
            return None
        
        # Try to find CPU temperature from common sensor names
        for name, entries in temps.items():
            # Look for common CPU sensor names
            if any(keyword in name.lower() for keyword in ['cpu', 'core', 'proc']):
                for entry in entries:
                    if entry.current:
                        return entry.current
        
        # If no CPU-specific sensor found, return the first available temperature
        for name, entries in temps.items():
            for entry in entries:
                if entry.current:
                    return entry.current
    except Exception as e:
        print(f"Error reading temperature: {e}")
    
    return None

def get_cpu_usage():
    """Get current CPU usage percentage"""
    return psutil.cpu_percent(interval=1)

def display_cpu_warmth():
    """Display CPU temperature and usage in a friendly format"""
    temp = get_cpu_temperature()
    cpu_usage = get_cpu_usage()
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    print(f"\n[{timestamp}] CPU Status:")
    print("=" * 40)
    
    if temp is not None:
        # Determine warmth level
        if temp < 40:
            warmth_level = "Cool 🟢"
        elif temp < 60:
            warmth_level = "Warm 🟡"
        elif temp < 80:
            warmth_level = "Hot 🟠"
        else:
            warmth_level = "Very Hot 🔴"
        
        print(f"Temperature: {temp:.1f}°C ({warmth_level})")
    else:
        print("Temperature: Not available on this system")
    
    print(f"CPU Usage: {cpu_usage:.1f}%")
    
    # Show usage level
    if cpu_usage < 20:
        usage_level = "Low"
    elif cpu_usage < 50:
        usage_level = "Moderate"
    elif cpu_usage < 80:
        usage_level = "High"
    else:
        usage_level = "Very High"
    
    print(f"Usage Level: {usage_level}")
    print("=" * 40)

def main():
    """Main monitoring loop"""
    print("🌡️  CPU Warmth Monitor Started")
    print("Press Ctrl+C to stop monitoring\n")
    
    try:
        while True:
            display_cpu_warmth()
            time.sleep(5)  # Update every 5 seconds
    except KeyboardInterrupt:
        print("\n\n🛑 CPU monitoring stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()