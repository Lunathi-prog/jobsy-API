from fastapi import FastAPI
from typing import List, Optional
from data.jobs_data import jobs

app = FastAPI() #Creates an instance of the FastAPI app
                #now there is an object called app
                #Will attach routes(URLs/endpoints) to it later



@app.get('/')
async def root():
    return {"message": "Welcome to Jobsy API"}


@app.get("/jobs")
def get_jobs(title: Optional[str] = None, location: Optional[str]= None) -> List[dict]:
    results = jobs

    #if title is provided, filter jobs by title

    if title:
        results = [job for job in results if title.lower() in job["title"].lower()]
    
    #if location is provided, filter jobs by location
    if location:
        results = [job for job in results if location.lower() in job["location"].lower()]

    return results