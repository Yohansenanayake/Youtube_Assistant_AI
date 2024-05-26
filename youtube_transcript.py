
from youtube_transcript_api import YouTubeTranscriptApi
#import youtube_id as yat
from urllib.parse import urlparse, parse_qs

def get_youtube_video_id(url):
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Check if the URL is from youtube.com or youtu.be
    if 'youtube.com' in parsed_url.netloc:
        # Extract the query parameters
        query_params = parse_qs(parsed_url.query)
        # Return the value of the 'v' parameter if it exists
        return query_params.get('v', [None])[0]
    elif 'youtu.be' in parsed_url.netloc:
        # The video ID is the path component of the URL
        return parsed_url.path.lstrip('/')
    else:
        return None




def transcript_to_text(transcript):
    combined_text = ' '.join([entry['text'].strip() for entry in transcript])
    return combined_text

def youtube_transcript_from_url(url):

    video_id = get_youtube_video_id(url)
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    for transcript in transcript_list:
        if transcript.is_generated:
            if transcript.language_code == 'en':
                return(transcript_to_text(transcript.fetch()))
            else:
                return(transcript_to_text(transcript.translate('en').fetch()))
                
        else:
            if transcript.language_code == 'en':
                return(transcript_to_text(transcript.fetch()))
            else:
                return(transcript_to_text(transcript.translate('en').fetch()))
                





    

