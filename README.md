# **styled_print**

A simple utility for printing styled text to the terminal with color, background, and other styles.

## **Installation**

You can install `styled_print` via pip:

```bash
pip install styled_print
```

## **Usage**

The `styled_print` function allows you to print styled text in the terminal. It accepts a string and an `options` dictionary to customize the output.

### **Function Signature:**

```python
styled_print(string, options)
```

### **Parameters:**

- `string` (str): The text you want to print.
- `options` (dict): A dictionary containing styling options.  
  The dictionary can include:
  - **`color`** (str, optional): The text color.  
    e.g., `"red"`, `"blue"`, `"green"`, etc.
  - **`styles`** (list, optional): A list of text styles.  
    Possible values: `["bold"]`, `["underline"]`, `["italic"]`, etc.
  - **`bg_color`** (str, optional): The background color.  
    e.g., `"on_white"`, `"on_red"`, etc.
  - **`uppercase`** (bool, optional): If `True`, converts the text to uppercase.
  - **`lowercase`** (bool, optional): If `True`, converts the text to lowercase.
  - **`align`** (str, optional): Align the text.  
    Possible values: `"left"`, `"center"`, `"right"`. Default is `"left"`.
  - **`padding`** (int, optional): Number of spaces to add around the text for padding. Default is `0`.
  - **`border`** (bool, optional): If `True`, prints the text with a border.

### **Example Usage:**

```python
from styled_print import styled_print

# Print bold red text on a white background
styled_print("Hello", {
    "color": "red",
    "styles": ["bold"],
    "bg_color": "on_white"
})

# Print uppercase text with padding and border
styled_print("Hello World", {
    "color": "blue",
    "styles": ["underline"],
    "bg_color": "on_yellow",
    "uppercase": True,
    "padding": 2,
    "border": True
})

# Print center-aligned, green italic text
styled_print("Centered Text", {
    "color": "green",
    "styles": ["italic"],
    "align": "center"
})
```

### **Example Output:**

For the example:

```python
styled_print("Hello", {
    "color": "red",
    "styles": ["bold"],
    "bg_color": "on_white"
})
```

You will get output like this:

```
Hello  (in bold red on white background)
```

For the second example with padding and a border, the output will look like this:

```
--------------------------------------------------
|     HELLO WORLD     |
--------------------------------------------------
```

### **Customization Options:**

- **Color:** The available text colors are the basic colors supported by `termcolor` (`red`, `blue`, `green`, etc.).
- **Text Styles:** You can apply multiple styles to text, such as:
  - `"bold"`: Makes the text bold.
  - `"underline"`: Underlines the text.
  - `"italic"`: Italicizes the text (not all terminals support this).
- **Background Color:** Background color options are also from `termcolor` (`on_white`, `on_red`, etc.).
- **Alignment:** You can align text to the `"left"`, `"center"`, or `"right"`.
- **Padding:** Adds a padding (space) around the text for visual clarity.
- **Border:** Wraps the text with a simple ASCII border.

### **Example Output:**

- **Uppercase Example:**

  ```python
  styled_print("hello", {"uppercase": True})
  ```

  Output:

  ```
  HELLO
  ```

- **Text with Padding:**

  ```python
  styled_print("padded text", {"padding": 4})
  ```

  Output:

  ```
  "    padded text    "
  ```

- **Text with Border:**

  ```python
  styled_print("bordered text", {"border": True})
  ```

  Output:

  ```
  ---------------------------
  | bordered text          |
  ---------------------------
  ```

## **License**

This package is licensed under the MIT [License](./LICENSE).
