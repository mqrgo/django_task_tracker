class TaskImportanceStatus:
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    CHOICES = (
        (HIGH, 'Высокий'),
        (MEDIUM, 'Средний'),
        (LOW, 'Низкий'),
    )


class TaskStatus:
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    PENDING = 'PENDING'

    CHOICES = (
        (IN_PROGRESS, 'В процессе'),
        (COMPLETED, 'Выполнена'),
        (PENDING, 'Ожидание'),
    )
