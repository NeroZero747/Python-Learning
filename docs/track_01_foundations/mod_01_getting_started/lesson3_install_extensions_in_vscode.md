# Module 1 — Getting Started

## Lesson 3 — How to Install Extensions in VS Code

### Lesson Objective

By the end of this lesson learners will understand:

• what Visual Studio Code (VS Code) extensions are  
• how extensions improve the Python development experience  
• which Python extensions are most important  
• how to install and manage extensions in VS Code  

Extensions add powerful capabilities to VS Code that make writing, debugging, and managing Python code much easier.

### Overview

Visual Studio Code (VS Code) is one of the most popular editors used for Python development. While VS Code works as a basic text editor out of the box, its true power comes from **extensions**.

Extensions are small software packages that add features to the editor.

Examples of what extensions can provide:

• Python syntax highlighting  
• intelligent code suggestions  
• debugging tools  
• code formatting  
• integrated notebook support  

Without extensions, VS Code simply displays text files. With the proper extensions installed, it becomes a **full Python development environment**.

For Python development, the most important extension is the **Python extension provided by Microsoft**.

This extension enables features such as:

• automatic code completion  
• error detection  
• debugging support  
• running Python scripts directly from the editor  

Additional extensions can further enhance productivity by improving formatting, linting, and notebook integration.

### Key Idea Cards (Cards)

#### Extensions Add Functionality (Card 1)

VS Code extensions add new capabilities to the editor.

Examples:

• debugging tools  
• syntax highlighting  
• language support  

Extensions allow developers to customize their development environment.

#### The Python Extension Is Essential (Card 2)

The **Python extension by Microsoft** is the most important extension for Python development.

It enables:

• running Python scripts  
• debugging programs  
• code suggestions  
• Jupyter Notebook integration  

Without this extension, Python development in VS Code would be very limited.

#### Extensions Improve Productivity (Card 3)

Extensions help developers work faster and make fewer mistakes.

Helpful features include:

• auto-complete suggestions  
• automatic formatting  
• code linting  
• debugging support  

These tools make development smoother and more efficient.

### Key Concepts (Tabs)

#### What is an Extension? (Tab 1)

An extension is a plugin that adds features to VS Code.

Extensions allow VS Code to support many different programming languages and workflows.

Examples of extensions include:

| Extension | Purpose |
|--------|---------|
| Python | Python development tools |
| Pylance | advanced code analysis |
| Jupyter | notebook support |
| Black Formatter | automatic code formatting |

Each extension adds specific functionality to the editor.

#### Python Extension (Tab 2)

The Python extension enables core Python development features.

Features include:

• running Python scripts  
• debugging code  
• code completion suggestions  
• environment selection  

This extension is maintained by Microsoft and widely used in the Python community.

#### Pylance (Tab 3)

Pylance is a language server that enhances Python development by providing:

• faster code analysis  
• type checking  
• improved code completion  

Pylance works together with the Python extension to improve the development experience.

### Decision Flow

When VS Code starts, it checks which extensions are installed.

Example flow:

```text
Open VS Code
      ↓
VS Code loads installed extensions
      ↓
Python extension activates
      ↓
Python files recognized
      ↓
Developer writes and runs Python code
```

When a `.py` file is opened, the Python extension automatically activates.

This enables syntax highlighting and coding assistance.

### Code Examples (Tabs)

#### Example - Using Extensions (Tab 1)

Extensions themselves are installed through the VS Code interface, not through Python code.

However, once the Python extension is installed, you can run Python code directly from VS Code.

Example Python file:

```python
print("VS Code is ready for Python development")
```

Running the script inside VS Code will display the output in the terminal panel.

#### Example — Using Auto Completion (Tab 2)

After installing the Python extension, VS Code can suggest code automatically.

Example:

Start typing:

```python
pri
```

VS Code will suggest:

```python
print()
```

This feature helps developers write code faster and avoid mistakes.

#### Example — Running Python Code in VS Code (Tab 3)

Create a file called:

```text
test_program.py
```

Add this code:

```python
name = "Python"

print("Learning", name)
```

Press the **Run Python File** button in VS Code.

Output:

```text
Learning Python
```

### SQL / Excel Comparison

Development tools exist for SQL and Excel as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| editor | VS Code | SQL client | Excel interface |
| extensions | VS Code plugins | database plugins | add-ins |
| execution | Python interpreter | database engine | calculation engine |

These tools help developers write and execute instructions efficiently.

### Practice Exercises (Tabs)

#### Exercise 1 (Tab 1)

Tags: VS Code, Extensions, Python Extension

Open VS Code and navigate to the **Extensions panel**.

Shortcut:

```text
Ctrl + Shift + X
```

Search for:

```text
Python
```

Install the **Python extension by Microsoft**.

#### Exercise 2 (Tab 2)

Tags: Extensions, Pylance, Jupyter

Install the following extensions:

• Python  
• Pylance  
• Jupyter  

Observe how these extensions add new features to VS Code.

#### Exercise 3 (Tab 3)

Tags: Syntax Highlighting, Python Files, Testing

Create a Python file and test whether syntax highlighting works correctly.

Example code:

```python
print("VS Code Python extension installed successfully")
```

If the extension is working, keywords and strings should appear in different colors.

### Common Mistakes (Tabs)

#### Installing the Wrong Extension (Tab 1)

There are many Python-related extensions available.

Always install the **Python extension published by Microsoft**.

#### Forgetting to Restart VS Code (Tab 2)

Sometimes extensions require restarting the editor before they activate.

If features are not working, restart VS Code.

#### Installing Too Many Extensions (Tab 3)

Installing too many extensions can slow down the editor.

Start with essential extensions:

• Python  
• Pylance  
• Jupyter  

Additional extensions can be added later if needed.

### Real-World Use

In professional environments, VS Code extensions enable developers to:

• debug complex programs  
• analyze large codebases  
• manage virtual environments  
• work with notebooks and scripts  

Example workflow:

```text
Open Python project in VS Code
      ↓
Write code
      ↓
Use auto-complete suggestions
      ↓
Run script
      ↓
Debug errors
```

Extensions transform VS Code into a powerful development environment.

### Lesson Recap

In this lesson you learned:

• VS Code extensions add functionality to the editor  
• the Python extension enables Python development features  
• Pylance improves code analysis and auto-completion  
• extensions help developers work faster and reduce errors  

Installing the correct extensions ensures a productive Python development environment.

### Next Lesson

Next you will learn:

**Lesson 4 — How to Setup a Virtual Environment**

In that lesson you will learn:

• what virtual environments are  
• why they are important in Python projects  
• how to create and activate them  

Virtual environments help manage project dependencies and keep Python environments organized.