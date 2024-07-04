import json
import datetime

def json_to_srt(json_data):
    subtitles = json.loads(json_data)
    srt_content = []

    for index, subtitle in enumerate(subtitles):
        start_time = str(datetime.timedelta(seconds=subtitle["start_time"])).split(".")
        end_time = str(datetime.timedelta(seconds=subtitle["end_time"])).split(".")
        
        start_time_str = start_time[0] + ',' + start_time[1][:3] if len(start_time) > 1 else start_time[0] + ',000'
        end_time_str = end_time[0] + ',' + end_time[1][:3] if len(end_time) > 1 else end_time[0] + ',000'
        
        srt_content.append(f"{index + 1}")
        srt_content.append(f"{start_time_str} --> {end_time_str}")
        srt_content.append(subtitle["text"])
        srt_content.append("")

    return "\n".join(srt_content)

#Example Transcript
json_transcript = '''
[
    {"start_time": 0, "end_time": 5, "text": "Hello, this is a sample subtitle."},
    {"start_time": 6, "end_time": 10, "text": "This is another subtitle example."}
]
'''

srt_output = json_to_srt(json_transcript)
print(srt_output)
