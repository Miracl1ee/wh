from pydantic import BaseModel, Field


class register_important(BaseModel):
    password: str = Field(..., min_length=1,
                          description="Пароль должен содержать больше 1 символа")
    username: str = Field(..., min_length=1,
                          description="Имя должно содержать больше 1 символа")


class add_homework_important(BaseModel):
    housework: str = Field(..., min_length=1,
                           description="Задача должна иметь больше 1 символа")
    username: str = Field(..., min_length=1,
                          description="Имя должно содержать больше 1 символа")
