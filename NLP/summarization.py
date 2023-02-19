from summa import summarizer
def summary(filename):
    print("Enter the compression ratio: ")
    ratioi = float(input())
    final_ratio = 1-ratioi
    file = open(filename,"r") 
    text = file.readline()
    summary = summarizer.summarize(text, ratio = final_ratio)
    filename = 'summa_summary.txt'
    with open(filename, 'w') as f:
        f.write(summary)
    print('The transcript has been summarized successfully, generated the text file.......')

