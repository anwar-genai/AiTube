from ..celery_app import celery_app
from .utils import get_logger


logger = get_logger(__name__)


@celery_app.task(name="summarization.run")
def run_summarization(video_id: str, transcript: str) -> dict:
    logger.info(f"Summarizing transcript for {video_id}")
    
    import openai
    import os
    
    # Get OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai.api_key:
        logger.warning("OpenAI API key not found, using mock summary")
        summary = {
            "summary_text": f"Mock summary for video {video_id}: This is a sample summary of the video content.",
            "hashtags": "#programming #tutorial #coding",
            "keywords": "programming, tutorial, coding, development",
        }
        return {"video_id": video_id, **summary}
    
    try:
        # Use OpenAI to generate summary
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert at summarizing video content. Create a concise summary, relevant hashtags, and key keywords."},
                {"role": "user", "content": f"Summarize this video transcript: {transcript[:2000]}"}  # Limit transcript length
            ],
            max_tokens=500
        )
        
        summary_text = response.choices[0].message.content
        
        # Extract hashtags and keywords (simple approach)
        hashtags = "#programming #tutorial #coding"  # You could make this smarter
        keywords = "programming, tutorial, coding, development"
        
        summary = {
            "summary_text": summary_text,
            "hashtags": hashtags,
            "keywords": keywords,
        }
        
        logger.info(f"Generated summary for {video_id} using OpenAI")
        return {"video_id": video_id, **summary}
        
    except Exception as e:
        logger.error(f"Error generating summary with OpenAI: {e}")
        # Fallback to mock summary
        summary = {
            "summary_text": f"Summary for video {video_id}: This is a fallback summary due to API error.",
            "hashtags": "#programming #tutorial",
            "keywords": "programming, tutorial",
        }
        return {"video_id": video_id, **summary}


