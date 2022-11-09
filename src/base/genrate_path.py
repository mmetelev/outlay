import uuid


def generate_user_file_path(instance, filename: str) -> str:
    """Генерация пути к директории с файлом пользователя"""
    return f'files/user_{instance.id}/{str(uuid.uuid4())}.{filename.split(".")[-1]}'
