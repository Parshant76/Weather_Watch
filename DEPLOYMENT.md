# How to Deploy & Run Weather Watch 🚀

Since this is a **Command Line Interface (CLI)** application, it runs in a terminal, not a web browser. "Deploying" usually means giving others the ability to run it.

Here are the two best ways to share your project for MLH Global Week.

---

## Option 1: Run Locally (Best for Judges/Developers)
This is the standard way to share Python code. Anyone with Python installed can run this.

**Instructions for others:**
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Parshant76/Weather_Watch.git
    cd Weather_Watch
    ```
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Setup API Key**:
    *   Create a file named `config.py` in the project folder.
    *   Add this line:
        ```python
        API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
        ```
4.  **Run**:
    ```bash
    python main.py
    ```

---

## Option 2: Run on Replit (Best for Shareable Links)
[Replit](https://replit.com/) allows you to run Python code in the browser.

1.  Create a new account on [Replit](https://replit.com/).
2.  Click **"Create Repl"** -> **"Import from GitHub"**.
3.  Paste your repo URL: `https://github.com/Parshant76/Weather_Watch.git`.
4.  **Important Security Step**:
    *   Since `config.py` is hidden (Ignored by Git), you must recreate it in Replit.
    *   Or, use Replit **Secrets** (Environment Variables) to store your `API_KEY`.
5.  Click **Run**.
6.  Share the Replit link!

---

## How to Verify It's Working
1.  Run the script: `python main.py`
2.  Enter a known city (e.g., `London`, `Tokyo`).
3.  Check if the output matches reality (Google "Weather in London").
4.  Try an invalid city (e.g., `Atlantis`) to verify error handling.
