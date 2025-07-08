from crewai.tools import BaseTool
from typing import Type, List, Dict
from pydantic import BaseModel, Field

class ArxivSearchInput(BaseModel):
    """Input schema for ArxivSearch tool."""
    query: str = Field(..., description="Search query for arXiv papers in ML/AI/GenAI.")

class GithubTrendsInput(BaseModel):
    """Input schema for GithubTrends tool."""
    time_period: str = Field(
        default="daily",
        description="Time period for trending repos (daily, weekly, monthly)"
    )

class TechNewsInput(BaseModel):
    """Input schema for TechNews tool."""
    category: str = Field(
        default="all",
        description="Category of tech news (all, ai, ml, genai, mlops)"
    )

class ArxivSearchTool(BaseTool):
    name: str = "search_arxiv"
    description: str = (
        "Search arXiv for recent papers in ML/AI/GenAI. "
        "Returns a list of relevant papers with titles, summaries, and URLs."
    )
    args_schema: Type[BaseModel] = ArxivSearchInput

    def _run(self, query: str) -> List[Dict]:
        # TODO: Implement actual arXiv API integration
        return [
            {
                "title": "Example ML Paper",
                "summary": "This is a placeholder for paper summary",
                "url": "https://arxiv.org/example",
                "published_date": "2024-01-01"
            }
        ]

class GithubTrendsTool(BaseTool):
    name: str = "get_github_trends"
    description: str = (
        "Fetch trending ML/AI repositories from GitHub. "
        "Returns a list of repositories with their names, descriptions, and URLs."
    )
    args_schema: Type[BaseModel] = GithubTrendsInput

    def _run(self, time_period: str = "daily") -> List[Dict]:
        # TODO: Implement actual GitHub API integration
        return [
            {
                "name": "Example ML Repo",
                "description": "This is a placeholder for repo description",
                "url": "https://github.com/example/repo",
                "stars": 1000,
                "language": "Python"
            }
        ]

class TechNewsTool(BaseTool):
    name: str = "get_tech_news"
    description: str = (
        "Fetch recent ML/AI news from tech news sources. "
        "Returns a list of news articles with titles, summaries, and URLs."
    )
    args_schema: Type[BaseModel] = TechNewsInput

    def _run(self, category: str = "all") -> List[Dict]:
        # TODO: Implement actual news API integration
        return [
            {
                "title": "Example AI News",
                "summary": "This is a placeholder for news summary",
                "url": "https://technews.example/article",
                "source": "TechNews",
                "published_date": "2024-01-01"
            }
        ]

# Helper class to instantiate all tools
class TopicTools:
    """Collection of tools for the Chief Topic Strategist."""

    def __init__(self):
        self.arxiv_tool = ArxivSearchTool()
        self.github_tool = GithubTrendsTool()
        self.news_tool = TechNewsTool()

    @property
    def get_all_tools(self) -> List[BaseTool]:
        """Return all tools as a list."""
        return [
            self.arxiv_tool,
            self.github_tool,
            self.news_tool
        ]
