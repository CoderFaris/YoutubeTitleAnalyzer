

# YouTube Video Analyzer

The YouTube Video Analyzer is a Python application that utilizes Natural Language Processing (NLP) and Named Entity Recognition (NER) techniques to analyze and track the most common nouns in the titles of YouTube videos. It provides insights into the frequently occurring entities in the video titles and calculates the average views of the analyzed videos.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CoderFaris/YoutubeTitleAnalyzer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd YoutubeTitleAnalyzer
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Obtain a YouTube Data API key:
   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project or select an existing project.
   - Enable the YouTube Data API v3 for your project.
   - Generate an API key for your project.

5. Configure the API key:
   - Rename the `.env.example` file to `.env`.
   - Open the `.env` file and replace `YOUR_API_KEY` with your YouTube Data API key.

## Usage

1. Run the application:
   ```bash
   python gui.py
   ```

2. Enter a search query in the provided input field.

3. Click the "Analyze" button to analyze the YouTube videos related to the search query.

4. The application will display the most common named entities (nouns) in the video titles, along with their frequencies. Additionally, the average views of the analyzed videos will be shown.

5. Click the "Export" button to export the results to a CSV file. A file dialog will appear to choose the destination and name of the exported file.

## Contributing

Contributions to the YouTube Video Analyzer project are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request. Make sure to follow the project's coding conventions and guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
