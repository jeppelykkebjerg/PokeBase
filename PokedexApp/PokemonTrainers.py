import random

def GetTrainerId() -> str:
    """
        We have 50 trainers in our trainer-union.
        This function returns a random number between 1 and 50 (inclusive) to provide the trainer-id variable
        in a pokedex event.

        Arguments: (none)

        Returns: str
    """
    trainer_id: int = random.randint(1,51)
    trainer_id_str = f"TID-{trainer_id}"

    return trainer_id_str