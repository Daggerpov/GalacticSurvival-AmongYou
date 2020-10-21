def retry_calculator(index, fails):
    import main
    from main import lose, index, short_tasks, long_tasks, screen, game_end
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
    retry_amount += fails

    if retry_amount >= 0:
        main.lose = False
        return retry_amount
    else:
        main.lose = True
        main.screen = 5
        main.game_end = True

