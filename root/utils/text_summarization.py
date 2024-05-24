import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def abstractive_summary(clusters):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    summary = []
    for cluster in clusters.values():
        
        cluster_text = ' '.join(cluster)
        chunk_summary = client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': f"Provide a well detailed technical summary of the following text:\n{cluster_text}"
                }
            ],
            model='gpt-3.5-turbo'
        )
        summary.append(chunk_summary.choices[0].message.content.strip())

    summary_text = ' '.join(summary)
    final_summarization = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f"Improve the semantic format:\n{summary_text}"
            }
        ],
        model='gpt-3.5-turbo'
    )
        
    return final_summarization.choices[0].message.content.strip()