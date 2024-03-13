import time
import pongo
import uuid
#Install with "pip install --upgrade pongo-python"

pongo_client = pongo.PongoClient("7309ef003c354494b6f3f8b6951b857f")
print(pongo_client.get_sub_orgs().json())
quit()
def pongo_demo():
    sub_org_id = pongo_client.create_sub_org(sub_org_name='Tutorial Organization').json()['sub_org_id']

    group_parent_id = str(uuid.uuid4())
    #upload your own text data to Pongo
    upload_response = pongo_client.upload(
        data=[
            "User1's favorite color is blue.",
            "User2's favoire color is red.",
            "Uesr3's favorite color is green."], 
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
    