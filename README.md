# 🌀 FlippinDuplex

Turn your single-sided printer into a duplex pro!

## 📑 Table of Contents

- [Features](#-features)
- [Why Use FlippinDuplex?](#-why-use-flippinduplex)
- [Requirements](#-requirements)
- [Installation](#️-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Pro Tips](#-pro-tips)
- [Troubleshooting](#️-troubleshooting--best-practices)
- [Contributions](#-contributions)
- [License](#-license)
- [Fun Fact](#-fun-fact)
- [Tested Configurations](#-tested-configurations)

## 🧐 Why Use FlippinDuplex?

Ever tried printing a long document only to mess up the order and waste paper? No more! FlippinDuplex gives you step-by-step printing instructions, so it's virtually impossible to make mistakes. Just follow the guide, and you'll have a perfectly printed document in no time!

## 🚀 Features

- 📄 **Automatic page splitting** - Separates odd and even pages effortlessly
- 🔄 **Reverse order processing** - Ensures correct order after flipping
- 🖨️ **Print-ready output** - Creates pre-organized files for two-pass printing
- 📁 **Multiple file handling** - Can merge and process multiple PDFs at once
- ⚡ **Super easy to use** - Just run a simple command!

## 🔧 Requirements

- Python 3.10+
- PyPDF2 library
- Single-sided printer (duplex not required)

## 🛠️ Installation

1. Make sure you have Python installed (version 3.x recommended)
2. Install the required dependencies:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📖 Usage

### Basic command

```bash
python duplex_printer.py input.pdf
```

### Output Files

- `input_1st_odd_pages.pdf` - Print first
- `input_2nd_even_pages_reversed.pdf` - Print after flipping paper

## 📚 Examples

### Single PDF Processing

Custom Output Name:

```bash
python duplex_printer.py input.pdf final_print.pdf
```

## 💡 Pro Tips

- Print odd pages first 🖨️
- Flip the paper the right way (pay attention to your printer's orientation) 🔄
- Print even pages in reverse order 🏁
- This was tested on an HP Smart Tank 555 printer.
- Make sure that your printer allways prints from the last page to the first page (reverse order). otherwise the script might not work as expected.

## ⚠️ Troubleshooting & Best Practices

For perfect duplex printing results, follow these key steps:

### 🖨️ Printer Setup

- **Critical**: Configure printer to print in reverse order (last page to first)
- Test printer's page order with a small document first

### 📄 Document Preparation

- Check PDF for any unwanted blank pages
- Start with a short test document before large prints

### 🔄 Printing Process

1. Print odd pages first
2. Pay careful attention to paper orientation when flipping

### 🚫 Common Issues

- Unexpected results? → Try a 2-3 page test document first
- Wrong page order? → Check printer's reverse order setting
- Misaligned pages? → Double-check paper orientation when flipping

## 👏 Contributions

Got ideas? Found a bug? PRs are welcome! Create an issue or fork away!

## 📜 License

This project is licensed under the MIT License.

## 🤓 Fun Fact

Did you know? The first duplex printer was invented in 1984! Now you don't need one. 😉

## 🔍 Tested Configurations

HP Smart Tank 555
Python 3.10
Ubuntu 20.04+/Windows 10+
