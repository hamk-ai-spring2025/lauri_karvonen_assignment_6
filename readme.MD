# Assignment 6: Image Assignments

Hestia // Lauri Karvonen

## Versatile command line utility for image generator using OpenAI API and DALL-E 3

This repository contains a command-line tool that allows users to generate images using OpenAI's DALL-E 3 model through the OpenAI API.

## Overview
- **Objective:** Generate high-quality images from text prompts using DALL-E 3
- **Features:**
    - Simple command line interface
    - Customizable image generation parameters
    - Image saving and management
    - Integration with OpenAI's API

## Files and Folders
- **readme.MD:** This file, providing an overview and instructions.
- **src/**: Contains the source code for the image generation tool.
- **images/**: Where generated images are saved.
- **config/**: Configuration files including API settings.

## Setup and Requirements
1. **Clone the Repository:**
     ```
     git clone https://github.com/yourusername/assignment_6.git
     ```
2. **Environment Setup:**
     - Install Python (>= 3.7)
     - Use a virtual environment:
         ```
         python -m venv venv
         source venv/bin/activate  # Linux/Mac
         venv\Scripts\activate  # Windows
         ```
3. **Install Dependencies:**
     ```
     pip install -r requirements.txt
     ```
4. **Set up OpenAI API Key:**
     - Create an account at [OpenAI](https://openai.com/)
     - Generate an API key in your account dashboard
     - Set your API key as an environment variable:
       ```
       export OPENAI_API_KEY=your_api_key_here  # Linux/Mac
       set OPENAI_API_KEY=your_api_key_here  # Windows
       ```

## Using the Image Generator
- Run the command-line tool:
    ```
    python src/main.py --prompt "Your image description here"
    ```
- Additional options:
    ```
    python src/main.py --prompt "A beautiful sunset" --size "1024x1024" --output "sunset.png"
    ```

## Example Commands
- Generate a basic image:
  ```
  python src/main.py --prompt "A cyberpunk city at night with neon lights"
  ```
- Specify image size and output location:
  ```
  python src/main.py --prompt "A serene mountain landscape" --size "1792x1024" --output "landscape.png"
  ```

## Further Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [DALL-E 3 Guide](https://platform.openai.com/docs/guides/images)
- [OpenAI Usage Policies](https://openai.com/policies/usage-policies)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
