class Salary:
    def __init__(self, from_amount, to_amount, currency):
        self.from_amount = from_amount
        self.to_amount = to_amount
        self.currency = currency

    def __str__(self):
        if self.from_amount is not None and self.to_amount is not None:
            return f'{self.from_amount} - {self.to_amount} {self.currency}'
        elif self.from_amount is not None:
            return f'От {self.from_amount} {self.currency}'
        elif self.to_amount is not None:
            return f'До {self.to_amount} {self.currency}'
        else:
            raise Exception('Поля from_amount или to_amount не должны быть оба None.')


class Vacancy:
    def __init__(self, hh_id, name, description, skills, employer_name, salary, area_name, published_at):
        self.hh_id = hh_id
        self.name = name
        self.description = description
        self.skills = skills
        self.employer_name = employer_name
        self.salary = salary
        self.area_name = area_name
        self.published_at = published_at

    @property
    def str_skills(self):
        return ', '.join(self.skills)

    def str_published_at(self):
        return self.published_at.strftime('%d.%m.%Y %H:%M')
