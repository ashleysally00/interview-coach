# Confidence Quiz - Setup Instructions

## Files Needed
- `testing_confidence_quiz.py`
- `test2.py`

## Setup Steps
1. Create a new folder on your computer called "confidence-quiz"
2. Open VSCode
3. Open the "confidence-quiz" folder in VSCode
4. Create two new files with these exact names:
   - `testing_confidence_quiz.py`
   - `test2.py`
5. Copy the code I sent you into each file

## Setting up Python Environment
6. Open VSCode's terminal (View -> Terminal)
7. Create a virtual environment by typing:
   ```bash
   python -m venv venv
   ```
   Note: If this doesn't work, try:
   ```bash
   python3 -m venv venv
   ```
8. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
   You should see (venv) appear at the start of your terminal line

## Running the Quiz
9. Make sure you're in the right folder (you should see testing_confidence_quiz in the terminal path)
10. Type: `python test2.py`
    Note: If this doesn't work, try:
    ```bash
    python3 test2.py
    ```
11. Follow the prompts to take the quiz!

## Requirements
- Python 3 must be installed on your computer
- VSCode or similar code editor

## Troubleshooting
If you get an error:
1. Make sure both files are in the same folder
2. Double-check that the files are named exactly:
   - `testing_confidence_quiz.py`
   - `test2.py`
3. Verify you're in the correct folder in the terminal
4. Make sure you see (venv) at the start of your terminal line
5. If commands with `python` don't work, try using `python3` instead
6. Check your Python installation by typing:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

## Deactivating the Environment
When you're done, you can deactivate the virtual environment by typing:
```bash
deactivate
```

## First Time Setup on Mac
If you've never used Python in your terminal before:
1. You might need to install Command Line Tools. If prompted, allow the installation
2. You might need to use `python3` explicitly instead of `python`
3. If Python isn't installed, you can download it from python.org or install via Homebrew:
   ```bash
   brew install python3
   ```

## File Structure
Your folder should look like this:
```
confidence-quiz/
├── testing_confidence_quiz.py
├── test2.py
└── venv/
```