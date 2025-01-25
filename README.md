# 🌀 FlippinDuplex

**Turn your single-sided printer into a duplex pro!**

Tired of manually sorting and flipping pages when printing double-sided? **FlippinDuplex** helps you print duplex documents on a non-duplex printer by rearranging PDF pages in the perfect order. Just print, flip, and print again!

## 🚀 Features

- 📄 **Automatic page splitting** - Separates odd and even pages effortlessly
- 🔄 **Reverse order processing** - Ensures correct order after flipping
- 🖨️ **Print-ready output** - Saves pages with clear order instructions
- ⚡ **Super easy to use** - Just run a simple command!

## 🛠️ Installation

1. Make sure you have Python installed (version 3.x recommended)
2. Install the required dependency:

```bash
pip install pypdf2
```

## 📖 Usage

### Basic command:

```bash
python duplex_printer.py input.pdf
```

This generates:

input_1st_odd_pages.pdf → Print this file first.
input_2nd_even_pages_reversed.pdf → Flip paper & print this second.

Specify an output filename:

```bash
python duplex_printer.py input.pdf my_duplex_print.pdf
```

This creates:

my_duplex_print_1st_odd_pages.pdf
my_duplex_print_2nd_even_pages_reversed.pdf

🧐 Why Use FlippinDuplex?
Ever tried printing a long document only to mess up the order and waste paper? No more!
FlippinDuplex gives you step-by-step printing instructions, so even your grandma can do it! 🧓✨

💡 Pro Tips
Print odd pages first 🖨️
Flip the paper the right way (pay attention to orientation) 🔄
Print the even pages in reverse order 🏁
👏 Contributions
Got ideas? Found a bug? PRs are welcome! Create an issue or fork away!

📜 License
This project is licensed under the MIT License.

🤓 Fun Fact
Did you know? The first duplex printer was invented in 1984! Now you don't need one. 😉

yaml
Copiar
Editar

---

This README is fun, engaging, and provides clear instructions for users. Let me know if you'd like any changes!
