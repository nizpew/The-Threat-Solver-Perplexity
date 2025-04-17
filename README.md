
 <div align="center">
  <a href="https://i.postimg.cc/Xv5mWNyz/perplexity-icon-staticanalisys.jpg" target="_blank">
    <img alt="The Threat Solver" src="https://i.postimg.cc/Xv5mWNyz/perplexity-icon-staticanalisys.jpg" height="20" style="margin-right: 10px;" />
    <img src="https://img.shields.io/badge/The Threat Solver-505050?style=flat&logo=appveyor&logoColor=white" alt="The Threat Solver" />
  </a>
</div>



## Project Description

The Threat Solver is a powerful desktop application designed to help developers and security analysts quickly understand and evaluate codebases using advanced AI technology. By integrating the Perplexity AI API, the app provides two key features: detailed code explanations and malicious code detection.

Users can easily import entire folders of source code, choose the type of analysis they want, and receive clear, actionable insights directly within the app. The intuitive PyQt5-based interface ensures a smooth user experience, while multithreading keeps the application responsive during potentially time-consuming AI analysis.

This project bridges the gap between cutting-edge AI capabilities and practical software development needs, enabling faster code reviews, improved security auditing, and enhanced code comprehension. It is ideal for developers working with unfamiliar code, security professionals scanning for vulnerabilities, or anyone seeking to leverage AI to boost their productivity and code quality.

With robust error handling, secure API key management, and thoughtful UI design, The Threat Solver demonstrates how AI can be seamlessly integrated into everyday development workflows to make coding safer and more efficient.

---

## Inspiration

The Threat Solver was inspired by the rapid evolution of AI-powered code analysis tools and the increasing complexity of modern software. As codebases grow and security threats become more sophisticated, developers need smarter, faster ways to review, understand, and secure their code. Observing how AI can automate tedious review tasks, catch subtle bugs, and flag vulnerabilities that humans might miss motivated us to build a tool that brings these benefits directly to the desktop.

---

## What it does

- **Code Explanation:** Summarizes and explains code to help developers quickly understand unfamiliar files.
- **Malicious Code Detection:** Scans code for patterns and behaviors that may indicate security threats or vulnerabilities.
- Allows users to select a folder of code, choose the type of analysis, and view results with clear visual safety indicators.

---

## How we built it

- Built with Python and PyQt5 for the GUI.
- Uses the Perplexity AI API for advanced code analysis.
- Implements multithreading with QThread to keep the UI responsive.
- Handles large code files by splitting them into chunks for API processing.
- Manages API keys securely via environment variables.

---

## Challenges we ran into

- Handling large files and chunking code effectively.
- Managing API rate limits and unexpected responses.
- Designing a responsive UI that provides clear feedback during analysis.
- Ensuring secure handling of API keys and user data.

---

## Accomplishments that we're proud of

- Creating a seamless, user-friendly desktop app that integrates AI-powered code analysis.
- Successfully implementing asynchronous API calls without freezing the UI.
- Robust error handling for various edge cases.
- Clear visual indicators to communicate analysis results effectively.

---

## What we learned

- The strengths and limitations of AI in code analysis.
- Best practices for asynchronous programming in PyQt5.
- How to design user-friendly interfaces that handle complex background tasks.
- The importance of secure API key management and error feedback.

---

## What's next for The Threat Solver

- Expand support for more programming languages and file types.
- Integrate additional AI models for deeper security and performance insights.
- Add collaboration features for team workflows.
- Allow customizable analysis rules and thresholds.
- Implement continuous learning from user feedback to improve accuracy.

---

## Built With

**Languages**
- Python

**Frameworks & Libraries**
- PyQt5
- Requests

**Platforms**
- Cross-platform desktop (Windows, macOS, Linux)

**APIs**
- Perplexity AI API

---

## Try It Out
  
  bash
  
    #install git if not installed
    git clone https://github.com/nizpew/The-Threat-Solver-Perplexity.git
    python The-Threat-Solver-Perplexity/main.py
    
- Demo Video: [Add your YouTube or Vimeo demo link here]

---

## Project Media

![App Screenshot 1](path/to/screenshot1.png)  
![App Screenshot 2](path/to/screenshot2.png)

---

## Video Demo Link

[Add your YouTube, Vimeo, or other video demo link here]
