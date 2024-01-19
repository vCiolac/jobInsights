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

    def check_key(self, job: Dict, key: str) -> None:
        if key not in job:
            raise ValueError(f"A chave {key} está ausente no dicionário.")

    def is_numeric(self, value: Union[int, str]) -> bool:
        str_value = str(value)
        return str_value.replace("-", "").isdigit()

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        mini = "min_salary"
        maxi = "max_salary"

        self.check_key(job, mini)
        self.check_key(job, maxi)

        if not self.is_numeric(job[mini]) or not self.is_numeric(job[maxi]):
            raise ValueError(f"Valores de {mini} ou {maxi} não são numéricos.")

        if int(job[mini]) > int(job[maxi]):
            raise ValueError(f"Valor de {mini} é maior que o de {maxi}.")

        if not self.is_numeric(salary):
            raise ValueError("O valor do salário não é numérico.")

        return int(job[mini]) <= int(salary) <= int(job[maxi])

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
