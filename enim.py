def remove_queued_move(self, queued_move):
    """Removes a move from the queue.

    Args:
        queued_move: The move to remove.
    """

    index = self._queued_moves.index(queued_move)
    del self._queued_moves[index]
