# @param {String} moves
# @return {Integer}
def furthest_distance_from_origin(moves)
    return (moves.count "_")+ ((moves.count "L") - (moves.count "R")).abs
end