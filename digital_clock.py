import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz
from pytz import timezone
import threading

class DigitalClock:
    """
    Digital Clock displaying current time in multiple time zones
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("1000x600")
        self.root.configure(bg="#1a1a1a")
        
        # Define time zones to display
        self.timezones = {
            'UTC': 'UTC',
            'New York': 'America/New_York',
            'London': 'Europe/London',
            'Tokyo': 'Asia/Tokyo',
            'Sydney': 'Australia/Sydney',
            'Dubai': 'Asia/Dubai',
            'Singapore': 'Asia/Singapore',
            'Hong Kong': 'Asia/Hong_Kong',
            'India': 'Asia/Kolkata',
            'Los Angeles': 'America/Los_Angeles',
            'Chicago': 'America/Chicago',
            'Mexico City': 'America/Mexico_City',
        }
        
        # Font definitions
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.clock_font = font.Font(family="Courier New", size=32, weight="bold")
        self.timezone_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.info_font = font.Font(family="Helvetica", size=10)
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create title
        self.title_label = tk.Label(
            self.main_frame,
            text="🕐 WORLD TIME CLOCK",
            font=self.title_font,
            fg="#00FF00",
            bg="#1a1a1a"
        )
        self.title_label.pack(pady=10)
        
        # Create clock frames container
        self.clocks_frame = tk.Frame(self.main_frame, bg="#1a1a1a")
        self.clocks_frame.pack(fill=tk.BOTH, expand=True)
        
        # Dictionary to store clock labels
        self.clock_labels = {}
        self.date_labels = {}
        self.offset_labels = {}
        
        # Create a grid of clocks
        self.create_clock_grid()
        
        # Create status bar
        self.status_frame = tk.Frame(self.root, bg="#2a2a2a", height=40)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Last updated: --:--:--",
            font=self.info_font,
            fg="#00FF00",
            bg="#2a2a2a"
        )
        self.status_label.pack(pady=8)
        
        # Start clock update thread
        self.update_clock()
    
    def create_clock_grid(self):
        """Create a grid layout for all timezone clocks"""
        
        # Create frames for each timezone (3 columns, 4 rows)
        col = 0
        row = 0
        
        for city, tz in self.timezones.items():
            # Create a frame for each timezone clock
            clock_frame = tk.Frame(
                self.clocks_frame,
                bg="#2a2a2a",
                relief=tk.RAISED,
                borderwidth=2
            )
            clock_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # City name label
            city_label = tk.Label(
                clock_frame,
                text=city,
                font=self.timezone_font,
                fg="#00FF00",
                bg="#2a2a2a"
            )
            city_label.pack(pady=5, padx=5)
            
            # Time display label
            time_label = tk.Label(
                clock_frame,
                text="--:--:--",
                font=self.clock_font,
                fg="#FF00FF",
                bg="#2a2a2a",
                family="Courier New"
            )
            time_label.pack(pady=5, padx=5)
            self.clock_labels[city] = time_label
            
            # Date label
            date_label = tk.Label(
                clock_frame,
                text="----/--/--",
                font=self.info_font,
                fg="#00FFFF",
                bg="#2a2a2a"
            )
            date_label.pack(pady=2, padx=5)
            self.date_labels[city] = date_label
            
            # UTC Offset label
            offset_label = tk.Label(
                clock_frame,
                text="UTC+0",
                font=self.info_font,
                fg="#FFFF00",
                bg="#2a2a2a"
            )
            offset_label.pack(pady=2, padx=5)
            self.offset_labels[city] = offset_label
            
            # Update grid weights
            self.clocks_frame.grid_rowconfigure(row, weight=1)
            self.clocks_frame.grid_columnconfigure(col, weight=1)
            
            # Move to next position
            col += 1
            if col >= 3:
                col = 0
                row += 1
    
    def get_utc_offset(self, tz_name):
        """Calculate UTC offset for a timezone"""
        try:
            tz = timezone(tz_name)
            now = datetime.now(tz)
            offset = now.strftime('%z')
            # Format offset as +HH:MM or -HH:MM
            if offset:
                return f"UTC{offset[:3]}:{offset[3:]}"
            return "UTC+0"
        except:
            return "UTC+0"
    
    def update_clock(self):
        """Update all clock displays"""
        for city, tz_name in self.timezones.items():
            try:
                # Get current time in timezone
                tz = timezone(tz_name)
                current_time = datetime.now(tz)
                
                # Format time as HH:MM:SS
                time_string = current_time.strftime("%H:%M:%S")
                
                # Format date as YYYY/MM/DD
                date_string = current_time.strftime("%Y/%m/%d")
                
                # Get UTC offset
                offset_string = self.get_utc_offset(tz_name)
                
                # Update labels
                self.clock_labels[city].config(text=time_string)
                self.date_labels[city].config(text=date_string)
                self.offset_labels[city].config(text=offset_string)
                
            except Exception as e:
                self.clock_labels[city].config(text="ERROR")
                print(f"Error updating {city}: {e}")
        
        # Update status bar
        current_update_time = datetime.now().strftime("%H:%M:%S")
        self.status_label.config(text=f"Last updated: {current_update_time}")
        
        # Schedule next update in 1000ms (1 second)
        self.root.after(1000, self.update_clock)


class AnalogClockWidget(tk.Canvas):
    """Analog clock widget for additional display"""
    
    def __init__(self, parent, timezone_name, **kwargs):
        super().__init__(parent, **kwargs)
        self.timezone_name = timezone_name
        self.tz = timezone(timezone_name)
        
    def draw_clock(self):
        """Draw analog clock face and hands"""
        w = self.winfo_width()
        h = self.winfo_height()
        
        if w < 2 or h < 2:
            return
        
        # Clear canvas
        self.delete("all")
        
        # Calculate center and radius
        center_x = w / 2
        center_y = h / 2
        radius = min(w, h) / 2 - 10
        
        # Draw clock face
        self.create_oval(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            fill="#2a2a2a",
            outline="#00FF00",
            width=2
        )
        
        # Draw hour markers
        for i in range(12):
            angle = i * 30 - 90
            x1 = center_x + (radius - 10) * (3.14159 * angle / 180)
            y1 = center_y + (radius - 10) * (3.14159 * angle / 180)
            
        # Get current time
        now = datetime.now(self.tz)
        hours = now.hour % 12
        minutes = now.minute
        seconds = now.second
        
        # Draw hour hand
        hour_angle = (hours * 30 + minutes * 0.5 - 90) * 3.14159 / 180
        hour_x = center_x + (radius * 0.5) * (3.14159 * hour_angle / 180)
        hour_y = center_y + (radius * 0.5) * (3.14159 * hour_angle / 180)
        self.create_line(center_x, center_y, hour_x, hour_y, fill="#FF00FF", width=4)
        
        # Draw minute hand
        minute_angle = (minutes * 6 + seconds * 0.1 - 90) * 3.14159 / 180
        minute_x = center_x + (radius * 0.7) * (3.14159 * minute_angle / 180)
        minute_y = center_y + (radius * 0.7) * (3.14159 * minute_angle / 180)
        self.create_line(center_x, center_y, minute_x, minute_y, fill="#00FFFF", width=3)
        
        # Draw second hand
        second_angle = (seconds * 6 - 90) * 3.14159 / 180
        second_x = center_x + (radius * 0.8) * (3.14159 * second_angle / 180)
        second_y = center_y + (radius * 0.8) * (3.14159 * second_angle / 180)
        self.create_line(center_x, center_y, second_x, second_y, fill="#FFFF00", width=1)
        
        # Draw center dot
        dot_size = 5
        self.create_oval(
            center_x - dot_size,
            center_y - dot_size,
            center_x + dot_size,
            center_y + dot_size,
            fill="#00FF00"
        )


def main():
    """Main function to run the digital clock application"""
    root = tk.Tk()
    
    # Create the digital clock application
    clock_app = DigitalClock(root)
    
    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()
