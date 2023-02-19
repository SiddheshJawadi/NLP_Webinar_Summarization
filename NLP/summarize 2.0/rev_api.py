from rev_ai import apiclient
from summa import summarizer

token = "02_I_UQbcXYLN3pO3Qc2Mslu40bBRcm-fgoAt3MZuocSC6V7qn6by6D4e-aP7NY-8nf0AjakFXM8_KHvUeGkwaMoa0GRs"
filePath = "D:/NLP/trial4.mp4"

# create your client
client = apiclient.RevAiAPIClient(token)

# send a local file
#job = client.submit_job_local_file(filePath)

# check job status
job_details = client.get_job_details('pyYEqT77v35tq5Op')

# retrieve transcript as text
transcript_text = client.get_transcript_text('pyYEqT77v35tq5Op')

# retrieve transcript as JSON
transcript_json = client.get_transcript_json('pyYEqT77v35tq5Op')

# retrieve transcript as a Python object
text_stream = client.get_transcript_text('pyYEqT77v35tq5Op')

with open('sample.txt', 'w') as f:
    f.write(text_stream)
file = open('sample.txt',"r") 
text = file.readline()
summary = summarizer.summarize(text)
filename = 'summary1.txt'
with open(filename, 'w') as f:
    f.write(summary)