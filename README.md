# Habit Tracker Capstone 🚀

This is a Concierge Agents built with Google ADK to help with Habit tracking

<img width="745" height="657" alt="image" src="https://github.com/user-attachments/assets/a425db30-14fc-4678-8e69-487fa00f8d57" />


[](https://opensource.org/licenses/MIT)
[](https://www.python.org/)
[](https://github.com/google/adk-python)

**Habit Tracker Capstone** is an intelligent Concierge Agent designed to help users build, track, and maintain positive habits. Built on top of the **Google Agent Development Kit (ADK)**, this project leverages the power of Generative AI (Gemini) to provide a conversational and personalized tracking experience.

Unlike traditional static apps, this AI Agent can understand natural language goals, provide motivation, and intelligently log progress through conversation.

-----

## 🌟 Features

  * **Conversational Interface**: Interact with your habit tracker using natural language (e.g., "I drank 2 liters of water today" or "Log a 30-minute run").
  * **Intelligent Goal Setting**: The agent helps define realistic habits and breaks them down into actionable steps.
  * **Progress Monitoring**: Keeps track of daily, weekly, and monthly streaks.
  * **Built with Google ADK**: Utilizes the latest agentic frameworks for robust tool calling and state management.
  * **Data Persistence**: securely stores user habits and logs using a **SQLite database**.

-----

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

  * **Python 3.10+**
  * **Google Cloud Project** with Vertex AI API enabled (or a Gemini API Key).

-----

## ⚡ Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/saran-surya/habit-tracker-capstone.git
    cd habit-tracker-capstone
    ```

2.  **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: This installs `google-adk`, `google-genai`, and other necessary libraries)*

4.  **Set up Environment Variables**
    Create a `.env` file in the root directory and add your API keys:

    ```bash
    GOOGLE_API_KEY=your_gemini_api_key_here
    # GOOGLE_CLOUD_PROJECT=your_project_id (if using Vertex AI)
    ```

-----

## 🚀 Usage (Running the Agent)

The agent is designed to be run via the **ADK Command Line Interface (CLI)**, exposing a web interface for interaction and using a local SQLite database for persistence.

1.  **Execute the ADK Web Command**

    Run the following command from the root directory of the project:

    ```bash
    adk web --session_data_uri 'sqlite:///habit_tracker.db'
    ```

      * This command launches the **ADK web interface**, allowing you to interact with the agent through your browser.
      * The `'sqlite:///habit_tracker.db'` argument ensures that all session data, conversation history, and habit logs are saved to a file named **`habit_tracker.db`** in the project directory.

2.  **Start Interacting**

    Once the command runs successfully, open the provided local URL in your browser (usually `http://localhost:8080` or similar) to chat with your Habit Tracker Agent.

    **Example Interaction:**

    > **User**: "I want to start reading more."
    > **Agent**: "That's a great goal\! How about we set a daily target? Maybe 15 minutes a day to start? I can remind you every evening."

-----

## 🤝 Contributing

Contributions are welcome\! Please follow these steps:

1.  Fork the project.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

-----

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

-----

## 🙏 Acknowledgments

  * Built with [Google Agent Development Kit](https://github.com/google/adk-python).
  * Powered by Google Gemini Models.

[How to create AI agents with Agent Development Kit (ADK)](https://www.youtube.com/watch?v=bLYbL3d5MwQ)
