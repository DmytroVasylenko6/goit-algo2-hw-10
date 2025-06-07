class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            coverage = teacher.can_teach_subjects & remaining_subjects
            if len(coverage) > len(best_coverage) or (
                len(coverage) == len(best_coverage)
                and teacher.age < (best_teacher.age if best_teacher else float("inf"))
            ):
                best_teacher = teacher
                best_coverage = coverage

        if not best_teacher:
            print("Неможливо покрити всі предмети наявними викладачами.")
            return None

        best_teacher.assigned_subjects = best_coverage
        schedule.append(best_teacher)
        remaining_subjects -= best_coverage

    return schedule


if __name__ == "__main__":
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    teachers = [
        Teacher(
            "Ірина", "Литвин", 40, "i.lytvyn@example.com", {"Математика", "Інформатика"}
        ),
        Teacher(
            "Андрій", "Семенюк", 34, "a.semenyuk@example.com", {"Фізика", "Математика"}
        ),
        Teacher("Тетяна", "Коваль", 29, "t.koval@example.com", {"Хімія"}),
        Teacher("Богдан", "Марчук", 36, "b.marchuk@example.com", {"Біологія", "Хімія"}),
        Teacher("Олег", "Нікітін", 44, "o.nikitin@example.com", {"Інформатика"}),
        Teacher("Леся", "Гаврилюк", 39, "l.havrylyuk@example.com", {"Біологія"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
