# Word Saver 单词快存

Select any text on your screen, press **F8**, and it's instantly saved with translation and phonetics to a dated Excel file.

## Quick Start

**Option A – No Python needed (recommended)**

1. Go to [Releases](../../releases) and download `WordSaver.exe`
2. Double-click it → click "Yes" on the UAC prompt
3. A blue **W** icon appears in your system tray — you're ready

**Option B – Run from source**

```bash
git clone https://github.com/GEUConn/word-saver.git
cd word-saver
```
Then right-click `安装和运行.bat` → **Run as administrator**

## Usage

| Action | Result |
|---|---|
| Select text → press `F8` | Translates and saves to Excel |
| Right-click tray icon | Open word folder / Exit |

- **English input** → translated to Chinese + IPA phonetics
- **Chinese input** → translated to English + pinyin
- Each day's words saved to a separate `YYYY-MM-DD.xlsx` in the same folder as the exe

## Requirements (source only)

- Windows 10/11
- Python 3.8+
- Internet connection (uses Google Translate)

## Build exe yourself

Right-click `打包成exe.bat` → Run — generates `WordSaver.exe` in the same folder.
