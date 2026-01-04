# 🔍 AI Domain Deep Research Agent

An advanced AI research agent built using the Agno Agent framework and OpenAI's GPT models. This agent helps users conduct comprehensive research on any topic by generating research questions, finding answers through multiple search engines, and compiling professional reports with multiple export options.

## Features

### 🧠 **Intelligent Question Generation**

- Automatically generates customizable research questions (3-10 questions)
- Supports multiple question types: yes/no, open-ended, comparative, and analytical
- Tailors questions to your specified domain
- Dynamic question generation based on research needs

### 🔎 **Multi-Source Research**

- Uses **SerpApi** (Google Search API) for comprehensive web results with source tracking
- Leverages **Perplexity AI** for deeper analysis
- Combines multiple sources for thorough research
- Parallel processing for faster research execution
- Automatic citation extraction and tracking

### 📊 **Professional Report Generation**

- Compiles research findings into a McKinsey-style report
- Structures content with executive summary, analysis, and conclusion
- Includes comprehensive source citations
- Multiple export formats: PDF, Markdown, and JSON

### ⚡ **Performance Enhancements**

- Parallel question research using asyncio
- Real-time progress tracking
- Optimized agent calls
- Faster research completion

### 🖥️ **User-Friendly Interface**

- Clean Streamlit UI with intuitive workflow
- Collapsible sections for better organization
- Real-time progress indicators
- Expandable sections to view detailed results
- Research settings customization panel



## New Features

### Question Customization
- Adjust the number of research questions (3-10)
- Select from different question types for varied research approaches

### Parallel Research Processing
- Research multiple questions simultaneously for faster results
- Real-time progress tracking for each question

### Citation Tracking
- Automatic extraction of source URLs from search results
- Source credibility indicators
- Comprehensive citations section in reports


## Technical Details

- **Agno Framework**: Used for creating and orchestrating AI agents
- **OpenAI**: Provides GPT-4 model for advanced language processing
- **SerpApi**: Google Search API service for comprehensive web results
- **Streamlit**: Powers the user interface with interactive elements
- **Asyncio**: Enables parallel processing for faster research

## Dependencies

- `agno>=2.2.10` - Agent framework
- `streamlit` - Web interface
- `openai` - OpenAI API client
- `requests` - HTTP library for API integrations (SerpApi, Perplexity)
- `reportlab` - PDF generation
- `python-dotenv` - Environment variable management

## Example Use Cases

- **Academic Research**: Quickly gather information on academic topics across various disciplines
- **Market Analysis**: Research market trends, competitors, and industry developments
- **Policy Research**: Analyze policy implications and historical context
- **Technology Evaluation**: Research emerging technologies and their potential impact
- **Competitive Intelligence**: Analyze competitors and market positioning
- **Trend Analysis**: Track and analyze industry trends

