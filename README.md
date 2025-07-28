### 🚀 The Soul of the Project: WhatsApp Profile Picture Automation

Tired of having the same old face on social media? Every day brings a new mood, new energy, a new "you." So why shouldn't your digital reflection keep up?

This automation steps in precisely at this point. This smart system we've designed for you:

  * **Dynamic Identity 🎨:** Selects a random photo from your defined image collection every 24 hours and sets it as your WhatsApp profile picture. A fresh start for every day\!
  * **Full Automation ⏰:** Set it up once, and forget about it. The program quietly works in the background while you go about your life. Say goodbye to the hassle of manually changing your profile picture. We call this "smart laziness."
  * **Infinite Personalization ✨:** The collection is entirely yours. Whether it's your favorite movie characters, nature landscapes, or your own drawings... You define your style, and the technology handles the rest.

This project pushes the boundaries of web automation using the power of **Selenium** and saves you time. Because our most valuable resource is time, and we'll never let you waste it.

-----

### 🛠️ Setup and Running Guide: Step-by-Step to Mars... I Mean, WhatsApp\!

Bringing our project to life isn't rocket science. Just follow the steps below and watch the magic unfold\!

**1. Requirements ✅**
First, you need two things installed on your computer:

  * **Python:** If it's not installed, you can download it from [python.org](https://www.python.org/downloads/).
  * **Google Chrome:** The automation runs through the Chrome browser.

**2. Download Project Files 📂**

  * Go to the [GitHub project page](https://github.com/omeraslandev/whatsapp-pfp-automation).
  * Click the green **"\<\> Code"** button and select **"Download ZIP"** to download all files to your computer.
  * Extract the downloaded ZIP file into a folder.

**3. Prepare Your Images 🖼️**

  * Inside the project folder, create a new folder named **`images`**.
  * Place all the images you want to use as profile pictures into this folder.
  * **VERY IMPORTANT:** You must number your photos as `1.jpg`, `2.jpg`, `3.jpg`... and so on. The current code randomly selects from photos numbered 1 to 48. If you have fewer or more photos, you need to change the `48` in the line `pfp = random.randint(1, 48)` in the `main.py` file to your actual number of photos.

**4. Install the Necessary Library 📦**
We need to install Selenium, the brain of the automation. Open your Command Prompt (CMD) or Terminal and type the following command, then press Enter:

```bash
pip install selenium
```

**5. Set Up the Driver (ChromeDriver) 🚗**
This is the bridge that allows the automation to control your browser.

  * First, find your Chrome browser's version. In Chrome, go to `Settings > About Chrome` to find your version number (e.g., `127.0.6533.72`).
  * Go to the [ChromeDriver download page](https://googlechromelabs.github.io/chrome-for-testing/).
  * Find the **most suitable** ChromeDriver for your browser version and download the `chromedriver-win64.zip` file.
  * Extract the `chromedriver.exe` file from the downloaded ZIP and place it inside the `chromedriver-win64` folder within your project's main folder (`whatsapp-pfp-automation`). The code path is set there\!

**6. Fire Up the Automation\! ▶️**
Everything's ready\! Now it's time to start the engines.

  * Open Command Prompt (CMD) or Terminal in the project's main folder.
  * Type the following command and press Enter to start the script:
    ```bash
    python main.py
    ```
  * The script will automatically open a Chrome window and navigate to `web.whatsapp.com`.
  * Scan the **QR code** with your phone to log in to WhatsApp Web.
  * After logging in, return to the terminal screen where you ran the script and type `yes` to the question **"Did you login? (yes/no):"**, then press Enter.

That's it\! Sit back and watch the script change your first profile picture. From now on, it will repeat this process for you every 24 hours. Your digital identity is now more vibrant than ever\! 😉
