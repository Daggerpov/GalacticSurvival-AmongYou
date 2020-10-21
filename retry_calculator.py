def retry_calculator(index):
    import main
    from main import lose, index, short_tasks, long_tasks
    from endMenu import end
    import math
    
    multiplier = 1

    if index == 0:
        multiplier = 2
    elif index == 1:
        multiplier = 1
    elif index == 2:
        multiplier = 0.5
    elif index == 3:
        multiplier = 0

    retry_amount = math.floor((multiplier * short_tasks) + (multiplier * long_tasks * 2))

    if retry_amount >= 0:
        lose = False
        return retry_amount
    else:
        lose = True
        end()
