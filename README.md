# SpecterText

**SpecterText** is a lightweight command-line steganography tool that hides secret messages inside plain text files using invisible Unicode characters.

Unlike traditional steganography tools that use images or audio, SpecterText works directly with **plain text files** and hides data using **zero-width characters**, making the hidden message invisible to normal readers.

The hidden message is stored **inside the same text file** without creating any additional output files.

Made by **Cyber Specterz**

---

# Features

* Hide secret messages inside `.txt` files
* Uses invisible **zero-width Unicode characters**
* No output file required (modifies the same file)
* Extract hidden messages easily
* Lightweight and fast
* No external Python libraries required
* Works on Linux, macOS, and Windows
* Simple CLI interface

---

# How It Works

SpecterText uses special **invisible Unicode characters** to encode binary data.

Character Encoding:

```
Zero Width Space      -> represents binary 0
Zero Width Non Joiner -> represents binary 1
Zero Width Joiner     -> used as delimiter
```

Process:

Embedding

```
Secret Message
      ↓
Convert to Binary
      ↓
Binary → Invisible Characters
      ↓
Append to Text File
```

Extraction

```
Read Text File
      ↓
Detect Invisible Characters
      ↓
Convert to Binary
      ↓
Decode Secret Message
```

The file will look completely normal even after hiding the message.

Example visible text file:

```
Meeting Notes
-------------
Discuss project timeline
Prepare documentation
Finalize deployment
```

Even though the file looks normal, it may contain hidden data.

---

# Requirements

* Python **3.7+**

Check Python version:

```
python3 --version
```

---

# Installation

Clone the repository:

```
git clone https://github.com/Cyber-specterz/SpecterText.git
```

Enter the directory:

```
cd SpecterText
```

Make the script executable (Linux/macOS):

```
chmod +x spectertext.py
```

No additional dependencies are required.

---

# Usage

Show help menu

```
python3 spectertext.py -h
```

---

# Embedding a Secret Message

Command:

```
python3 spectertext.py -e "your secret message" -f file.txt
```

Example:

```
python3 spectertext.py -e "attack at midnight" -f notes.txt
```

Output:

```
[+] Secret embedded successfully.
```

The secret message is now hidden inside **notes.txt**.

Important:

The file will look unchanged to normal users.

---

# Extracting Hidden Message

Command:

```
python3 spectertext.py -x -f file.txt
```

Example:

```
python3 spectertext.py -x -f notes.txt
```

Output:

```
Hidden Message:

attack at midnight
```

---

# Example Workflow

Step 1 – Create a text file

```
nano document.txt
```

Example content:

```
This is a normal document.
Nothing suspicious here.
```

Step 2 – Hide secret message

```
python3 spectertext.py -e "this is classified" -f document.txt
```

Step 3 – Extract hidden message

```
python3 spectertext.py -x -f document.txt
```

---

# Project Structure

```
SpecterText/
│
├── spectertext.py
├── README.md
└── sample.txt
```

---

# Limitations

* Works best with **UTF-8 encoded text files**
* Some text editors that remove invisible characters may break hidden data
* Large messages may increase file size slightly

---

# Educational Use

This tool is intended for:

* Cybersecurity learning
* Steganography research
* Digital forensics practice
* Capture The Flag (CTF) challenges

---

# Author

Cyber Specterz

Cybersecurity Research | Ethical Hacking | Security Tools

---

# License

This project is released for educational purposes.

---

# Disclaimer

This tool is created for **educational and research purposes only**.
The author is not responsible for misuse or illegal activities performed using this tool.
