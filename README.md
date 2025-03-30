# Setting Up Appium Environment for Python Testing

This guide walks you through setting up an Appium environment for mobile automation testing using Python on macOS.

## Prerequisites
- macOS with **Xcode** installed (for iOS testing)
- **Homebrew** installed (for installing dependencies)
- **Node.js & npm** installed
- **Python 3** installed
- **Java Development Kit (JDK) 17+** installed

## Step 1: Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Step 2: Install Node.js & npm
```bash
brew install node
```
Verify installation:
```bash
node -v
npm -v
```

## Step 3: Install Appium
```bash
npm install -g appium
```
Verify installation:
```bash
appium -v
```

## Step 4: Install Appium Drivers
### For iOS:
```bash
npm install -g appium-xcuitest-driver
```
### For Android:
```bash
npm install -g appium-uiautomator2-driver
```

## Step 5: Install Java & Set JAVA_HOME
```bash
brew install openjdk@11
```
Set JAVA_HOME:
```bash
export JAVA_HOME=$(/usr/libexec/java_home)
export PATH=$JAVA_HOME/bin:$PATH
```
Verify Java installation:
```bash
java -version
```

## Step 6: Install Android SDK & Set Environment Variables
```bash
brew install android-platform-tools
```
Set up environment variables (add to `~/.zshrc` or `~/.bash_profile`):
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$PATH
```
Verify installation:
```bash
sdkmanager --list
```

## Step 7: Install Appium Python Client
```bash
pip install Appium-Python-Client
```

## Step 8: Install Appium Doctor
```bash
npm install -g appium-doctor
```
Run Appium Doctor to check if everything is set up correctly:
```bash
appium-doctor
```

## Step 9: Launch a Simulator (iOS) or Emulator (Android)
### For iOS:
```bash
open -a Simulator
```
### For Android:
```bash
emulator -list-avds  # List available devices
emulator -avd <device_name>  # Start an emulator
```

## Step 10: Start Appium Server
```bash
appium
```

## Step 11: Run Your First Test
Create a file `test_app.py` with the following example:
```python
from appium import webdriver

desired_caps = {
    'platformName': 'iOS',  # Change to 'Android' if testing on Android
    'deviceName': 'iPhone 12',
    'platformVersion': '14.5',
    'app': '/path/to/your/app.app',  # Use .apk for Android
    'automationName': 'XCUITest'  # Use 'UiAutomator2' for Android
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

print("App Launched Successfully!")
driver.quit()
```
Run the test:
```bash
python test_app.py
```

## Conclusion
You now have a working Appium environment for Python testing!

For more details, check out [Appium Documentation](https://appium.io/).

