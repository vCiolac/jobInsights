from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> [int]:
        maxi = "max_salary"
        valid_salaries = [
            int(job[maxi])
            for job in self.jobs_list
            if job[maxi] not in ["", "None", None] and job[maxi].isdigit()
        ]

        return max(valid_salaries)

    def get_min_salary(self) -> int:
        mini = "min_salary"
        valid_salaries = [
            int(job[mini])
            for job in self.jobs_list
            if job[mini] not in ["", "None", None] and job[mini].isdigit()
        ]

        return min(valid_salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
