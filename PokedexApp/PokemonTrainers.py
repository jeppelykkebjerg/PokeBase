import random

def ReturnTrainerId() -> str:
    trainer_id: int = random.randint(1,51)
    trainer_id_str = f"TID-{trainer_id}"
    return trainer_id_str


print(ReturnTrainerId())