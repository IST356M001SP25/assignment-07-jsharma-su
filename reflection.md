# Reflection

Student Name:  Jiya Sharma
Sudent Email:  jsharma@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

This assignment has been a learning experience, not just in terms of understanding the technical aspects of working with Python and pytest, but also in navigating the various obstacles that can arise when setting up and running a development environment. Throughout the process, I encountered multiple issues, which, although frustrating at times, ultimately helped me understand the importance of properly configuring my environment and debugging effectively.

The first major hurdle I faced was getting pytest up and running in my virtual environment. Despite having installed pytest through pip, I kept receiving an error stating that pytest was not found when I tried to run my tests. This error, ModuleNotFoundError: No module named 'pytest', was particularly confusing, especially since I had previously installed it. After some troubleshooting, I discovered that my virtual environment wasn't properly activated, which meant that Python wasn't pointing to the correct environment where pytest was installed.

This situation made me realize how crucial it is to ensure that the virtual environment is activated before installing packages or running any tests. It also reinforced the need to double-check that the correct version of Python is being used, especially when working with multiple environments.

In addition to the issues with pytest installation, I ran into problems with Python import errors. Specifically, the error ModuleNotFoundError: No module named 'code.menuitem'; 'code' is not a package occurred when I tried to run tests. This issue was related to how the code was structured within my project. I had mistakenly referenced a module that Python couldn't locate. I had to adjust the import paths to properly reflect the structure of my project. This experience underscored the importance of understanding module and package structures in Python, especially when dealing with larger projects or when using external libraries.

While troubleshooting these issues, I also learned the importance of debugging effectively. I tried using print statements and placing breakpoints to observe what was happening during the tests. This allowed me to pinpoint where things were going wrong, and, over time, I became more comfortable with the process of step-by-step debugging.

Additionally, the errors I encountered made me more aware of the nuances of working in an Integrated Development Environment (IDE) like VS Code. I learned that sometimes the IDE’s environment may not be correctly configured to use the right Python interpreter, leading to confusion and errors. I had to adjust the settings to ensure that it used the interpreter from the virtual environment, which was another valuable takeaway.

In summary, this assignment provided an opportunity to strengthen my problem-solving and debugging skills. I learned the importance of carefully managing my development environment, ensuring that dependencies are correctly installed and imported, and double-checking configurations. Although it was a frustrating experience at times, it has made me more confident in dealing with similar issues in future projects. I now have a deeper understanding of how to handle Python environments, troubleshoot import issues, and work with pytest to effectively run and debug tests.

