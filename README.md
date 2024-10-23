# Text2Pandas-Command-Generator


## Overview
The **Text2Pandas Command Generator** is a Streamlit application that allows users to upload a CSV file and convert natural language queries into Pandas commands for data analysis. Utilizing the Google Gemini API, the app assists users in generating accurate Pandas code based on their input, enabling efficient exploration of their datasets.

## Features
- Upload CSV files for analysis.
- Enter natural language queries to interact with the data.
- Automatically generate Pandas commands based on user queries.
- Execute generated commands and display the results.
- Integrated spelling correction for better command generation.
- Real-time DataFrame visualization.

## Requirements
To run the application, you need the following libraries:
- Streamlit
- Pandas
- google-generativeai
- python-dotenv
- pyspellchecker

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text2pandas.git
   cd text2pandas
   ```

2. Install the required Python packages:
   ```bash
   pip install streamlit pandas google-generativeai python-dotenv pyspellchecker
   ```

3. Create a `.env` file in the project root directory and add your Google Gemini API key:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:
```bash
streamlit run Text2pandas.py
```

Then, open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

1. **Upload CSV File**: Click on the "Upload a CSV file" button and select your CSV file.
2. **Enter Query**: Type your natural language query into the input box.
3. **Generate Command**: Click the "Generate Command" button to produce the corresponding Pandas command.
4. **View Results**: The results of executing the command will be displayed below.

## Example Queries
- "Show me the average value of column_name"
- "What are the unique values in the category column?"
- "Filter the data where column_a is greater than 100"

## Contributing
If you would like to contribute to this project, please feel free to submit a pull request or report issues.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Streamlit](https://streamlit.io/) - The framework used for the application.
- [Pandas](https://pandas.pydata.org/) - The data manipulation library.
- [Google Gemini API](https://cloud.google.com/generative-ai/docs/) - Used for natural language processing.
- [pyspellchecker](https://pypi.org/project/pyspellchecker/) - For spelling correction in queries.
