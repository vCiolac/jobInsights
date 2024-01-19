import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file_path: str) -> List[Dict]:
        with open(file_path, "r") as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                self.jobs_list.append(line)

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set()

        for job in self.jobs_list:
            unique_job_types.add(job["job_type"])

        return list(unique_job_types)

    def filter_by_multiple_criteria(
        self,
        jobs_list: List[Dict],
        filter_criteria: Dict
    ) -> List[dict]:
        filtered_jobs = list()

        jtype = filter_criteria["job_type"]
        ind = filter_criteria["industry"]

        for job in jobs_list:
            if job["job_type"] == jtype and job["industry"] == ind:
                filtered_jobs.append(job)

        return filtered_jobs
