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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
