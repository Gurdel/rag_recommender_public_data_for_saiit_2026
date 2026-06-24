from RAG.dm.dialog_state import (
    DialogState
)


class StateRepository:

    def __init__(self):

        self.states = {}


    def get(
        self,
        user_id: int
    ) -> DialogState:

        if user_id not in self.states:

            self.states[user_id] = (
                DialogState(
                    user_id=user_id
                )
            )

        return self.states[user_id]
    
    
    def save(
        self,
        state: DialogState
    ):

        self.states[
            state.user_id
        ] = state