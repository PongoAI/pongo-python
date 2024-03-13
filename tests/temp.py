import time
import pongo
import uuid
#Install with "pip install --upgrade pongo-python"

pongo_client = pongo.PongoClient("e1d2e57eb927440ab7492b25ffb39adb")

def pongo_demo():
    sub_org_id = pongo_client.create_sub_org(sub_org_name='test').json()['sub_org_id']

    group_parent_id = str(uuid.uuid4())
    #upload your own text data to Pongo
    with open("/Users/sina/Downloads/Uflo Platform/extract_pdf/transcript-merge/transcript/slides.txt", 'r') as file:
        slides_data = file.read()
    with open("/Users/sina/Downloads/Uflo Platform/extract_pdf/transcript-merge/transcript/transcript.txt", 'r') as file:
        transcript_data = file.read()
    
    split_slides = []
    temp_str = ''
    for i in range(len(slides_data)):
        temp_str += slides_data[i]
        if i % 1000 == 0 and i != 0:
            split_index = temp_str.rfind('\n')
            split_slides.append(temp_str[:split_index])
            temp_str = temp_str[split_index:]
    split_slides.append(temp_str)

    split_transcripts = []
    temp_str = ''
    for i in range(len(transcript_data)):
        temp_str += transcript_data[i]
        if i % 1000 == 0 and i != 0:
            split_index = temp_str.rfind('\n')
            split_transcripts.append(temp_str[:split_index])
            temp_str = temp_str[split_index:]
    split_transcripts.append(temp_str)

    all_text = split_slides + split_transcripts

    upload_response = pongo_client.upload(
        data=all_text,
        metadata={'parent_id': group_parent_id, 'source': 'Pongo Tutorial'},
        sub_org_id=sub_org_id)
    upload_result_data = upload_response.json()


    job_id = upload_result_data['job_id']
    
    #Wait for the job to complete before searching for the data we uploaded
    while True:
        job_status = pongo_client.get_job(job_id=job_id, sub_org_id=sub_org_id).json()['job']['job_status']

        if job_status == 'processed':
            break
        else:
            print(f'waiting for job {job_id} to process')
            time.sleep(5)
    
    #Returns the data we uploaded earlier
    search_response = pongo_client.search(query="What is User1's favorite color?", sub_org_id=sub_org_id)

    return search_response.json() 

print(pongo_demo()) 
    