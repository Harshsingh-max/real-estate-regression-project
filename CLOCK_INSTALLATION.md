# Digital Clock Installation Guide

## Quick Start (2 minutes)

### Option 1: Web Version (Recommended - Easiest)

1. **Download the file**
   ```bash
   git clone https://github.com/Harshsingh-max/real-estate-regression-project.git
   cd real-estate-regression-project
   ```

2. **Open in browser**
   - Windows: Double-click `digital_clock.html`
   - Mac: Right-click → Open with → Your Browser
   - Linux: Open with your browser

3. **Done!** Clock is now running

### Option 2: Python Desktop Version

1. **Install Python** (if not already installed)
   - Download from https://www.python.org/downloads/
   - Choose Python 3.7 or higher

2. **Install Dependencies**
   ```bash
   pip install pytz
   ```

3. **Run the application**
   ```bash
   python digital_clock.py
   ```

## Detailed Installation

### Windows

**For Web Version:**
1. Download `digital_clock.html`
2. Right-click the file
3. Select "Open with" → "Google Chrome" (or your browser)

**For Python Version:**
1. Install Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Open Command Prompt (Win+R, type `cmd`)
4. Run:
   ```bash
   pip install pytz
   python digital_clock.py
   ```

### macOS

**For Web Version:**
1. Download `digital_clock.html`
2. Double-click the file (opens in default browser)
3. Or right-click → Open with → Select your browser

**For Python Version:**
1. Python 3 is pre-installed on newer Macs
2. Open Terminal (Cmd+Space, type `terminal`)
3. Run:
   ```bash
   pip3 install pytz
   python3 digital_clock.py
   ```

### Linux

**For Web Version:**
1. Download `digital_clock.html`
2. Right-click → Open with → Your browser

**For Python Version:**
1. Open Terminal
2. Run:
   ```bash
   sudo apt-get install python3 python3-pip
   pip3 install pytz
   python3 digital_clock.py
   ```

## Verification

### Check Python Installation

```bash
python --version
# or
python3 --version
```

You should see: `Python 3.x.x`

### Check pytz Installation

```bash
python -c "import pytz; print('pytz installed!')"
```

You should see: `pytz installed!`

## Run with Web Server (Optional)

For better performance, serve the web version with a local server:

**Python 3 (Built-in)**
```bash
python -m http.server 8000
```

**Python 2 (Legacy)**
```bash
python -m SimpleHTTPServer 8000
```

**Node.js (if installed)**
```bash
npx http-server
```

Then visit: `http://localhost:8000/digital_clock.html`

## Troubleshooting

### "ModuleNotFoundError: No module named 'pytz'"

**Solution:**
```bash
pip install --upgrade pytz
```

### "Python not found" or "python: command not found"

**Solution:**
1. Reinstall Python from https://www.python.org/downloads/
2. Make sure "Add Python to PATH" is checked
3. Restart your computer

### "Permission denied" (Linux/Mac)

**Solution:**
```bash
chmod +x digital_clock.py
python digital_clock.py
```

### Web version shows blank page

**Solution:**
1. Clear browser cache (Ctrl+Shift+Delete)
2. Check browser console for errors (F12)
3. Try a different browser
4. Enable JavaScript in browser settings

### Clocks show wrong time

**Solution:**
1. Check your system time is correct
2. Check your timezone setting
3. For web version: Clear cookies (Settings → Clear browsing data)

## System Requirements

### Python Version
- **Minimum**: Python 3.7
- **Recommended**: Python 3.9 or higher
- **Check version**: `python --version`

### Hardware Requirements
- **RAM**: 256 MB minimum (both versions)
- **Disk Space**: 50 MB (Python version with dependencies)
- **Display**: 800×600 minimum resolution

### Browser Requirements (Web Version)
- **Minimum**: Any browser from 2015+
- **Recommended**: Chrome, Firefox, Safari, or Edge (latest)
- **JavaScript**: Must be enabled
- **Canvas**: Must be supported

## Performance Tips

### Python Version
1. Close other applications to free memory
2. Use a modern computer for best performance
3. Don't run multiple instances simultaneously

### Web Version
1. Use Chrome or Firefox for best performance
2. Close unnecessary browser tabs
3. Disable browser extensions if experiencing lag
4. Use hardware acceleration (if available)

## Updating

### Get Latest Version

```bash
cd real-estate-regression-project
git pull origin main
```

### Update Dependencies (Python)

```bash
pip install --upgrade pytz
```

## Uninstallation

### Remove Python Package

```bash
pip uninstall pytz
```

### Remove Cloned Repository

```bash
rm -rf real-estate-regression-project  # Linux/Mac
rmdir /s real-estate-regression-project  # Windows
```

## Next Steps

1. ✅ Application is installed
2. ✅ Clock is running
3. 📖 Read `DIGITAL_CLOCK_README.md` for features
4. 🎨 Customize colors and timezones (optional)
5. 🚀 Share with friends!

## Getting Help

- **Official Repository**: https://github.com/Harshsingh-max/real-estate-regression-project
- **Report Issues**: Open GitHub issue
- **Documentation**: See README files
- **Contact**: Open issue on GitHub

---

**Installation Version**: 1.0
**Last Updated**: June 15, 2026
